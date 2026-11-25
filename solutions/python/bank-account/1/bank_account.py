class BankAccount:
    def __init__(self):
        self._balance = 0
        self._is_open = False

    def get_balance(self):
        self._validate_account()
        return self._balance

    def open(self):
        if self._is_open:
            raise ValueError("account already open")

        self._balance = 0
        self._is_open = True

    def deposit(self, amount):
        self._validate_account()
        self._validate_amount(amount)

        self._balance += amount

    def withdraw(self, amount):
        self._validate_account()
        self._validate_amount(amount)

        if amount > self._balance:
            raise ValueError("amount must be less than balance")

        self._balance -= amount

    def close(self):
        self._validate_account()

        self._is_open = False
        self._balance = 0

    def _validate_account(self):
        if not self._is_open:
            raise ValueError("account not open")

    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than 0")