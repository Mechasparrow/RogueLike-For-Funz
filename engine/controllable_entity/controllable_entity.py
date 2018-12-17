from ..gameobjects.entity import Entity

class ControllableEntity(Entity):

    def __init__(self, x, y, name, chr, color, combat_behavior = None, available_actions = [], game = None):
        Entity.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, game = game, entity_type = "Controllable")
        self.available_actions = available_actions

    def get_actions_available(self):
        return self.available_actions

    # TODO consider dropping bodies

    def control_entity(self, action, callback=None):

        pass
