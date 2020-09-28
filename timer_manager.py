from game_state import GameState
from action_manager import ActionManager

class TimerManager:
    
    @classmethod
    def process(cls, dt):
        if "timers" in GameState.current_state:
            timers = GameState.current_state["timers"]
            for id, timer in enumerate(timers):
                timer["elapsed"]+=dt
                if timer["elapsed"] >= timer["duration"]:
                    if timer["repeatable"]:
                        timer["duration"] = timer["elapsed"]-timer["duration"]
                    else:
                        timer["duration"] = timer["elapsed"]
                        del timers[id]
                    if "end_action" in timer:
                        getattr(ActionManager, timer["end_action"])()
                getattr(ActionManager, timer["step_action"])(timer)
