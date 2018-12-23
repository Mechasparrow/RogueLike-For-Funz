# Provides Base Controllable Entity that is controlled through a series of actions
# controllable_entity.py
# Author: Michael Navazhylau

# import polyfill
import sys
sys.path.append("..")

from engine.gameobjects import Entity, DeadBodyEntity

class ControllableEntity(Entity):

    # Initialize object
    def __init__(self, x, y, name, chr, color, combat_behavior = None, available_actions = [], game = None):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, game = game, entity_type = "Controllable")

        # Pass set of available actions for the controllable entity as a param
        self.available_actions = available_actions

    # function to retrieve list of available actions for said entity
    def get_actions_available(self):
        return self.available_actions

    # Returns a dead version of the controllable entity
    def drop_body(self):
        dead_body = DeadBodyEntity(self.x , self.y, color = self.color, game = self.game)
        return dead_body

    # Main function that controls entity based off certain action passed in via other entity interaction, keyboard control, etc
    def control_entity(self, action, callback=None):

        pass
