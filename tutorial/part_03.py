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

player.x = 25
player.y = 23

objects = [player]

# game map
MAP_WIDTH = 80
MAP_HEIGHT = 45

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

color_dark_wall = tcod.Color(0, 0, 100)
color_dark_ground = tcod.Color(50, 50, 150)

class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)

    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1
            and self.y1 <= other.y2 and self.y2 >= other.y1)

class Tile:
    #tile of map
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        #by default, if a tile is blocked, also block sight
        block_sight = blocked if block_sight is None else None
        self.block_sight = block_sight

def create_room(room):
    global map

    for x in range (room.x1 + 1, room.x2 + 1):
        for y in range(room.y1 + 1, room.y2 + 1):
            map[x][y].blocked = False
            map[x][y].block_sight = False

def create_h_tunnel(x1, x2, y):
    global map

    # horiz tunnel
    for x in range(min(x1, x2), max(x1, x2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False

def create_v_tunnel(y1, y2, x):
    global map

    # vertical tunnel
    for y in range(min(y1, y2), max(y1, y2) + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False

def make_map():
    global map

    # map with unblocked tiles
    map = [
        [Tile(True) for y in range (MAP_HEIGHT)]
        for x in range(MAP_WIDTH)
    ]

    rooms = []
    num_rooms = 0

    for r in range(MAX_ROOMS):
        # r width + height
        w = tcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = tcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        # random position without going out of boundaries
        x = tcod.random_get_int(0,0, MAP_WIDTH - w - 1)
        y = tcod.random_get_int(0,0,MAP_WIDTH - h - 1)

        new_room = Rect(x,y, w, h)

        #run to see if they failed
        failed = False
        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break

        if not failed:

            create_room(new_room)

            (new_x, new_y) = new_room.center()

            if num_rooms == 0:
                player.x = new_x
                player.y = new_y
        else:

            (prev_x, prev_y) = rooms[num_rooms-1].center()

            if tcod.random_get_int(0,0,1) == 1:
                create_h_tunnel(prev_x, new_x, prev_y)
                create_v_tunnel(prev_y, new_y, new_x)
            else:
                create_v_tunnel(prev_y, new_y, prev_x)
                create_h_tunnel(prev_x, new_x, new_y)

            rooms.append(new_room)
            num_rooms += 1

# create the map
make_map()

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
