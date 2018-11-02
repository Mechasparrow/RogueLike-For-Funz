# Make sure 'arial10x10.png' is in the same directory as this script.
import time

import tcod

# Setup the font.
tcod.console_set_custom_font(
    'arial10x10.png',tcod.FONT_LAYOUT_TCOD,
    )

player_x = 20
player_y = 20

end_game = False

def render_player(console):
    console.print_(x=player_x, y = player_y, string = '@')

def draw_box(console, x, y, width, height):

    console.hline(x,y, width)
    console.hline(x,y + (height -1),width)


    console.vline(x, y, height)
    console.vline(x + (width - 1), y, height)


    pass


# Initialize the root console in a context.
with tcod.console_init_root(80, 60, 'title') as root_console:
    while not end_game:

        root_console.clear()
        render_player(root_console)

        draw_box(root_console, 0, 0, 80, 60)
        
        xi = 5
        yi = 5

        dx = 15
        dy = 15

        for i in range(0,4):
            for c in range(0,3):
                draw_box(root_console, xi + (dx*i), yi + (dy*c), 15, 15)





        tcod.console_flush()

        # move the player up one
        player_y += 1

        time.sleep(0.01)

        if (player_y == 80):
            end_game = True

    time.sleep(30)
# The window is closed here, after the above context exits.
