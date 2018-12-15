from .agent_utils import *
from .gameobject_utils import *

# polyfill
import sys
sys.path.append("..")

from engine.pickups import XPDrop

class GameTurnHandler:
    def __init__(self, game):
        self.game = game

    def take_turn(self):


        agents = get_game_agents(self.game)
        for agent in agents:


            # TODO check if agent is ded
            if (agent.combat_behavior.dead):
                print ("DEAD")

                dead_body = agent.drop_body()

                # remove the agent
                remove_gameobject_from_game(self.game, agent)

                # push the new entities
                add_gameobject_to_game(self.game, dead_body)


                # drop the xp
                if (agent.combat_behavior):
                    if (agent.combat_behavior.get_combat_stats().xp_drop):
                        dropped_xp = XPDrop(agent.x, agent.y, xp = agent.combat_behavior.get_combat_stats().xp_drop, game = self.game)
                        add_gameobject_to_game(self.game, dropped_xp)

            #

            # TODO if agent is dead drop xp


            #

            agent.ai_behavior()
