import tcod
import time

from gameconstants import *

from engine.gameobject import *

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

def run():
    # initialize game end boolean
    game_end = False

    #initialize core console
    root_console = tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)

    #create the player
    player = GameObject(0,0, "@", (255, 255, 255))

    # objects
    objects = [player]


    # Set the game fps
    tcod.sys_set_fps(GAME_FPS)

    while not game_end:
        tcod.console_set_default_foreground(0, tcod.white)

        # render the game objects
        for object in objects:
            object.draw(root_console)

        tcod.console_flush()

        # clear the screen
        for object in objects:
            object.clear(root_console)


        game_action = handle_input()

        if (game_action == 'exit'):
            game_end = True



# Check if game is to be run
if __name__ == "__main__":
    run()
