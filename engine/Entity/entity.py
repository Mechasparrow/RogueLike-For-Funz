import tcod
from ..gameobject import GameObject

class Entity:

    def __init__(self, name, gameobject, combatBehavior = None, game = None):
        self.name = name
        self.game = game

        # Add the gameobject
        if (gameobject):
            self.gameobject = gameobject
        else:
            self.gameobject = Entity.base_gameobject(self.name, (255, 255, 255))

    def base_gameobject(name, color):
        return GameObject(0, 0, name, "X", color)
