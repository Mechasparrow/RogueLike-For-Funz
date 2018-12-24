# Purpose: Turn Handler for the Game in turn based games
# game_turn_handler.py
# Author: Michael Navazhylau

# Utilize additional utils
from .agent_utils import *
from .gameobject_utils import *

# polyfill
import sys
sys.path.append("..")

# Game pickups
from engine.pickups import XPDrop

class GameTurnHandler:
    def __init__(self, game):
        self.game = game

    # Execute the game's/computer's turn for turn based games
    def take_turn(self):

        # run all the agent ai behavior
        # check if any agents are dead, drop their body + pickups FIXME
        agents = get_game_agents(self.game.get_current_floor())
        # iterate through all the agents
        for agent in agents:
            if (agent.combat_behavior.dead):

                # remove the agent from the game FIXME
                remove_gameobject_from_game(self.game.get_current_floor(), agent)

                # Drop a dead body
                dead_body = agent.drop_body()

                # add the dead body to the game FIXME
                add_gameobject_to_game(self.game.get_current_floor(), dead_body)

                # drop the xp FIXME
                if (agent.combat_behavior):
                    if (agent.combat_behavior.get_combat_stats().xp_drop):
                        dropped_xp = XPDrop(agent.x, agent.y, xp = agent.combat_behavior.get_combat_stats().xp_drop, game = self.game)
                        add_gameobject_to_game(self.game.get_current_floor(), dropped_xp)

            # AI agent behavior
            agent.ai_behavior()
