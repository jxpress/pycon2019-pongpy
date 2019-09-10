import random
from pongpy.interfaces.team import Team
from pongpy.models.game_info import GameInfo
from pongpy.models.state import State


class RandomTeam(Team):
    """
    ランダムに折り返して動くサンプル。
    """
    atk_direction = -1
    def_direction = -1

    @property
    def name(self) -> str:
        return 'random team'

    def atk_action(self, info: GameInfo, state: State) -> int:
        if random.random() > 0.9:
            self.atk_direction *= -1
        return self.atk_direction

    def def_action(self, info: GameInfo, state: State) -> int:
        if random.random() > 0.95:
            self.def_direction *= -1
        return self.def_direction
