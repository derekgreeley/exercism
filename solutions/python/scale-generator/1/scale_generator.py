# scale_generator.py

from __future__ import annotations


SHARPS = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLATS  = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

# Tonics that should use the flat spelling (major + minor)
USE_FLATS = {
    # Major
    "F", "Bb", "Eb", "Ab", "Db", "Gb",
    # Minor
    "d", "g", "c", "f", "bb", "eb",
}

STEP = {"m": 1, "M": 2, "A": 3}


def _normalize_tonic(tonic: str) -> str:
    """
    Return tonic with:
      - first char upper
      - accidental (#/b) preserved (b stays lowercase per spec)
    Examples:
      "c"  -> "C"
      "f#" -> "F#"
      "bb" -> "Bb"
      "eB" -> "Eb"
    """
    t = tonic.strip()
    if not t:
        return t
    t = t[0].upper() + t[1:].lower()
    # if it's a sharp, tests expect '#', not '♯'
    t = t.replace("♯", "#").replace("♭", "b")
    return t


class Scale:
    def __init__(self, tonic: str):
        self.tonic_raw = tonic
        self.tonic = _normalize_tonic(tonic)

        # Decide whether to use flats or sharps.
        # Per spec/tests: decision is based on "key signature" set (case-insensitive in input),
        # and we still output normalized tonic in proper casing.
        key = tonic.strip().replace("♯", "#").replace("♭", "b")
        self._use_flats = key in USE_FLATS

        self._scale = FLATS if self._use_flats else SHARPS

        if self.tonic not in self._scale:
            # In this Exercism exercise, tonics provided in tests are always valid.
            # If a user passes something weird, fail clearly.
            raise ValueError(f"Unknown tonic: {tonic!r}")

    def chromatic(self) -> list[str]:
        i = self._scale.index(self.tonic)
        return self._scale[i:] + self._scale[:i]

    def interval(self, intervals: str) -> list[str]:
        chrom = self.chromatic()

        notes = [chrom[0]]
        pos = 0
        for ch in intervals:
            pos = (pos + STEP[ch]) % 12
            notes.append(chrom[pos])
        return notes
