from .strategy import BattleStrategy
from .errors import InvalidStrategyError
from ex3 import Creature
from ex3 import TransformCapability


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature : Creature) -> bool:
        if not isinstance(creature, Creature):
            return (False)
        return (True)

    def act(self, creature : Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature : Creature) -> bool:
        if not isinstance(creature, TransformCapability):
            return (False)
        return (True)

    def act(self, creature : Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.get_name()}' "
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())



    

