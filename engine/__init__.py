from . import gameobjects
from . import pickups
from . import agents
from . import game
from . import hostiles
from . import ui
from . import renderer
from . import mapping
from . import controllable_entity
from . import combat
from . import items
from . import inventory
from . import floors
from . import menu

entity_dicts = [
    gameobjects.entities,
    agents.entities,
    controllable_entity.entities,
    mapping.entities,
    pickups.entities
]

# TODO merge all the entities into hashtable
entities = {

}

for entity_dict in entity_dicts:
    for (k, v) in entity_dict.items():
        entities[k] = v
