#
#   main.py
#   purpose: entry point for the game
#   @author Michael Navazhylau
#

# Import additional libs
import tcod
import time
import copy
import sys

# Import constants
from gameconstants import *
from keycodes import *

# JSON
import json
import pickle

# Import Game engine
from engine.game import *
from engine.floors import *
from engine.ui import *
from engine.mapping import *
from engine.combat import *
from engine.controllable_entity import *
from engine.floors import DungeonFloorManager
from engine.menu import *

# Player behavior based off of current key pressed
def player_behavior(game, action):

    if (len(find_gameobjects_by_name(game.floor_manager.get_current_floor(), "Player")) > 0 and game.game_state == "playing"):
        player = find_gameobjects_by_name(game.floor_manager.get_current_floor(), "Player")[0]
        player.control_entity(action)

        # If dead drop a body TODO
        if (player.combat_behavior.dead):
            gameover_dashboard.show_dashboard()
            print ("still dead")

        game.floor_manager.get_current_floor().game_map.compute_fov_map(player.x, player.y, radius = 8)


# Generate game behavior
# includes exitting the game, pausing, etc
def general_game_behavior(game, action):

    if (action == 'exit'):
        game.stop_loop()
    elif (action == 'reset'):
        reset_game(game)
    elif (action == 'menu'):
        game.game_state = "in_menu"

# Core logic of the game in question
def core_logic(game):
    # TODO retrieve dashboard from game instead
    global gameover_dashboard
    global floor_dashboard

    # DEBUG update floor number
    floor_dashboard.set_message("Current floor: " + str(game.floor_manager.current_floor_number))

    # handle the game inputs
    handle_inputs(game)

# Save and Load algorithms
# TODO extrapolate into its own class for simplification
# WARNING not functional

def save_game(g):

    floor_dungeon = g.floor_manager

    with open('saves/game.pickle', 'wb+') as f:
        floor_data = floor_dungeon.as_dictionary()
        #print (floor_data)
        f.write(pickle.dumps(floor_data))
        f.close()

def load_game(g):

    with open('saves/game.pickle', 'rb') as f:
        floor_dungeon = pickle.load(f)
        parsed_floor_dungeon = DungeonFloorManager.from_dictionary(floor_dungeon, g)
        print (parsed_floor_dungeon.current_floor_number)
        g.floor_manager = parsed_floor_dungeon

        player_dashboards = find_dashboard_by_name(g, "player_dash")
        players = find_gameobjects_by_name(g.floor_manager.get_current_floor(), "Player")

        if (len(player_dashboards) > 0 and len(players) > 0):
            player_dashboard = player_dashboards[0]
            player_combat = players[0].combat_behavior
            player_dashboard.combat_behavior = player_combat

        print ("GAME LOADED")
        g.game_state = "playing"


# Hard reset of the game
# TODO extrapolate into its own class for simplification

