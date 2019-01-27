# Purpose: Base Pickup Model
# pickup.py
# Author: Michael Navazhylau

# polyfill
import sys
sys.path.append("..")

from engine.gameobjects import Entity

# combat
def grab_combat():
    from engine.combat import CombatBehavior
    return CombatBehavior


# Extends from entity
class BasePickUp(Entity):

    # Params
    # refer to entity params
    # pickup_type: Type of pickup

    def __init__(self, x, y, name, chr, color, combat_behavior = None, game = None, pickup_type = "basic"):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, game = game, entity_type = "pickup")
        self.pickup_type = pickup_type

    #serialization + parsing
    def as_dictionary(self):

        entity_dictionary = super().as_dictionary()

        pickup_dict = {
            'pickup_type': self.pickup_type
        }

        merged_dict = {**entity_dictionary, **pickup_dict}
        return merged_dict

    def from_dictionary(dictionary, g):

        CombatBehavior = grab_combat()

        parsed_combat_behavior = CombatBehavior.from_dictionary(dictionary['combat_behavior'], g)

        return BasePickUp( x = dictionary['x'], y = dictionary['y'], name = dictionary['name'], chr = dictionary['chr'], color = dictionary['color'], combat_behavior = parsed_combat_behavior, game = g)

    # Pickup Behavior of the pickup
    # Interacts with entity recieving the pickup
    def pickup_behavior(recieving_entity):

        pass
