import tcod
import time

from gameconstants import *
from keycodes import *

from engine.gameobject import *
from engine.game import *
from engine.font import *
from engine.input_handler import *

# Setup the font
tcod.console_set_custom_font(
    FONT,
    FONT_FLAGS,
)

def player_behavior(game, action):

    pass

def general_game_behavior(game, action):

    if (action == 'exit'):
        game.stop_loop()

def core_logic(game):
    pass

def run():

    game_font = Font(FONT, FONT_FLAGS)
    g = Game(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, game_font, fps=GAME_FPS)

    # Add a player
    player = GameObject(0, 0, "Player", "@", color = (255, 255, 255))
    g.add_gameobject_to_game(player)

    # input handlers

    # player handler
    player_key_actions = {
        "up": UP_KEY,
        "down": DOWN_KEY,
        "right": RIGHT_KEY,
        "left": LEFT_KEY
    }
    player_input_handler = InputHandler(g, player_key_actions)
    player_input_handler.add_behavior(player_behavior)

    # game handler
    game_key_actions = {
        "exit": tcod.KEY_ESCAPE
    }
    general_game_input_handler = InputHandler(g, game_key_actions)
    general_game_input_handler.add_behavior(general_game_behavior)

    # Add input handlers
    g.add_input_handler(player_input_handler)
    g.add_input_handler(general_game_input_handler)

    g.start_loop(core_logic)



# Check if game is to be run
if __name__ == "__main__":
    run()
