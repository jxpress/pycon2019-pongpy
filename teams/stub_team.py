from pongpy.interfaces.team import Team
from pongpy.models.game_info import GameInfo
from pongpy.models.state import State


class StubTeam(Team):
    """
    初期位置のまま動かないサンプル。
    """
    @property
    def name(self) -> str:
        return 'stub team'

    def atk_action(self, info: GameInfo, state: State) -> int:
        return 0

    def def_action(self, info: GameInfo, state: State) -> int:
        return 0
