import tcod
import time

from gameconstants import *

from engine.gameobject import *
from engine.game import *

# Setup the font
tcod.console_set_custom_font(
    FONT,
    FONT_FLAGS,
)

def handle_input():

    key = tcod.console_check_for_keypress()

    if (key.vk == tcod.KEY_ESCAPE):
        return 'exit'

    return 'no-key'

def core_logic(self):

    print ("counter: " + str(self.props["counter"]))
    if (self.props["counter"] >= 10):
        self.running = False


    self.props["counter"] += 1


def run():

    g = Game()

    g.props["counter"] = 0

    g.start_loop(core_logic)

    pass


# Check if game is to be run
if __name__ == "__main__":
    run()
