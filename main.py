import tcod
import time

from gameconstants import *
from keycodes import *

# Game engine
from engine.gameobject import *
from engine.game import *
from engine.font import *
from engine.input_handler import *

# Gameobject modifiers
from engine.fighter import Fighter

# Mapping
from engine.mapping.tile import Tile
from engine.mapping.room import Room
from engine.mapping.dungeon import Dungeon

# Setup the font
tcod.console_set_custom_font(
    FONT,
    FONT_FLAGS,
)

def player_behavior(game, action):

    # Grab the player object
    player = game.find_gameobjects_by_name("Player")[0]
    turn_taken = False

    # Movement offset from current pos
    dx = 0
    dy = 0

    if (action == "up"):
        dy = -1
        turn_taken = True
    elif (action == "down"):
        dy = 1
        turn_taken = True
    elif (action == "right"):
        dx = 1
        turn_taken = True
    elif (action == "left"):
        dx = -1
        turn_taken =True

    # Move the player
    player.move(dx, dy)

    # Move the enemy
    monster = game.find_gameobjects_by_name("Gobta")[0]

    if (turn_taken == True):
        monster.fighter.nav(player)



def general_game_behavior(game, action):

    if (action == 'exit'):
        game.stop_loop()

def core_logic(game):
    game.handle_inputs()

    player = game.find_gameobjects_by_name("Player")[0]

    game.fov_map.compute_fov(player.x, player.y, radius = 8, light_walls = True, algorithm = 0)


def init_game(g):

    # create dungeon
    dungeon = Dungeon(g,g.map, [])
    dungeon.push_dungeon_to_map()

    # grab random room to spawn in
    random_dungeon_room = dungeon.grab_random_room()
    (room_centre_x, room_centre_y) = random_dungeon_room.rect.center()

    # Add a player
    player = GameObject(room_centre_x, room_centre_y, "Player", "@", color = (255, 255, 255), entity = True, game = g)

    # Add a monter
    monster_fighter = Fighter(20, 5, 4)
    monster = GameObject(room_centre_x + 2, room_centre_y + 2, "Gobta", "G", color = (255,0, 0), entity = True, fighter = monster_fighter, game = g)

    # Add initial game objects
    g.add_gameobject_to_game(player)
    g.add_gameobject_to_game(monster)

    # input handlers
    # ============== #
    # player handler
    player_key_actions = {
        "up": UP_KEY,
        "down": DOWN_KEY,
        "right": RIGHT_KEY,
        "left": LEFT_KEY
    }
    player_input_handler = InputHandler(g, player_key_actions)
    player_input_handler.add_behavior(player_behavior)

    # game handler
    game_key_actions = {
        "exit": tcod.KEY_ESCAPE
    }
    general_game_input_handler = InputHandler(g, game_key_actions)
    general_game_input_handler.add_behavior(general_game_behavior)

    # Add input handlers
    g.add_input_handler(player_input_handler)
    g.add_input_handler(general_game_input_handler)



def run():

    game_font = Font(FONT, FONT_FLAGS)
    g = Game(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, game_font, fps=GAME_FPS)

    init_game(g)


    g.start_loop(core_logic)



# Check if game is to be run
if __name__ == "__main__":
    run()
