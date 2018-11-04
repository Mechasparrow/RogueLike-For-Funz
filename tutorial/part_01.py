import tcod

# Declare constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

# fonts
font_path = '../font_images/arial10x10.png'
font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(font_path, font_flags)

# game window info
window_title = 'Python 3 libtcod tutorial'
fullscreen = False

# for exitting the game
exit_game = False

# initialize player_pos
player_x = 0
player_y = 0

# handle input
def handle_keys():
    global player_x, player_y
    global exit_game

    #movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player_y = player_y - 1
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_y = player_y + 1
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_x = player_x - 1
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_x = player_x + 1

    key = tcod.console_check_for_keypress()

    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt-enter toggle fullscreen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
    elif key.vk == tcod.KEY_ESCAPE:
        exit_game = True

tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)

while not exit_game:

    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(0,player_x, player_y, '@', tcod.BKGND_NONE)
    tcod.console_flush()

    tcod.console_put_char(0,player_x, player_y, ' ', tcod.BKGND_NONE)
    handle_keys()
