import tcod
import time

from gameconstants import *
from keycodes import *

# Game engine
from engine.game import *
from engine.ui import *
from engine.mapping import *
from engine.combat import *
from engine.controllable_entity import *

def player_behavior(game, action):
    # Grab the player object
    player = find_gameobjects_by_name(game, "Player")[0]
    player.control_entity(action)

    if (player.combat_behavior.dead):
        gameover_dashboard.show_dashboard()

    game.map.compute_fov_map(player.x, player.y, radius = 8)

def general_game_behavior(game, action):

    if (action == 'exit'):
        game.stop_loop()

def core_logic(game):
    global gameover_dashboard

    handle_inputs(game)

    #handle death NOTE delegated to game class
    objects = game.objects
    for object in objects:
        if (object.combat_behavior):
            if (object.combat_behavior.dead == True and object.chr != "%"):
                object.chr = "%"

    player = find_gameobjects_by_name(game, "Player")[0]


def init_game(g):

    global gameover_dashboard

    # create dungeon
    dungeon = Dungeon(g,g.map, [])
    dungeon.push_dungeon_to_map()

    # grab random room to spawn in
    random_dungeon_room = dungeon.grab_random_room()
    (room_centre_x, room_centre_y) = random_dungeon_room.rect.center()

    # Turn based handler for game
    game_turn_handler = GameTurnHandler(g)

    # Add a player
    player_combat = CombatBehavior(max_health = 100, defense = 2, attack = 20)
    player = TurnBasedPlayer(room_centre_x, room_centre_y, "Player", "@", color = (255, 255, 255), combat_behavior = player_combat, turn_handler = game_turn_handler, game = g)

    player_dashboard = CombatDashboard(1,1, 60, 4, combat_behavior = player_combat)
    gameover_dashboard = CustomMessageDashboard(40,10,60,3, message = "Game Over")
    gameover_dashboard.hide_dashboard()

    dungeon.add_monsters_to_rooms(player)

    add_gameobject_to_game(g, player)
    add_dashboard_to_game(g, player_dashboard)
    add_dashboard_to_game(g, gameover_dashboard)

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
    add_input_handler(g, player_input_handler)
    add_input_handler(g, general_game_input_handler)



def run():

    game_font = Font(FONT, FONT_FLAGS)
    g = Game(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, game_font, fps=GAME_FPS)

    init_game(g)


    g.start_loop(core_logic)



# Check if game is to be run
if __name__ == "__main__":
    run()
