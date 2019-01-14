# Purpose: Util functions for dealing with game user input
# input_utils.py
# Author: Michael Navazhylau

# import libs
import tcod

# add a input handler to the game
def add_input_handler(game, input_handler):
    game.input_handlers.append(input_handler)

# handle user inputs
def handle_inputs(game):

    key = tcod.console_check_for_keypress()

    for handler in game.input_handlers:
        handler.handle_input(key)
