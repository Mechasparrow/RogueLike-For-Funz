# Purpose: Handler for User Input and associated behavior typed to input actions
# input_handler.py
# Author: Michael Navazhylau

# import libs
import tcod

class InputHandler:
    # Single input checker.. no combos

    # @param actions is a hash table like so
    # {"action": "keycode":} etc etc

    # behaviors
    # functions to run when the input handler is triggered

    def __init__(self, game, actions):
        self.game = game
        self.actions = actions
        self.behaviors = []

    # add an behavior function to run
    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    # Handle user input based on key code passed
    def handle_input(self,key):

        key_code = key.vk
        key_char = chr(key.c)

        input_action = None

        # run through and see what actions apply
        for (action, key) in self.actions.items():
            if (key == key_code):
                input_action = action
            elif (key_code == tcod.KEY_CHAR):
                if (key == key_char):
                    input_action = action

        # pass action to behaviors
        for behavior in self.behaviors:
            behavior(self.game, input_action)
