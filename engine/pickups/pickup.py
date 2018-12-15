# polyfill
import sys
sys.path.append("..")

from engine.gameobjects import Entity

class BasePickUp(Entity):

    def __init__(self, x, y, name, chr, color, combat_behavior = None, game = None, pickup_type = "basic"):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, game = game, entity_type = "pickup")
        self.pickup_type = pickup_type

    def pickup_behavior(recieving_entity):
        
        pass
