import pyxel

from pongpy.interfaces.team import Team
from pongpy.models.game_info import GameInfo
from pongpy.models.state import State


class ManualTeam(Team):
    """
    デバッグ用の手動操作チーム。
    Pyxel を直接読んでいるのでデバッグ用と以外では利用しない。
    """
    @property
    def name(self) -> str:
        return 'Manual'

    def atk_action(self, info: GameInfo, state: State) -> int:
        if pyxel.btn(pyxel.KEY_I):
            return -info.atk_return_limit
        if pyxel.btn(pyxel.KEY_K):
            return info.atk_return_limit
        return 0

    def def_action(self, info: GameInfo, state: State) -> int:
        if pyxel.btn(pyxel.KEY_W):
            return -info.def_return_limit
        if pyxel.btn(pyxel.KEY_S):
            return info.def_return_limit
        return 0
