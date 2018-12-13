from .gameobject_utils import *

def add_agent_to_game(game, agent):
    add_gameobject_to_game(game, agent)

def get_game_agents(game):

    def filter_agents(object):
        if (object.type == "Entity"):
            if (object.entity_type == "Agent"):
                return True
        else:
            return False

    filtered_agents = list(filter(filter_agents, game.objects))

    return filtered_agents
