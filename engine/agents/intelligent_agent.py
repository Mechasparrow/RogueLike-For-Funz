import tcod

from ..gameobjects.entity import Entity

class IntelligentAgent(Entity):

    def __init__(self, x, y, name, chr, color, combat_behavior = None, game = None):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior, game)

    # abstract method
    def ai_behavior(self):

        pass
