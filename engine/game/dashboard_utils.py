# Purpose: Utils for interacting with game dashboards
# dashboard_utils.py
# Author: Michael Navazhylau

# Adds a dashboard to the game
def add_dashboard_to_game(game, dashboard):
    game.dashboards.append(dashboard)

def find_dashboard_by_type(game, type):

    # filter function by gameobject name
    def filter_by_type(dashboard):
        if (dashboard.dashboard_type == type):
            return True
        else:
            return False

    #return the filtered game objects
    filtered_dashboard = list(filter(filter_by_type, game.dashboards))
    return filtered_dashboard

def push_message_to_log(game, message):

    message_boards = find_dashboard_by_type(game, type = "log")

    if (len(message_boards) > 0):
        message_board = message_boards[0]
        message_board.log_message(message)
