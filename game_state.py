from constants import GAME_STATES_FOLDER
import json


class GameState:

    current_state = {}

    @staticmethod
    def load(state_name: str):
        assert type(state_name) == str
        assert len(state_name) > 0
        with open(f"./{GAME_STATES_FOLDER}/{state_name}.json", "r") as f:
            GameState.current_state = json.load(f)

    @staticmethod
    def save(state_name: str):
        assert type(state_name) == str
        assert len(state_name) > 0
        with open(f"./{GAME_STATES_FOLDER}/{state_name}.json", "w") as f:
            json.dump(GameState.current_state, f)

    @staticmethod
    def get_node(path):
        current_node = GameState.current_state
        for part in path.split("."):
            try:
                if type(current_node) == list:
                    current_node = current_node[int(part)]
                elif type(current_node) == dict:
                    current_node = current_node[part]
            except Exception:
                raise Exception("Unknow path: " + path)
        return current_node

    @staticmethod
    def get_value(path):
        return GameState.get_node(path)

    @staticmethod
    def set_value(path, value):
        try:
            path_lst = path.split(".")
            node = GameState.get_node(".".join(path_lst[:-1]))
            node[path_lst[-1]] = value
        except Exception:
            raise Exception("Unknow path: " + path)
