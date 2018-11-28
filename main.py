import tcod
import time

from gameconstants import *
from keycodes import *

# Game engine
from engine.gameobject import *
from engine.game import *
from engine.font import *
from engine.input_handler import *

# Mapping
from engine.mapping.tile import *

# Setup the font
tcod.console_set_custom_font(
    FONT,
    FONT_FLAGS,
)

def player_behavior(game, action):

    # Grab the player object
    player = game.find_gameobjects_by_name("Player")[0]

    # Movement offset from current pos
    dx = 0
    dy = 0

    if (action == "up"):
        dy = -1
    elif (action == "down"):
        dy = 1
    elif (action == "right"):
        dx = 1
    elif (action == "left"):
        dx = -1

    # Move the player
    player.move(dx, dy)


def general_game_behavior(game, action):

    if (action == 'exit'):
        game.stop_loop()

def core_logic(game):
    game.handle_inputs()

def init_game(g):
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


def run():

    game_font = Font(FONT, FONT_FLAGS)
    g = Game(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, game_font, fps=GAME_FPS)

    init_game(g)


    g.start_loop(core_logic)



# Check if game is to be run
if __name__ == "__main__":
    run()
