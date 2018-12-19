#
#   main.py
#   purpose: entry point for the game
#   @author Michael Navazhylau
#

# Import additional libs
import tcod
import time

# Import constants
from gameconstants import *
from keycodes import *

# Import Game engine
from engine.game import *
from engine.ui import *
from engine.mapping import *
from engine.combat import *
from engine.controllable_entity import *

# Player behavior based off of current key pressed
def player_behavior(game, action):
    # Grab the player object
    player = find_gameobjects_by_name(game, "Player")[0]
    player.control_entity(action)

    if (player.combat_behavior.dead):
        gameover_dashboard.show_dashboard()

    game.map.compute_fov_map(player.x, player.y, radius = 8)

# Generate game behavior
# includes exitting the game, pausing, etc
def general_game_behavior(game, action):

    if (action == 'exit'):
        game.stop_loop()

# Core logic of the game in question
def core_logic(game):
    # TODO retrieve dashboard from game instead
    global gameover_dashboard

    # handle the game inputs
    handle_inputs(game)

    #handle death TODO delegated to game class
    objects = game.objects
    for object in objects:
        if (object.combat_behavior):
            if (object.combat_behavior.dead == True and object.chr != "%"):
                object.chr = "%"

# Initialize the game world + constituents
def init_game(g):

    # TODO seperate into more functions for kicks and giggles
    # TODO don't make this GLOBAL!!!!
    global gameover_dashboard

    # Turn based handler for game
    game_turn_handler = GameTurnHandler(g)

    # Create the player
    player_combat = CombatBehavior.create_combat_behavior_manual(max_health = 100, defense = 2, attack = 20)
    player = TurnBasedPlayer(0, 0, "Player", "@", color = (255, 255, 255), combat_behavior = player_combat, turn_handler = game_turn_handler, game = g)

    # create dungeon
    dungeon = Dungeon(g,g.map, [])
    dungeon.push_dungeon_to_map()

    # grab random room to spawn in TODO make into dungeon function
    random_dungeon_room = dungeon.grab_random_room()
    (room_centre_x, room_centre_y) = random_dungeon_room.rect.center()

    # Put Player in random dungeon
    player.x = room_centre_x
    player.y = room_centre_y

    # Add player to the game
    add_gameobject_to_game(g, player)

    # Add monsters and pickups to the dungeon
    dungeon.add_monsters_to_rooms(player)
    dungeon.add_health_to_rooms(chance = 0.5)
    dungeon.add_stairs_to_dungeon(chance = 0.3)

    # Create UI dashboards
    player_dashboard = CombatDashboard(1,1, 60, 6, combat_behavior = player_combat)
    gameover_dashboard = CustomMessageDashboard(40,10,60,3, message = "Game Over")
    gameover_dashboard.hide_dashboard()

    # Add dashboards to the game
    add_dashboard_to_game(g, player_dashboard)
    add_dashboard_to_game(g, gameover_dashboard)

    # input handlers

    ## player input handler
    player_key_actions = {
        "up": UP_KEY,
        "down": DOWN_KEY,
        "right": RIGHT_KEY,
        "left": LEFT_KEY
    }
    player_input_handler = InputHandler(g, player_key_actions)
    player_input_handler.add_behavior(player_behavior)

    ## game handler
    game_key_actions = {
        "exit": tcod.KEY_ESCAPE
    }
    general_game_input_handler = InputHandler(g, game_key_actions)
    general_game_input_handler.add_behavior(general_game_behavior)

    # Add input handlers to the game
    add_input_handler(g, player_input_handler)
    add_input_handler(g, general_game_input_handler)


def run():

    # create game font
    game_font = Font(FONT, FONT_FLAGS)

    # create game console with props
    g = Game(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, game_font, fps=GAME_FPS)

    # initialize the game (generate dungeon, create player, etc)
    init_game(g)

    # start the main game loops
    g.start_loop(core_logic)


# Check if game is to be run
if __name__ == "__main__":
    run()
