from game_state import GameState
from action_manager import ActionManager

class ProcessManager:

    @classmethod
    def tick(cls, dt):
         for ps in GameState.current_state["process"]:
            ps["elapsed"]+=dt
            if ps["elapsed"] >= ps["period"]:
                ps["period"] = ps["elapsed"]-ps["period"]
            getattr(ActionManager, ps["action"])(ps)