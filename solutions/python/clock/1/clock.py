# clock.py

class Clock:
    _MINUTES_PER_DAY = 24 * 60

    def __init__(self, hour: int, minute: int):
        total = hour * 60 + minute
        self._minutes = total % self._MINUTES_PER_DAY  # normalizes negatives too

    @property
    def hour(self) -> int:
        return self._minutes // 60

    @property
    def minute(self) -> int:
        return self._minutes % 60

    def __repr__(self) -> str:
        # tests expect exactly "Clock(h, m)" with the normalized integers (no zero-pad)
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Clock):
            return NotImplemented
        return self._minutes == other._minutes

    def __add__(self, minutes: int):
        if not isinstance(minutes, int):
            return NotImplemented
        return Clock(0, self._minutes + minutes)

    def __sub__(self, minutes: int):
        if not isinstance(minutes, int):
            return NotImplemented
        return Clock(0, self._minutes - minutes)
