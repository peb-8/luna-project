from entity_manager import EntityManager
from game_state import GameState
import math

class ActionManager:

    @classmethod
    def emit_particle(cls, process):
        ent = EntityManager.get_by_id(process["payload"]["entity_id"])
        vel = math.sqrt(ent["vel"][0]*ent["vel"][0] + ent["vel"][1]*ent["vel"][1])
        GameState.get_value("entities").append({
            "lifespan": .5,
            "elapsed": .0,
            "pos": ent["pos"][:],
            "rot": .0,
            "rvl": 0,
            "rac": 0,
            "vel": [vel*math.cos(ent["rot"]+math.pi), vel*math.sin(ent["rot"]+math.pi)],
            "acc": [.0, .0],
            "drawing": {
                "type": "particle",
                "color": [255, 255, 255],
                "radius": 20
            }
        })
        
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
        GameState.get_value("process").append({
            "period": 1.0,
            "action": "emit_particle",
            "elapsed": 0.0,
            "payload": {"entity_id": 0}
        })

    @classmethod
    def thruster_off(cls):
        ent = EntityManager.get_by_id(0)
        ent["acc"] = [0.0, 0.0]

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
        ent["rac"] = 0.0

    @classmethod
    def thruster_right_off(cls):
        ent = EntityManager.get_by_id(0)
        ent["rac"] = 0.0

    @classmethod
    def decay(cls, timer):
        ent = EntityManager.get_by_id(timer["payload"]["entity_id"])
        ratio = timer["elapsed"]/timer["period"]
        ent["drawing"]["color"][0]=(1-ratio)*255
        ent["drawing"]["color"][1]=(1-ratio)*255
        ent["drawing"]["color"][2]=(1-ratio)*255