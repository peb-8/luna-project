import arcade as ac
from game_state import GameState
from entity_manager import EntityManager
from drawing_manager import DrawingManager
from input_manager import InputManager
from motion_manager import MotionManager
from timer_manager import TimerManager
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

class Game(ac.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        GameState.load("default")
        ac.set_background_color(ac.color.AMAZON)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def run(self):
        ac.run()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        ac.start_render()
        DrawingManager.process()

    def on_key_press(self, symbol, modifiers):
        InputManager.key_press(symbol)

    def on_key_release(self, symbol, modifiers):
        InputManager.key_release(symbol)

    def on_update(self, dt):
        MotionManager.process(dt)
        TimerManager.process(dt)