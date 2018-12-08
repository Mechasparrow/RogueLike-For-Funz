import tcod
import time

from gameconstants import *
from keycodes import *

# Game engine
from engine.gameobject import *
from engine.game import *
from engine.font import *
from engine.input_handler import *

# Dashboards
from engine.ui.fighter_dashboard import FighterDashboard
from engine.ui.custom_message_dashboard import CustomMessageDashboard

# Fighting
from engine.fighter import Fighter
from engine.ai.ai_monster import MonsterAI

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

    (predicted_pos_x, predicted_pos_y) = (player.x + dx, player.y + dy)

    gameobjects_at_next_position = game.find_gameobjects_at_point(predicted_pos_x, predicted_pos_y)

    # Move the player
    if (turn_taken == True and player.fighter.dead != True):
        if not (len(gameobjects_at_next_position) > 0):
            player.move(dx, dy)
        else:
            all_good = False
            # if the next position as a gameobject, check if it is a fighter. If so, attack
            for gameobject in gameobjects_at_next_position:
                can_walk_over = False
                if (gameobject.fighter):
                    enemy_fighter = gameobject.fighter
                    if (enemy_fighter.dead):
                        can_walk_over = True
                    else:
                        player.fighter.attack(enemy_fighter)

            if (can_walk_over):
                player.move(dx, dy)

    # Move the enemy

    if (turn_taken == True and player.fighter.dead != True):

        for gameobject in game.objects:
            fighter = gameobject.fighter
            if (fighter):
                if (fighter.ai):
                    fighter.ai.perform_ai()


def general_game_behavior(game, action):

    if (action == 'exit'):
        game.stop_loop()

def core_logic(game):
    global gameover_dashboard

    game.handle_inputs()

    player = game.find_gameobjects_by_name("Player")[0]

    if (player.fighter.dead == True):
        gameover_dashboard.show_dashboard()

    game.fov_map.compute_fov(player.x, player.y, radius = 8, light_walls = True, algorithm = 0)


def init_game(g):

    global gameover_dashboard

    # create dungeon
    dungeon = Dungeon(g,g.map, [])
    dungeon.push_dungeon_to_map()

    # grab random room to spawn in
    random_dungeon_room = dungeon.grab_random_room()
    (room_centre_x, room_centre_y) = random_dungeon_room.rect.center()

    # Add a player
    player_fighter = Fighter(health = 100, defense = 2, damage = 20)
    player = GameObject(room_centre_x, room_centre_y, "Player", "@", color = (255, 255, 255), entity = True, fighter = player_fighter, game = g)

    player_dashboard = FighterDashboard(1,1, 60, 4, fighter = player_fighter)
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
