import tcod
import time

from gameconstants import *

# Setup the font
tcod.console_set_custom_font(
    FONT,
    FONT_FLAGS,
)

def draw_player(con, x, y):
    # Set the player color
    tcod.console_set_default_foreground(con, (255, 255, 255))
    # Draw the player on to the console
    tcod.console_put_char(con, x, y, "@", tcod.BKGND_NONE)

def clear_player(con, x, y):
    # Set the player color
    tcod.console_set_default_foreground(con, (255, 255, 255))
    # Draw the player on to the console
    tcod.console_put_char(con, x, y, " ", tcod.BKGND_NONE)

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

    player_x = 0

    # Set the game fps
    tcod.sys_set_fps(GAME_FPS)

    while not game_end:
        tcod.console_set_default_foreground(0, tcod.white)

        draw_player(root_console, player_x, 0)
        tcod.console_flush() # Show the console
        clear_player(root_console, player_x, 0)
        player_x += 1

        game_action = handle_input()

        if (game_action == 'exit'):
            game_end = True

# Check if game is to be run
if __name__ == "__main__":
    run()
