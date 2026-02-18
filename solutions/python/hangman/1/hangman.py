# Game status categories
# Change the values as you see fit
# hangman.py

STATUS_ONGOING = "ongoing"
STATUS_WIN = "win"
STATUS_LOSE = "lose"


class Hangman:
    def __init__(self, word: str):
        self.word = word
        self.remaining_guesses = 9
        self._guessed = set()

    def get_masked_word(self) -> str:
        return "".join(ch if ch in self._guessed else "_" for ch in self.word)

    def get_status(self) -> str:
        if self.get_masked_word() == self.word:
            return STATUS_WIN
        if self.remaining_guesses < 0:
            return STATUS_LOSE
        return STATUS_ONGOING

    def guess(self, letter: str) -> None:
        # If game already ended, guessing is illegal.
        if self.get_status() in (STATUS_WIN, STATUS_LOSE):
            raise ValueError("The game has already ended.")

        # Repeating any previous guess is a failure.
        if letter in self._guessed:
            self.remaining_guesses -= 1
            return

        self._guessed.add(letter)

        # Incorrect guess is a failure.
        if letter not in self.word:
            self.remaining_guesses -= 1
            return
