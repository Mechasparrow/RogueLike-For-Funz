import tcod

# polyfill
import sys
sys.path.append("..")

from engine.gameobjects import Entity, DeadBodyEntity

class IntelligentAgent(Entity):

    def __init__(self, x, y, name, chr, color, combat_behavior = None, game = None):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, game = game, entity_type = "Agent")

    def drop_body(self):
        dead_body = DeadBodyEntity(self.x, self.y, color = self.color, game = self.game)
        return dead_body

    # abstract method
    def ai_behavior(self):

        pass
