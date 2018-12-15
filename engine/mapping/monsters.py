# polyfill
import sys
sys.path.append("..")

from engine.hostiles import Monster

goblin = Monster("Goblin", "G")
druid = Monster("Druid", "D")
serpent = Monster("Serpent", "S")

monsters = {
    "goblin": goblin,
    "druid": druid,
    "serpent": serpent
}
