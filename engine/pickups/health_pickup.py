# Purpose: Health Pickup Model
# health_pickup.py
# Author: Michael Navazhylau

# Extends from BasePickUp
from .pickup import BasePickUp

class HealthDrop(BasePickUp):

    # Same params as BasePickUp
    # with additional of health attribute
    # Amount health gained when picked up
    def __init__(self, x, y, health, name = "health drop", chr = "*", color = (255, 0, 0), combat_behavior = None, game = None):
        BasePickUp.__init__(self, x, y, name, chr, color, combat_behavior, game = game, pickup_type = "health_pickup")
        self.health = health

    def pickup_behavior(self,recieving_entity):
        if (recieving_entity.combat_behavior):
            recieving_entity.combat_behavior.gain_health(self.health)
    
        else:
            return
