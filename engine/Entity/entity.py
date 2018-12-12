import tcod
from ..gameobject import GameObject

class Entity:

    def __init__(self, name, gameobject, combatBehavior = None, game = None):
        self.name = name
        self.game = game
        self.gameobject = gameobject

    def simple_entity():

        pass
