from .dungeon import Dungeon
from .dungeon_spawn_stats import DungeonSpawnStats
from .game_map import GameMap
from .rect import Rect
from .room import Room
from .tile import Tile
from .tunnel import Tunnel
from .stairs import Stairs
from .chest import Chest

def get_name(cls):
    return cls.__name__

entities = {
    get_name(Stairs): Stairs,
    get_name(Chest): Chest
}
