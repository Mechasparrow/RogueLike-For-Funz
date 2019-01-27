from .pickup import BasePickUp
from .xp_pickup import XPDrop
from .health_pickup import HealthDrop

def get_name(cls):
    return cls.__name__

entities = {
    get_name(BasePickUp): BasePickUp,
    get_name(XPDrop): XPDrop,
    get_name(HealthDrop): HealthDrop
}
