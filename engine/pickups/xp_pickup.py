from .pickup import BasePickUp

class XPDrop(BasePickUp):

    def __init__(self, x, y, xp, name = "xp drop", chr = "*", color = (0, 255, 0), combat_behavior = None, game = None):
        BasePickUp.__init__(self, x, y, name, chr, color, combat_behavior, game = game, pickup_type = "xp_pickup")
        self.xp = xp

    def pickup_behavior(self,recieving_entity):
        if (recieving_entity.combat_behavior):
            recieving_entity.combat_behavior.gain_xp(self.xp)
        else:
            return
