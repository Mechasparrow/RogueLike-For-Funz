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

    def __init__(self, x, y, char, name, color, blocks = False):
        self.name = name
        self.blocks = blocks
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # move by a delta

        if not is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def draw(self):
        #set the color then draw the character for this object at its pos

        if tcod.map_is_in_fov(fov_map, self.x, self.y):
            tcod.console_set_default_foreground(con, self.color)
            tcod.console_put_char(con, self.x, self.y, self.char, tcod.BKGND_NONE)

    def clear(self):
        #erase the character that reps this object
        tcod.console_put_char(con, self.x, self.y, ' ', tcod.BKGND_NONE)

# game objects
player = Object(0, 0, '@', 'player', tcod.white, blocks = True)


objects = [player]

# game map
MAP_WIDTH = 80
MAP_HEIGHT = 45

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

MAX_ROOM_MONSTERS = 3

# FOV constants
FOV_ALGO = 0
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10
fov_recompute = True

color_dark_wall = tcod.Color(0, 0, 100)
color_light_wall = tcod.Color(130,110,50)

color_dark_ground = tcod.Color(50, 50, 150)
color_light_ground = tcod.Color(200, 180, 50)

class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return (center_x, center_y)

    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1
            and self.y1 <= other.y2 and self.y2 >= other.y1)

class Tile:
    #tile of map
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
        self.explored = False

        #by default, if a tile is blocked, also block sight
        block_sight = blocked if block_sight is None else None
        self.block_sight = block_sight


def create_room(room):
    global map

    for x in range (room.x1 + 1, room.x2 + 1):
        for y in range(room.y1 + 1, room.y2 + 1):
            map[x][y].blocked = False
            map[x][y].block_sight = False

def place_objects(room):
    #random num of monsters
    num_monsters = tcod.random_get_int(0,0,MAX_ROOM_MONSTERS)

    for i in range (num_monsters):
        # choose random spot for this monster
        x = tcod.random_get_int(0, room.x1, room.x2)
        y = tcod.random_get_int(0, room.y1, room.y2)

        if not is_blocked(x, y):
            if tcod.random_get_int(0, 0, 100) < 80: #80$ chance of getting orc
                #create orc
                monster = Object(x, y, 'o', 'orc', tcod.desaturated_green, blocks = True)
            else:
                #create a troll
                monster = Object(x, y, 'T', 'troll', tcod.darker_green, blocks = True)

            objects.append(monster)

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
        #rand width and height
        w = tcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = tcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)

        # random pos
        x = tcod.random_get_int(0,0, MAP_WIDTH - w - 1)
        y = tcod.random_get_int(0,0, MAP_HEIGHT - h - 1)

        # New room
        new_room = Rect(x, y, w, h)

        # run through other rooms to check for collision
        failed = False

        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break

        if not failed:
            # paint the room
            create_room(new_room)

            #center coordinates of new room

            (new_x, new_y) = new_room.center()

            if num_rooms == 0:
                player.x = new_x
                player.y = new_y


        else:

            #center coordinates of prev room
            (prev_x, prev_y) = rooms[num_rooms-1].center()

            if tcod.random_get_int(0,0,1) == 1:

                create_h_tunnel(prev_x, new_x, prev_y)
                create_v_tunnel(prev_y, new_y, new_x)
            else:
                create_v_tunnel(prev_y, new_y, prev_x)
                create_h_tunnel(prev_x, new_x, new_y)

        rooms.append(new_room)
        place_objects(new_room)

        num_rooms += 1

def is_blocked(x, y):
    if map[x][y].blocked:
        return True

    #check for any blocking objects
    for object in objects:
        if object.blocks and object.x == x and object.y == y:
            return True

    return False


# create the map
make_map()

fov_map = tcod.map_new(MAP_WIDTH, MAP_HEIGHT)
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        tcod.map_set_properties(fov_map, x, y, not map[x][y].block_sight, not map[x][y].blocked)

# render function
def render_all():
    global fov_recompute


    if fov_recompute:
        fov_recompute = False
        tcod.map_compute_fov(fov_map, player.x, player.y, TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGO)


    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            visible = tcod.map_is_in_fov(fov_map, x, y)
            wall = map[x][y].block_sight

            if not visible:
                if map[x][y].explored:
                    if wall:
                        tcod.console_set_char_background(con, x, y, color_dark_wall, tcod.BKGND_SET)
                    else:
                        tcod.console_set_char_background(con, x, y, color_dark_ground, tcod.BKGND_SET)
            else:
                if wall:
                    tcod.console_set_char_background(con, x, y, color_light_wall, tcod.BKGND_SET)
                else:
                    tcod.console_set_char_background(con, x, y, color_light_ground, tcod.BKGND_SET)

                map[x][y].explored = True

    #draw all object in object list
    for object in objects:
        object.draw()

    tcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

# handle input
def handle_keys():
    global exit_game
    global fov_recompute


    player_dx = 0
    player_dy = 0

    #movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player_dy = -1
        fov_recompute = True
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_dy = 1
        fov_recompute = True
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_dx = -1
        fov_recompute = True
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_dx = 1
        fov_recompute = True

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


# main game loop
while not exit_game:

    tcod.console_set_default_foreground(0, tcod.white)
    render_all()

    tcod.console_flush()

    for object in objects:
        object.clear()

    handle_keys()
