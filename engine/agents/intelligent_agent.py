#
# intelligent_agent.py
# Base Class/Model for Intelligent Agents
# Author: Michael Navazhylau

# import libs
import tcod

# import polyfill
import sys
sys.path.append("..")

from engine.gameobjects import Entity, DeadBodyEntity

# Intelligent agent is sub class of Entities
class IntelligentAgent(Entity):

    def __init__(self, x, y, name, chr, color, combat_behavior = None, game = None):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, game = game, entity_type = "Agent")

    # Drops a body at the same location as the agent, preferably when dead.
    def drop_body(self):
        dead_body = DeadBodyEntity(self.x, self.y, color = self.color, game = self.game)
        return dead_body

    # abstract method for AI behavior of the intelligent agent
    def ai_behavior(self):

        pass
