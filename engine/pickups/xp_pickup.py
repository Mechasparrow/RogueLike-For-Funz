# Purpose: Pickup the gives XP
# xp_pickup.py
# Author: Michael Navazhylau

# Extends from BasePickUp
from .pickup import BasePickUp

# combat
def grab_combat():
    from engine.combat import CombatBehavior
    return CombatBehavior

class XPDrop(BasePickUp):

    # Same params as BasePickUp
    # with additional xp parameter that is amount of xp given when picked up
    def __init__(self, x, y, xp, name = "xp drop", chr = "*", color = (0, 255, 0), combat_behavior = None, game = None):
        BasePickUp.__init__(self, x, y, name, chr, color, combat_behavior, game = game, pickup_type = "xp_pickup")
        self.xp = xp

    #serialization + parsing
    def as_dictionary(self):

        pickup_dictionary = super().as_dictionary()

        xp_dict = {
            'xp': self.health
        }

        merged_dict = {**pickup_dictionary, **xp_dict}
        return merged_dict

    def from_dictionary(dictionary, g):
        CombatBehavior = grab_combat()

        parsed_combat_behavior = CombatBehavior.from_dictionary(dictionary['combat_behavior'], g)

        return XPDrop( x = dictionary['x'], y = dictionary['y'], xp = dictionary['xp'], name = dictionary['name'], chr = dictionary['chr'], color = dictionary['color'], combat_behavior = parsed_combat_behavior, game = g)

    # pickup behavior that gives the recieving entity xp
    def pickup_behavior(self,recieving_entity):
        if (recieving_entity.combat_behavior):
            recieving_entity.combat_behavior.gain_xp(self.xp)
        else:
            return
