# bowling.py

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("invalid number of pins")

        if self._is_complete():
            raise IndexError("cannot roll after game is over")

        self._validate_roll(pins)
        self.rolls.append(pins)

    def score(self):
        if not self._is_complete():
            raise IndexError("score cannot be taken until the end of the game")

        score = 0
        i = 0

        for _ in range(10):
            if self.rolls[i] == 10:  # strike
                score += 10 + self.rolls[i + 1] + self.rolls[i + 2]
                i += 1
            elif self.rolls[i] + self.rolls[i + 1] == 10:  # spare
                score += 10 + self.rolls[i + 2]
                i += 2
            else:  # open frame
                score += self.rolls[i] + self.rolls[i + 1]
                i += 2

        return score

    def _validate_roll(self, pins):
        frame = 1
        i = 0
        n = len(self.rolls)

        # Walk frames 1-9
        while frame < 10 and i < n:
            first = self.rolls[i]
            if first == 10:
                i += 1
                frame += 1
            else:
                if i + 1 < n:
                    i += 2
                    frame += 1
                else:
                    # second roll in a frame before the 10th
                    if first + pins > 10:
                        raise ValueError("pin count exceeds pins on the lane")
                    return

        # Still before 10th frame, starting a fresh frame
        if frame < 10:
            return

        # Validate 10th frame
        tenth = self.rolls[i:]

        if len(tenth) == 0:
            return

        if len(tenth) == 1:
            first = tenth[0]
            if first != 10 and first + pins > 10:
                raise ValueError("pin count exceeds pins on the lane")
            return

        if len(tenth) == 2:
            first, second = tenth

            if first == 10:
                # In 10th after strike:
                # - if first fill ball is strike, second fill can be 0..10
                # - otherwise second fill must keep fill-ball frame <= 10
                if second != 10 and second + pins > 10:
                    raise ValueError("invalid fill balls")
                return

            if first + second < 10:
                raise IndexError("cannot throw bonus with an open tenth frame")

            # spare in 10th -> one fill ball allowed, any 0..10
            return

        if len(tenth) == 3:
            raise IndexError("game already has ten frames")

        raise IndexError("game already has ten frames")

    def _is_complete(self):
        i = 0

        # Frames 1-9
        for _ in range(9):
            if i >= len(self.rolls):
                return False
            if self.rolls[i] == 10:
                i += 1
            else:
                if i + 1 >= len(self.rolls):
                    return False
                i += 2

        # 10th frame
        remaining = len(self.rolls) - i
        if remaining < 2:
            return False

        first = self.rolls[i]
        second = self.rolls[i + 1]

        if first == 10:
            if remaining < 3:
                return False
            third = self.rolls[i + 2]

            if second != 10 and second + third > 10:
                raise ValueError("invalid fill balls")
            return remaining == 3

        if first + second == 10:
            return remaining == 3

        return remaining == 2