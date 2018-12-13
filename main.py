import tcod
import time

from gameconstants import *
from keycodes import *

# Game engine
from engine.gameobjects.gameobject import GameObject
from engine.gameobjects.entity import Entity
from engine.game import *
from engine.font import *
from engine.input_handler import *

# Dashboards
from engine.ui.combat_dashboard import CombatDashboard
from engine.ui.custom_message_dashboard import CustomMessageDashboard

# Fighting
from engine.combat.combat_behavior import CombatBehavior

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
    elif (action == "down"):
        dy = 1
    elif (action == "right"):
        dx = 1
    elif (action == "left"):
        dx = -1

    if (dx != 0 or dy != 0):
        turn_taken = True

    (potential_x, potential_y) = player.anticipate_move(dx, dy)


    #FIXME Turn based behavior
    if not (player.combat_behavior.dead):
        safe_to_move = True
        for object in game.objects:
            if (object.x == potential_x and object.y == potential_y):
                safe_to_move = False
                if (object.combat_behavior):
                    if (object.combat_behavior.dead):
                        safe_to_move = True

        for agent in game.agents:
            if (agent.x == potential_x and agent.y == potential_y):
                player.combat_behavior.attack(agent.combat_behavior)

        if (safe_to_move):
            player.move(dx, dy)

        if (turn_taken):
            agents = game.agents
            for agent in agents:
                agent.ai_behavior()


def general_game_behavior(game, action):

    if (action == 'exit'):
        game.stop_loop()

def core_logic(game):
    global gameover_dashboard

    game.handle_inputs()

    #handle death
    objects = game.objects
    for object in objects:
        if (object.combat_behavior):
            if (object.combat_behavior.dead == True and object.chr != "%"):
                object.chr = "%"

    player = game.find_gameobjects_by_name("Player")[0]

    # DEBUG
    if (player.combat_behavior.dead):
        gameover_dashboard.show_dashboard()

    game.map.compute_fov_map(player.x, player.y, radius = 8)


def init_game(g):

    global gameover_dashboard

    # create dungeon
    dungeon = Dungeon(g,g.map, [])
    dungeon.push_dungeon_to_map()

    # grab random room to spawn in
    random_dungeon_room = dungeon.grab_random_room()
    (room_centre_x, room_centre_y) = random_dungeon_room.rect.center()

    # Add a player
    player_combat = CombatBehavior(max_health = 100, defense = 2, attack = 20)
    player = Entity(room_centre_x, room_centre_y, "Player", "@", color = (255, 255, 255), combat_behavior = player_combat, game = g)

    # FIXME stat dashboard
    player_dashboard = CombatDashboard(1,1, 60, 4, combat_behavior = player_combat)
    gameover_dashboard = CustomMessageDashboard(40,10,60,3, message = "Game Over")
    gameover_dashboard.hide_dashboard()

    dungeon.add_monsters_to_rooms(player)

    g.add_gameobject_to_game(player)
    g.add_dashboard_to_game(player_dashboard)
    g.add_dashboard_to_game(gameover_dashboard)

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
