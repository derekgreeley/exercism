import json
from typing import Any, Dict, List, Optional


class RestAPI:
    def __init__(self, database: Dict[str, Any]):
        # Database format: {"users": [userdict, ...]}
        self.database = database

    # ---------- Public API ----------

    def get(self, url: str, payload: Optional[str] = None) -> str:
        if url != "/users":
            raise ValueError(f"Unknown GET endpoint: {url}")

        if payload is None:
            users = self._sorted_users(self.database.get("users", []))
            return json.dumps({"users": users})

        requested = json.loads(payload).get("users", [])
        users = [self._get_user(name) for name in requested]
        users = self._sorted_users(users)
        return json.dumps({"users": users})

    def post(self, url: str, payload: str) -> str:
        data = json.loads(payload)

        if url == "/add":
            name = data["user"]
            user = {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}
            self.database.setdefault("users", []).append(user)
            return json.dumps(user)

        if url == "/iou":
            lender_name = data["lender"]
            borrower_name = data["borrower"]
            amount = float(data["amount"])

            lender = self._get_user(lender_name)
            borrower = self._get_user(borrower_name)

            self._apply_iou(lender, borrower, amount)

            # Recompute balances (tests expect exact floats)
            self._recalc_balance(lender)
            self._recalc_balance(borrower)

            result_users = self._sorted_users([lender, borrower])
            return json.dumps({"users": result_users})

        raise ValueError(f"Unknown POST endpoint: {url}")

    # ---------- Core IOU Logic ----------

    def _apply_iou(self, lender: Dict[str, Any], borrower: Dict[str, Any], amount: float) -> None:
        """
        lender lends borrower 'amount'.

        Netting rules:
        - If lender currently OWES borrower, reduce that first.
        - Otherwise increase borrower OWES lender (i.e., lender is OWED_BY borrower).
        """
        lender_name = lender["name"]
        borrower_name = borrower["name"]

        lender_owes_borrower = float(lender["owes"].get(borrower_name, 0.0))

        if lender_owes_borrower > 0:
            # Reduce existing opposite debt first
            if amount < lender_owes_borrower:
                # Still owes some
                new_owed = lender_owes_borrower - amount
                lender["owes"][borrower_name] = new_owed
                borrower["owed_by"][lender_name] = new_owed
                return

            if amount == lender_owes_borrower:
                # Debt cancels out completely
                lender["owes"].pop(borrower_name, None)
                borrower["owed_by"].pop(lender_name, None)
                return

            # amount > lender_owes_borrower -> flip direction with remainder
            remainder = amount - lender_owes_borrower
            lender["owes"].pop(borrower_name, None)
            borrower["owed_by"].pop(lender_name, None)

            # Now borrower owes lender remainder
            self._increase_debt(lender, borrower, remainder)
            return

        # No opposite debt: borrower owes lender amount
        self._increase_debt(lender, borrower, amount)

    def _increase_debt(self, lender: Dict[str, Any], borrower: Dict[str, Any], amount: float) -> None:
        lender_name = lender["name"]
        borrower_name = borrower["name"]

        # lender is owed_by borrower
        lender["owed_by"][borrower_name] = float(lender["owed_by"].get(borrower_name, 0.0)) + amount
        borrower["owes"][lender_name] = float(borrower["owes"].get(lender_name, 0.0)) + amount

    # ---------- Helpers ----------

    def _get_user(self, name: str) -> Dict[str, Any]:
        for user in self.database.get("users", []):
            if user["name"] == name:
                return user
        raise ValueError(f"Unknown user: {name}")

    def _recalc_balance(self, user: Dict[str, Any]) -> None:
        owed_by_total = sum(float(v) for v in user["owed_by"].values())
        owes_total = sum(float(v) for v in user["owes"].values())
        user["balance"] = owed_by_total - owes_total

    def _sorted_users(self, users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return sorted(users, key=lambda u: u["name"])
