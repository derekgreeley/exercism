# robot_name.py

import random
import string


class Robot:
    # Class-level set to track all names that have ever been used
    _used_names = set()

    def __init__(self):
        self._name = None

    @property
    def name(self) -> str:
        """Return the robot's name, generating it if necessary."""
        if self._name is None:
            self._name = self._generate_unique_name()
        return self._name

    def reset(self) -> None:
        """Reset the robot to factory settings with a new unique name."""
        self._name = self._generate_unique_name()

    @classmethod
    def _generate_unique_name(cls) -> str:
        """Generate a unique name: two uppercase letters + three digits."""
        while True:
            letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
            digits = ''.join(random.choice(string.digits) for _ in range(3))
            candidate = letters + digits
            if candidate not in cls._used_names:
                cls._used_names.add(candidate)
                return candidate
