# I- ABSTRACT PRODUCT 2

from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

    def is_transformed(self) -> bool:
        return (self._transformed)
