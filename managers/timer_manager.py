from game_state import GameState
from .action_manager import ActionManager

class TimerManager:
    
    @classmethod
    def tick(cls, dt):
        timers = GameState.current_state["timers"]
        for id, ob in enumerate(timers):
            ob["elapsed"]+=dt
            if ob["elapsed"] >= ob["duration"]:
                ob["duration"] = ob["elapsed"]
                getattr(ActionManager, ob["action"])(ob["payload"])
                del timers[id]
                
