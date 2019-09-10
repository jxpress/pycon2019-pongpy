from pongpy.interfaces.team import Team
from pongpy.models.game_info import GameInfo
from pongpy.models.state import State


class FollowTeam(Team):
    """
    現在のボールの位置似合わせて動くサンプル。
    """
    @property
    def name(self) -> str:
        return 'follow team'

    def atk_action(self, info: GameInfo, state: State) -> int:
        direction = (state.ball_pos.y - state.mine_team.atk_pos.y) > 0
        return info.atk_return_limit if direction else -info.atk_return_limit

    def def_action(self, info: GameInfo, state: State) -> int:
        direction = (state.ball_pos.y - state.mine_team.def_pos.y) > 0
        return info.def_return_limit if direction else -info.def_return_limit
