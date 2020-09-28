from game_state import GameState
import arcade as ac
import math
 
class DrawingManager:

    @classmethod
    def process(cls):
        if "entities" in GameState.current_state:
            for ent in GameState.current_state["entities"]:
                if "pos" in ent and "rot" in ent and "drawing" in ent:
                    cls.draw(ent["pos"], ent["rot"], ent["drawing"])
    
    @classmethod
    def draw(cls, pos, rot, drawing):
        if "type" in drawing:
            if drawing["type"] == "filled_circle":
                color = drawing["color"] if "color" in drawing else (0, 0, 0)
                radius = drawing["radius"] if "radius" in drawing else 20
                ac.draw_circle_filled(pos[0], pos[1], radius, color)
            if drawing["type"] == "filled_triangle":
                color = drawing["color"] if "color" in drawing else (0, 0, 0)
                radius = drawing["radius"]
                x, y = pos[0], pos[1]
                a1 =  -math.pi/2 + rot + math.pi/2
                a2 =   math.pi/6 + rot + math.pi/2
                a3 = 5*math.pi/6 + rot + math.pi/2
                p1 = [radius*math.cos(a1), radius*math.sin(a1)]
                p2 = [radius*math.cos(a2), radius*math.sin(a2)]
                p3 = [radius*math.cos(a3), radius*math.sin(a3)]
                ac.draw_triangle_filled(
                    x + p1[0], y + p1[1], x + p2[0], y + p2[1], x + p3[0], y + p3[1],
                    color
                )