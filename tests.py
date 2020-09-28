from game_state import GameState
from entity_manager import EntityManager
from constants import GAME_STATES_FOLDER

class Test:

    @classmethod 
    def setup_class(cls):
        GameState.current_state = {
            "test": {
                "val1": True,
                "val2": 85,
                "val3": [1, 5, {"val4": 88, "to_change": False}, 4]
            },
            "val5": 3.14,
            "entities": [
                {"id": 0, "pos": [0, 0]},
                {"id": 0, "pos": [0, 0]}
            ]
        }
        GameState.save("test")
        GameState.current_state = None

    @classmethod 
    def teardown_class(cls):
        import os
        os.remove(f"./{GAME_STATES_FOLDER}/test.json") 

    def test_game_state_saving_and_loading(self):
        GameState.load("test")
        assert GameState.current_state != None
        
    def test_game_state_reading_value(self):
        val1 = GameState.get_value("test.val1")
        assert type(val1) == bool
        assert val1 == True
        val2 = GameState.get_value("test.val2")
        assert type(val2) == int
        assert val2 == 85
        val3 = GameState.get_value("test.val3")
        assert type(val3) == list
        assert len(val3) == 4
        val4 = GameState.get_value("test.val3.2.val4")
        assert type(val4) == int
        assert val4 == 88
        val5 = GameState.get_value("val5")
        assert type(val5) == float
        assert val5 == 3.14

    def test_game_state_writing_value(self):
        GameState.set_value("test.val3.2.to_change", True)
        to_change = GameState.get_value("test.val3.2.to_change")
        assert type(to_change) == bool
        assert to_change == True

    def test_entity_manager_checking(self):
        id_doublon_detected = False
        try:
            EntityManager.check_all()
        except:
            id_doublon_detected = True
        if not id_doublon_detected:
            raise "Entity manager has missed an id doublon"
        GameState.set_value("entities.1.id", 1)
        EntityManager.check_all()

