from entity_manager import EntityManager
import math

class ActionManager:

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
        ratio = timer["elapsed"]/timer["duration"]
        ent["drawing"]["color"][0]=(1-ratio)*255
        ent["drawing"]["color"][1]=(1-ratio)*255
        ent["drawing"]["color"][2]=(1-ratio)*255
        print(int(ratio*100))