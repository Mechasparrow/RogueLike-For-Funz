# Basic Agent for monsters
# monster_agent.py
# Author: Michael Navazhylau

# import libs
import tcod

# extends from intelligent agent as base
from .intelligent_agent import IntelligentAgent

# polyfill
import sys
sys.path.append("..")

# utilize some game functions
from engine.game import *

# Monster Agent Class Def
# extends from Intelligent Agent
class MonsterAgent(IntelligentAgent):

    def __init__(self, x, y, name, chr, color, combat_behavior = None, game = None, ai_target = None):
        IntelligentAgent.__init__(self, x, y, name, chr, color, combat_behavior = combat_behavior, game = game)

        # takes in ai target to know what to chase
        self.ai_target = ai_target

    # convert gameobject to a monster agent
    def from_gameobject(gameobject, combat_behavior = None):
        gameobject_monster_agent = MonsterAgent(gameobject.x, gameobject.y, gameobject.name, gameobject.chr, gameobject.color, combat_behavior = combat_behavior, game = gameobject.game)
        return gameobject_monster_agent

    # pathfinding for monster + attacking TODO
    def ai_behavior(self):

        # alias
        target = self.ai_target
        combat_behavior = self.combat_behavior

        # FIXME
        fov_map = self.game.get_current_floor().game_map.fov_map

        # Only trigger ai if in FOV
        if (fov_map.fov[self.y][self.x] == False):
            return

        # Dont do anything if no target
        if (target == None or self.combat_behavior.dead):
            return

        # Compute a new path with no diagonals
        path = tcod.path_new_using_map(fov_map, dcost = 0)
        tcod.path_compute(path, self.x, self.y, target.x, target.y)

        # generate the next x and next y on the path recompute if necessary
        (next_x, next_y) = tcod.path_walk(path, recompute = True)

        # Only move if
        if (next_x and next_y):
            # get the movement values
            dx = next_x - self.x
            dy = next_y - self.y

            # predicted position based off the path dx + dy
            predicted_pos_x = self.x + dx
            predicted_pos_y = self.y + dy

            # check if there are any gameobjects at the predicted FIXME
            gameobjects_at_next_position = find_gameobjects_at_point(self.game.get_current_floor(), predicted_pos_x, predicted_pos_y)

            # TODO ignore other monsters
            # dont move if a gameobject is at the next position
            if (len(gameobjects_at_next_position) > 0):
                # if a gameobject does exist at the next possition and happens to be one that can be attacked
                # attack it
                for gameobject in gameobjects_at_next_position:
                    if (gameobject == target):
                        # Dont move there instead attack
                        if (target.combat_behavior):
                            target_behavior = target.combat_behavior
                            self.combat_behavior.attack(target_behavior)
            else:
                # if there are no gameobjects at the next position, go ahead and move
                self.move(dx, dy)
