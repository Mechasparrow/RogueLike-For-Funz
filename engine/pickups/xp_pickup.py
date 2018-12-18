# Purpose: Pickup the gives XP
# xp_pickup.py
# Author: Michael Navazhylau

# Extends from BasePickUp
from .pickup import BasePickUp

class XPDrop(BasePickUp):

    # Same params as BasePickUp
    # with additional xp parameter that is amount of xp given when picked up
    def __init__(self, x, y, xp, name = "xp drop", chr = "*", color = (0, 255, 0), combat_behavior = None, game = None):
        BasePickUp.__init__(self, x, y, name, chr, color, combat_behavior, game = game, pickup_type = "xp_pickup")
        self.xp = xp

    # pickup behavior that gives the recieving entity xp
    def pickup_behavior(self,recieving_entity):
        if (recieving_entity.combat_behavior):
            recieving_entity.combat_behavior.gain_xp(self.xp)
        else:
            return
