from .controllable_entity import ControllableEntity
from .turn_based_player import TurnBasedPlayer

def get_name(cls):
    return cls.__name__

entities = {
    get_name(ControllableEntity): ControllableEntity,
    get_name(TurnBasedPlayer): TurnBasedPlayer
}
