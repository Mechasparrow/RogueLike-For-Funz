# Purpose: A Entity that's just a general "dead" entity
# dead_body.py
# Author: Michael Navazhylau


from .entity import Entity

# Extends from base entity
class DeadBodyEntity(Entity):

    def __init__(self, x, y, name = "dead body", chr = "%", color = (0,0,0), game = None):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = None, game = game, entity_type = "dead_body")
