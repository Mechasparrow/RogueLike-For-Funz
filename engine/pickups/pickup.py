# Purpose: Base Pickup Model
# pickup.py
# Author: Michael Navazhylau

# polyfill
import sys
sys.path.append("..")

from engine.gameobjects import Entity

# Extends from entity
class BasePickUp(Entity):

    # Params
    # refer to entity params
    # pickup_type: Type of pickup

    def __init__(self, x, y, name, chr, color, combat_behavior = None, game = None, pickup_type = "basic"):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, game = game, entity_type = "pickup")
        self.pickup_type = pickup_type

    # Pickup Behavior of the pickup
    # Interacts with entity recieving the pickup
    def pickup_behavior(recieving_entity):

        pass
