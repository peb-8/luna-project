from game_state import GameState
from action_manager import ActionManager

class TimerManager:
    
    @classmethod
    def tick(cls, dt):
        timers = GameState.current_state["timers"]
        for id, timer in enumerate(timers):
            timer["elapsed"]+=dt
            if timer["elapsed"] >= timer["duration"]:
                timer["duration"] = timer["elapsed"]
                del timers[id]
            if "action" in timer:
                getattr(ActionManager, timer["action"])(timer)
