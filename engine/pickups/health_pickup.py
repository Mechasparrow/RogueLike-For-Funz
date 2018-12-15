from .pickup import BasePickUp

class HealthDrop(BasePickUp):

    def __init__(self, x, y, health, name = "health drop", chr = "*", color = (255, 0, 0), combat_behavior = None, game = None):
        BasePickUp.__init__(self, x, y, name, chr, color, combat_behavior, game = game, pickup_type = "health_pickup")
        self.health = health

    def pickup_behavior(self,recieving_entity):
        if (recieving_entity.combat_behavior):
            recieving_entity.combat_behavior.gain_health(self.health)
            print ("pickup!")
        else:
            return
