
from .entity import Entity

class DeadBodyEntity(Entity):

    def __init__(self, x, y, name = "dead body", chr = "%", color = (0,0,0), game = None):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = None, game = game, entity_type = "dead_body")
