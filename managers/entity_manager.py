from game_state import GameState


class EntityManager:

    @classmethod
    def get_by_id(cls, id):
        entities = GameState.current_state["entities"]
        if id > len(entities):
            raise Exception(f"Unable to find such entity with id: {id}")
        return entities[id]

    @classmethod
    def remove_by_id(cls, id):
        del GameState.current_state["entities"][id]

    @classmethod
    def tick(cls, dt):
        for id, ent in enumerate(GameState.current_state["entities"]):
            if "lifespan" in ent:
                if "elapsed" in ent:
                    ent["elapsed"] += dt
                    if ent["elapsed"] >= ent["lifespan"]:
                        ent["elapsed"] = ent["lifespan"]
                        cls.remove_by_id(id)
