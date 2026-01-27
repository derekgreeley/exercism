# swift_scheduling.py

from __future__ import annotations

from datetime import datetime, timedelta


def _is_workday(d: datetime) -> bool:
    return d.weekday() < 5  # Mon=0 .. Fri=4


def _first_workday(year: int, month: int) -> datetime:
    d = datetime(year, month, 1, 8, 0, 0)
    while not _is_workday(d):
        d += timedelta(days=1)
    return d


def _last_workday_of_month(year: int, month: int) -> datetime:
    # first day of next month minus one day
    if month == 12:
        d = datetime(year + 1, 1, 1)
    else:
        d = datetime(year, month + 1, 1)
    d -= timedelta(days=1)
    d = d.replace(hour=8, minute=0, second=0)
    while not _is_workday(d):
        d -= timedelta(days=1)
    return d


def _quarter_of_month(month: int) -> int:
    return (month - 1) // 3 + 1  # 1..4


def delivery_date(meeting_start: str, description: str) -> str:
    start = datetime.fromisoformat(meeting_start)

    if description == "NOW":
        return (start + timedelta(hours=2)).isoformat()

    if description == "ASAP":
        if start.hour < 13:
            return start.replace(hour=17, minute=0, second=0).isoformat()
        # tomorrow 13:00
        tomorrow = (start + timedelta(days=1)).replace(hour=13, minute=0, second=0)
        return tomorrow.isoformat()

    if description == "EOW":
        wd = start.weekday()  # Mon=0 .. Sun=6
        if wd <= 2:  # Mon/Tue/Wed -> Friday 17:00
            days_to_fri = 4 - wd
            target = start + timedelta(days=days_to_fri)
            target = target.replace(hour=17, minute=0, second=0)
            return target.isoformat()
        # Thu/Fri -> Sunday 20:00
        days_to_sun = 6 - wd
        target = start + timedelta(days=days_to_sun)
        target = target.replace(hour=20, minute=0, second=0)
        return target.isoformat()

    # Variable patterns: "<N>M" or "Q<N>"
    if description.endswith("M") and description[:-1].isdigit():
        n_month = int(description[:-1])
        year = start.year
        # "Before N-th month" means strictly earlier month
        if start.month < n_month:
            return _first_workday(year, n_month).isoformat()
        return _first_workday(year + 1, n_month).isoformat()

    if description.startswith("Q") and description[1:].isdigit():
        q = int(description[1:])
        current_q = _quarter_of_month(start.month)
        year = start.year
        # "Before or in N-th quarter" => current_q <= q
        if current_q <= q:
            end_month = q * 3
            return _last_workday_of_month(year, end_month).isoformat()
        end_month = q * 3
        return _last_workday_of_month(year + 1, end_month).isoformat()

    # Not required by the tests, but makes debugging nicer
    raise ValueError("Unknown delivery date description")
