from game_state import GameState
from action_manager import ActionManager

class ProcessManager:

    @classmethod
    def tick(cls, dt):
         for ob in GameState.current_state["process"]:
            ob["elapsed"]+=dt
            if ob["elapsed"] >= ob["period"]:
                ob["period"] = ob["elapsed"]-ob["period"]
            getattr(ActionManager, ob["action"])(ob["payload"])