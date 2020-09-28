from game_state import GameState

class EntityManager:

    @classmethod
    def get_by_id(cls, id):
        entities = GameState.current_state["entities"]
        if id > len(entities):
            raise Exception(f"Unable to find such entity with id: {id}")
        return entities[id]