from datetime import date, timedelta
import calendar


class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""
    def __init__(self, message: str):
        super().__init__(message)


# Map weekday names to datetime.weekday() numbers (Mon=0 ... Sun=6)
_WEEKDAY_MAP = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


def _first_weekday_on_or_after(start: date, target_wd: int) -> date:
    """Return the first date on or after `start` that has weekday `target_wd`."""
    delta = (target_wd - start.weekday()) % 7
    return start + timedelta(days=delta)


def meetup(year: int, month: int, which: str, weekday_name: str) -> date:
    """
    Return the exact meetup date for given year/month, week descriptor, and weekday name.

    `which` in {"first","second","third","fourth","fifth","last","teenth"}.
    """
    target_wd = _WEEKDAY_MAP[weekday_name]

    # Month boundaries
    _, last_day = calendar.monthrange(year, month)  # (weekday_of_first, days_in_month)
    first_of_month = date(year, month, 1)
    last_of_month = date(year, month, last_day)

    if which == "teenth":
        # Check days 13..19 and pick the one matching the weekday
        for d in range(13, 20):
            dt = date(year, month, d)
            if dt.weekday() == target_wd:
                return dt
        # Defensive fallback
        raise MeetupDayException("That day does not exist.")

    if which in {"first", "second", "third", "fourth", "fifth"}:
        first_occurrence = _first_weekday_on_or_after(first_of_month, target_wd)
        idx = {"first": 0, "second": 1, "third": 2, "fourth": 3, "fifth": 4}[which]
        candidate = first_occurrence + timedelta(days=7 * idx)
        if candidate.month == month:
            return candidate
        # e.g., nonexistent fifth weekday
        raise MeetupDayException("That day does not exist.")

    if which == "last":
        back = (last_of_month.weekday() - target_wd) % 7
        return last_of_month - timedelta(days=back)

    # Unknown descriptor
    raise MeetupDayException("That day does not exist.")
