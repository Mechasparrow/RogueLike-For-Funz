class InputHandler:
    # Single input checker.. no combos

    # @param actions is a hash table like so
    # {"keycode": "action":} etc etc

    def __init__(self, game, actions):
        self.game = game
        self.actions = actions
        self.behaviors = []

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def handle_input(self,key_code):

        input_action = None

        # run through and see what actions apply
        for (action, key) in self.actions.items():
            if (key == key_code):
                input_action = action

        # pass action to behaviors
        for behavior in self.behaviors:
            behavior(self.game, input_action)
