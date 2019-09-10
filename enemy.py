from pongpy.interfaces.team import Team
from pongpy.models.game_info import GameInfo
from pongpy.models.state import State


class EnemyTeam(Team):
    @property
    def name(self) -> str:
        return 'ENEMY'

    def atk_action(self, info: GameInfo, state: State) -> int:
        return 1

    def def_action(self, info: GameInfo, state: State) -> int:
        return 1
