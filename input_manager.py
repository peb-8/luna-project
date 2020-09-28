from game_state import GameState
from action_manager import ActionManager

class InputManager:

    @classmethod
    def check_bindings(cls):
        if "binding" in GameState.current_state:
            bindings = GameState.current_state["binding"]
            for binding in bindings:
                assert "type" in binding
                assert type("type") == str
                assert binding["type"]
                if binding["type"] == "keyboard":
                    assert "key_action" in binding
                    key_action = binding["key_action"]
                    assert type(key_action) == str
                    assert key_action in ("pressed", "released")
                    assert "key" in binding
                    key = binding["key"]
                    assert type(key) == int
                    assert key
                    assert "action" in binding
                    action = binding["action"]
                    assert type(action) == str
                    assert action
        
    @classmethod
    def key_press(cls, symbol):
        for binding in GameState.current_state["bindings"]:
            if binding["type"] == "keyboard":
                if binding["key_action"] == "pressed":
                    if binding["key"] == symbol:
                        action = binding["action"]
                        print(action)
                        getattr(ActionManager, action)()

    @classmethod
    def key_release(cls, symbol):
        for binding in GameState.current_state["bindings"]:
            if binding["type"] == "keyboard":
                if binding["key_action"] == "released":
                    if binding["key"] == symbol:
                        action = binding["action"]
                        print(action)
                        getattr(ActionManager, action)()
