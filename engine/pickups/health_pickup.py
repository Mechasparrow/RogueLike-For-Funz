# Purpose: Health Pickup Model
# health_pickup.py
# Author: Michael Navazhylau

# Extends from BasePickUp
from .pickup import BasePickUp

# combat
def grab_combat():
    from engine.combat import CombatBehavior
    return CombatBehavior

class HealthDrop(BasePickUp):

    # Same params as BasePickUp
    # with additional of health attribute
    # Amount health gained when picked up
    def __init__(self, x, y, health, name = "health drop", chr = "*", color = (255, 0, 0), combat_behavior = None, game = None):
        BasePickUp.__init__(self, x, y, name, chr, color, combat_behavior, game = game, pickup_type = "health_pickup")
        self.health = health

    #serialization + parsing
    def as_dictionary(self):

        pickup_dictionary = super().as_dictionary()

        health_dict = {
            'health': self.health
        }

        merged_dict = {**pickup_dictionary, **health_dict}
        return merged_dict

    def from_dictionary(dictionary, g):

        CombatBehavior = grab_combat()

        parsed_combat_behavior = CombatBehavior.from_dictionary(dictionary['combat_behavior'], g)


        return HealthDrop( x = dictionary['x'], y = dictionary['y'], health = dictionary['health'], name = dictionary['name'], chr = dictionary['chr'], color = dictionary['color'], combat_behavior = parsed_combat_behavior, game = g)

    def pickup_behavior(self,recieving_entity):
        if (recieving_entity.combat_behavior):
            recieving_entity.combat_behavior.gain_health(self.health)

        else:
            return
