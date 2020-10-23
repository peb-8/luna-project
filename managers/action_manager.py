from .entity_manager import EntityManager
from game_state import GameState
import math
from factory import Factory

class ActionManager:

    @classmethod
    def emit_particle(cls, payload):
        ent_id = payload["entity_id"]
        ent = EntityManager.get_by_id(ent_id)
        GameState.get_value("entities").append(
            Factory.create_particle(
                ent["pos"].copy(), .0,
                math.sqrt(ent["vel"][0]*ent["vel"][0] + ent["vel"][1]*ent["vel"][1])
            )
        )
        
    @classmethod
    def move_up(cls):
        ent = EntityManager.get_by_id(0)
        ent["pos"][1]+=10

    @classmethod
    def move_right(cls):
        ent = EntityManager.get_by_id(0)
        ent["pos"][0]+=10

    @classmethod
    def move_down(cls):
        ent = EntityManager.get_by_id(0)
        ent["pos"][1]-=10.0

    @classmethod
    def move_left(cls):
        ent = EntityManager.get_by_id(0)
        ent["pos"][0]-=10.0

    @classmethod
    def thruster_on(cls):
        ent = EntityManager.get_by_id(0)
        ent["acc"][0] = 100.0*math.cos(ent["rot"])
        ent["acc"][1] = 100.0*math.sin(ent["rot"])
        GameState.get_value("process").append(
            Factory.create_process(
                1.0, "emit_particle", {"entity_id": 0}
            )
        )

    @classmethod
    def thruster_off(cls):
        ent = EntityManager.get_by_id(0)
        ent["acc"] = [.0, .0]

    @classmethod
    def thruster_left_on(cls):
        ent = EntityManager.get_by_id(0)
        ent["rac"] =  2.0

    @classmethod
    def thruster_right_on(cls):
        ent = EntityManager.get_by_id(0)
        ent["rac"] = -2.0

    @classmethod
    def thruster_left_off(cls):
        ent = EntityManager.get_by_id(0)
        ent["rac"] = .0

    @classmethod
    def thruster_right_off(cls):
        ent = EntityManager.get_by_id(0)
        ent["rac"] = .0

    @classmethod
    def decay(cls, payload):
        ent_id = payload["entity_id"]
        ent = EntityManager.get_by_id(ent_id)
        timer_id = payload["timer_id"]
        timer = GameState.current_state["timers"][timer_id]
        print(timer)
        ratio = timer["elapsed"]/timer["duration"]
        ent["drawing"]["color"][0]=(1-ratio)*255
        ent["drawing"]["color"][1]=(1-ratio)*255
        ent["drawing"]["color"][2]=(1-ratio)*255