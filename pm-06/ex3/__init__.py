# III and IV
from .factories import CreatureFactory, FlameFactory, TransformCreatureFactory
# I
from .creature import Creature
from .capability import TransformCapability

__all__ = [
    "Creature",
    "TransformCapability",
    "CreatureFactory",
    "FlameFactory",
    "TransformCreatureFactory"
]
