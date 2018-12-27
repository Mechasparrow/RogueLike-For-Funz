# Purpose: Turn Handler for the Game in turn based games
# gameobject_utils.py
# Author: Michael Navazhylau

# Add a gameobject to the game
def add_gameobject_to_floor(floor,gb, bottom = False):
    floor.objects.append(gb)

# remove a gameobject from the game
def remove_gameobject_from_floor(floor, gb):
    floor.objects.remove(gb)

# returns a list of game objects by their name
def find_gameobjects_by_name(floor, name):

    # filter function by gameobject name
    def filter_by_name(object):
        if (object.name == name):
            return True
        else:
            return False

    #return the filtered game objects
    filtered_gameobjects = list(filter(filter_by_name, floor.objects))

    return filtered_gameobjects

# return a list of game objects at a specific point
def find_gameobjects_at_point(floor,x, y):

    # filter function by object position
    def filter_by_point(object):
        if (object.x == x and object.y == y):
            return True
        else:
            return False

    filtered_gameobjects = list(filter(filter_by_point, floor.objects))
    return filtered_gameobjects

# returns a boolean as to whether gameobjects exist a point on the map
def gameobjects_exist_at_point(floor, x, y):

    gameobjects = find_gameobjects_at_point(floor, x, y)
    return len(gameobjects) > 0
