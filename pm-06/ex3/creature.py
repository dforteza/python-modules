# I - ABSTRACT PRODUCT 1

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        super().__init__()
        self._name: str = name
        self._type: str = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f'{self._name} is a {self._type} type Creature')

    def get_name(self) -> str:
        return (self._name)

    def get_type(self) -> str:
        return (self._type)
