from .intelligent_agent import IntelligentAgent
from .monster_agent import MonsterAgent

# Gets the class name of the object
# TODO put into a util script
def get_name(cls):
    return cls.__name__

entities = {
    get_name(IntelligentAgent): IntelligentAgent,
    get_name(MonsterAgent): MonsterAgent
}