def reset_game(g):

    global player

    # TODO reset the player properties


    # Create the player
    # TODO allows leveling system to be have ability to reset stats along with combat behavior

    # Turn based handler for game
    game_turn_handler = GameTurnHandler(g)

    # Reset player stats
    player_leveling_system = LevelingSystem(update_stat_deltas = LevelingSystem.generate_update_stats_deltas(1, 1, 1, 0))
    player_leveling_system.enable_dashboard_logging(g)
    player_combat = CombatBehavior.create_combat_behavior_manual(max_health = 100, defense = 2, attack = 10, leveling_system = player_leveling_system)
    player_combat.game = g
    player = TurnBasedPlayer(0, 0, "Player", "@", color = (255, 255, 255), combat_behavior = player_combat, turn_handler = game_turn_handler, game = g)

    # Reset player dashboard and gameover dashboard

    # TODO simplify
    player_dashboards = find_dashboard_by_name(g, "player_dash")
    if (len(player_dashboards) > 0):
        player_dashboard = player_dashboards[0]
        player_dashboard.combat_behavior = player_combat

    # TODO simplify
    gameover_dashboards = find_dashboard_by_name(g, "gameover_dash")
    if (len(gameover_dashboards) > 0):
        gameover_dashboard = gameover_dashboards[0]
        gameover_dashboard.hide_dashboard()


    # spawn rates for dungeon
    dungeon_spawn_rates = DungeonSpawnStats(monsters_per_room = 3, health_chance = 0.5, stairs_chance = 0.4, upward_stairs_chance = 0.4, chest_spawn_chance = 0.5)

    # create dungeon
    g.floor_manager = FloorManager((g.window_width * 3) // 4, g.window_height, game = g)
    dungeon_floor_manager = DungeonFloorManager(g.floor_manager.floor_width, g.floor_manager.floor_height, floors = g.floor_manager.floors, main_entity = player, dungeon_spawn_stats = dungeon_spawn_rates, game = g)
    g.floor_manager = dungeon_floor_manager

    # generate the next floor
    g.floor_manager.generate_and_go_to_next_floor()

# Initialize the game world + constituents

def init_game(g):

    # TODO seperate into more functions for kicks and giggles
    # TODO don't make this GLOBAL!!!!
    global gameover_dashboard
    global floor_dashboard
    global player


    # Turn based handler for game
    game_turn_handler = GameTurnHandler(g)

    # Create the player
    player_leveling_system = LevelingSystem(update_stat_deltas = LevelingSystem.generate_update_stats_deltas(1, 1, 1, 0))
    player_leveling_system.enable_dashboard_logging(g)
    player_combat = CombatBehavior.create_combat_behavior_manual(max_health = 100, defense = 2, attack = 10, leveling_system = player_leveling_system)
    player_combat.game = g
    player = TurnBasedPlayer(0, 0, "Player", "@", color = (255, 255, 255), combat_behavior = player_combat, turn_handler = game_turn_handler, game = g)

    # spawn rates for dungeon
    dungeon_spawn_rates = DungeonSpawnStats(monsters_per_room = 3, health_chance = 0.5, stairs_chance = 0.4, upward_stairs_chance = 0.4, chest_spawn_chance = 0.5)

    # create dungeon
    dungeon_floor_manager = DungeonFloorManager(g.floor_manager.floor_width, g.floor_manager.floor_height, floors = g.floor_manager.floors, main_entity = player, dungeon_spawn_stats = dungeon_spawn_rates, game = g)
    g.floor_manager = dungeon_floor_manager

    # generate the next floor
    g.floor_manager.generate_and_go_to_next_floor()


    # Create UI dashboards
    player_dashboard = CombatDashboard(1,1, 80, 6, dashboard_name = "player_dash", combat_behavior = player_combat)

    # DEBUG floor dashboard
    floor_dashboard = CustomMessageDashboard(1, 6, 80, 2, message = "Current floor: " + str(g.floor_manager.current_floor_number))

    gameover_dashboard = CustomMessageDashboard(40,10,60,3, message = "Game Over",  dashboard_name = "gameover_dash")
    gameover_dashboard.hide_dashboard()


    # Add dashboards to the game
    add_dashboard_to_game(g, player_dashboard)
    add_dashboard_to_game(g, gameover_dashboard)
    add_dashboard_to_game(g, floor_dashboard)

    # input handlers

    ## Menu input handler
    # TODO temporary
    menu_key_actions = {
        "menu_up": UP_KEY,
        "menu_down": DOWN_KEY,
        "menu_select": ENTER_KEY
    }
    menu_input_handler = InputHandler(g, menu_key_actions)
    menu_input_handler.add_behavior(g.main_menu.handle_menu_interaction)

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
        "exit": tcod.KEY_ESCAPE,
        "reset": "r",
        "menu": "m"
    }
    general_game_input_handler = InputHandler(g, game_key_actions)
    general_game_input_handler.add_behavior(general_game_behavior)

    # Add input handlers to the game
    add_input_handler(g, player_input_handler)
    add_input_handler(g, general_game_input_handler)
    add_input_handler(g, menu_input_handler)

def run():

    # create game font
    game_font = Font(FONT, FONT_FLAGS)


    # menu functions
    # TODO put somewhere else
    def start_game(game):
        game.game_state = "playing"

    def exit_game(game):
        game.stop_loop()


    # create the main menu for the game
    main_menu_items = [MenuItem(text="Start Game", menu_action = start_game), MenuItem(text="Exit", menu_action = exit_game), MenuItem(text="Save", menu_action = save_game), MenuItem(text="Load", menu_action = load_game)]
    main_menu = MenuSystem(SCREEN_WIDTH, SCREEN_HEIGHT)
    main_menu.selected_menu_screen.menu_options = main_menu_items
    main_menu.selected_menu_screen.set_selected_option(main_menu_items[0])

    # create game console with props
    g = Game(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, game_font, fps=GAME_FPS, main_menu=main_menu)

    init_game(g)
    # initialize the game (generate dungeon, create player, etc)

    # start the main game loops
    g.start_loop(core_logic)


# Check if game is to be run
if __name__ == "__main__":
    run()
