### II- PRODUCTS

from .creature import Creature
from .capability import TransformCapability


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return (f"{self.get_name()} uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return (f"{self.get_name()} uses Flamethrower!")


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    # Creature Methods
    def attack(self) -> str:
        if self.is_transformed():
            return (f"{self.get_name()} performs a boosted strike!")
        else:
            return (f"{self.get_name()} attacks normally.")

    # TransformCapability Methods
    def transform(self) -> str:
        self._transformed = True
        return (f"{self.get_name()} shifts into a sharper form!")

    def revert(self) -> str:
        self._transformed = False
        return (f"{self.get_name()} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    # Creature Methods
    def attack(self) -> str:
        if self.is_transformed():
            return (f"{self.get_name()} unleashes a devastating morph strike!")
        else:
            return (f"{self.get_name()} attacks normally.")

    # TransformCapability Methods
    def transform(self) -> str:
        self._transformed = True
        return (f"{self.get_name()} morphs into a dragonic battle form!")

    def revert(self) -> str:
        self._transformed = False
        return (f"{self.get_name()} stabilizes its form.")
