from .entity import Entity
from .gameobject import GameObject
from .dead_body import DeadBodyEntity

def get_name(cls):
    return cls.__name__

entities = {
    get_name(Entity): Entity,
    get_name(GameObject): GameObject,
    get_name(DeadBodyEntity): DeadBodyEntity
}
