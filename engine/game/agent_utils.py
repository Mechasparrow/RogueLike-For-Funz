# Purpose: Utils for interacting specifically with agent gameobjects
# agent_utils.py
# Author: Michael Navazhylau

# Utilize gameobject utils
from .gameobject_utils import *

# Add a agent entity to the game
def add_agent_to_floor(floor, agent):
    add_gameobject_to_floor(floor, agent)

# Retrieve all agent entities from the game
def get_game_agents(floor):

    def filter_agents(object):
        if (object.type == "Entity"):
            if (object.entity_type == "Agent"):
                return True
        else:
            return False

    filtered_agents = list(filter(filter_agents, floor.objects))

    return filtered_agents
