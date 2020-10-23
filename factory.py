import math
class Factory:
    
    @classmethod
    def create_particle(cls, pos:list, rot:float, abs_vel:float)->dict:
        assert type(pos) == list
        assert type(rot) == float
        assert type(abs_vel) == float
        return dict(
            cls.create_entity(pos, rot, [.0, .0], .0), **{
                "lifespan": .5,
                "elapsed": .0,
                "vel": [
                    abs_vel*math.cos(rot+math.pi),
                    abs_vel*math.sin(rot+math.pi)
                ],
                "drawing": {
                    "type": "particle",
                    "color": [255, 255, 255],
                    "radius": 20
                }
            }
        )

    @classmethod
    def create_entity(cls, pos:list, rot:float, vel:list, rvl:float)->dict:
        assert type(pos) == list
        assert type(rot) == float
        assert type(vel) == list
        assert type(rvl) == float
        return {
            "pos": pos.copy(),
            "rot": .0,
            "rvl": .0,
            "rac": .0,
            "vel": vel.copy(),
            "acc": [.0, .0]
        }

    @classmethod
    def create_process(cls, period:float, action:str, payload:dict={})->dict:
        assert type(period) == float
        assert type(action) == str
        assert type(payload) == dict
        return {
            "period": period,
            "action": action,
            "elapsed": .0,
            "payload": payload
        }

    @classmethod
    def create_timer(cls, duration:float, action:str, payload:dict={})->dict:
        assert type(duration) == float
        assert type(action) == str
        assert type(payload) == dict
        return {
            "duration": duration,
            "action": action,
            "elapsed": .0,
            "payload": payload
        }

    @classmethod
    def create_binding(cls, binding_type:str, key_action:str, key:int, action:str, payload:dict={})->dict:
        assert type(binding_type) == str
        assert type(key_action) == str
        assert type(key) == int
        assert type(action) == str
        assert type(payload) == dict
        return {
            "type": binding_type,
            "key_action": key_action,
            "key": key,
            "action": action,
            "payload": payload
        }