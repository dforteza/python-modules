from abc import ABC, abstractmethod
from .creature import Creature
from .entities import Flameling, Pyrodon, Shiftling, Morphagon

### III- ABSTRACT FACTORY ###
class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass

### IV- FACTORY ###
class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Flameling())

    def create_evolved(self) -> Creature:
        return (Pyrodon())

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Shiftling())

    def create_evolved(self) -> Creature:
        return (Morphagon())