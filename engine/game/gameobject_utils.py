def add_gameobject_to_game(game,gb):
    game.objects.append(gb)

# returns a list of game objects by their name
def find_gameobjects_by_name(game, name):

    # filter function by gameobject name
    def filter_by_name(object):
        if (object.name == name):
            return True
        else:
            return False

    #return the filtered game objects
    filtered_gameobjects = list(filter(filter_by_name, game.objects))

    return filtered_gameobjects

# return a list of game objects at a specific point
def find_gameobjects_at_point(game,x, y):

    # filter function by object position
    def filter_by_point(object):
        if (object.x == x and object.y == y):
            return True
        else:
            return False

    filtered_gameobjects = list(filter(filter_by_point, game.objects))
    return filtered_gameobjects
