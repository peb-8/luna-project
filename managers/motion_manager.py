from game_state import GameState
import arcade as ac

class MotionManager:

    @classmethod
    def check_entity(cls, entity):
        pass

    @classmethod
    def tick(cls, dt):
        for ent in GameState.current_state["entities"]:
            if "pos" in ent and \
               "vel" in ent and \
               "acc" in ent and \
               "rot" in ent and \
               "rvl" in ent:
                ent["vel"][0]+=ent["acc"][0]*dt
                ent["vel"][1]+=ent["acc"][1]*dt
                ent["pos"][0]+=ent["vel"][0]*dt
                ent["pos"][1]+=ent["vel"][1]*dt
                ent["rot"]+=ent["rvl"]*dt
                ent["rvl"]+=ent["rac"]*dt