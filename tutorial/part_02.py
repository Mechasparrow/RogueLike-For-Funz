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

# off screen console
con = tcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

# Object generalization
class Object:
    # generic object for most things

    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # move by a delta

        if not map[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

    def draw(self):
        #set the color then draw the character for this object at its pos
        tcod.console_set_default_foreground(con, self.color)
        tcod.console_put_char(con, self.x, self.y, self.char, tcod.BKGND_NONE)

    def clear(self):
        #erase the character that reps this object
        tcod.console_put_char(con, self.x, self.y, ' ', tcod.BKGND_NONE)

# game objects
player = Object(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, '@', tcod.white)
npc = Object(SCREEN_WIDTH // 2 - 5, SCREEN_HEIGHT // 2, '@', tcod.yellow)
objects = [npc, player]

# game map
MAP_WIDTH = 80
MAP_HEIGHT = 45

color_dark_wall = tcod.Color(0, 0, 100)
color_dark_ground = tcod.Color(50, 50, 150)

class Tile:
    #tile of map
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        #by default, if a tile is blocked, also block sight
        block_sight = blocked if block_sight is None else None
        self.block_sight = block_sight

def make_map():
    global map

    # map with unblocked tiles
    map = [
        [Tile(False) for y in range (MAP_HEIGHT)]
        for x in range(MAP_WIDTH)
    ]

# create the map
make_map()

map[30][22].blocked = True
map[30][22].block_sight = True
map[50][22].blocked = True
map[50][22].block_sight = True

# handle input
def handle_keys():
    global exit_game

    player_dx = 0
    player_dy = 0

    #movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player_dy = -1
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_dy = 1
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_dx = -1
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_dx = 1

    # move the player
    player.move(player_dx, player_dy)

    # check for specific key presses combos, etc
    key = tcod.console_check_for_keypress()

    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt-enter toggle fullscreen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
    elif key.vk == tcod.KEY_ESCAPE:
        exit_game = True

# set the game fps
tcod.sys_set_fps(LIMIT_FPS)

# initialize the root console
tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)

# render function
def render_all():
    #draw all object in object list
    for object in objects:
        object.draw()

    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = map[x][y].block_sight

            if wall:
                tcod.console_set_char_background(con, x, y, color_dark_wall, tcod.BKGND_SET)
            else:
                tcod.console_set_char_background(con, x, y, color_dark_ground, tcod.BKGND_SET)

# main game loop
while not exit_game:

    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(0,player_x, player_y, '@', tcod.BKGND_NONE)

    render_all()

    tcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    tcod.console_flush()

    for object in objects:
        object.clear()

    handle_keys()
