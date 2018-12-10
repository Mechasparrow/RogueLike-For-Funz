import tcod

class Entity:

    def __init__(self, name, chr, color, combatBehavior = None, game = None):
        self.name = name
        self.game = game
        
        self.gameobject = GameObject(0, 0, name, chr, color, game = game)

        pass
