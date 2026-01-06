# Tile Mechanics
- FLOOR: Standard traversable ground.
- WALL: Impassable structural obstacle.
- MART_SHELF: Impassable shop display in Poké Marts.
- FLOOR_UP_WALL: Impassable vertical ledge face (cannot be jumped up).
- LEDGE_HOP_DOWN: One-way jumpable ledge (jump down to bypass obstacles).
- LEDGE_HOP_LEFT: One-way jumpable ledge (jump left to bypass obstacles).
- PIT: Impassable; warps the player to the floor below.
- LADDER: Warp between different floors of a building or cave.
- BOULDER: Movable object requiring Strength (HM04) to push.
- LAVA: Impassable hazard with WALL collision.
- WATER: Traversable surface requiring Surf (HM03) to cross.
- CAVE: Warp entrance leading to an interior map.
- TALL_GRASS: Reachable area where wild Pokémon encounters are triggered.

# Strategy: Final Badge
- Primary Goal: Acquire the Rising Badge from Gym Leader Clair in Blackthorn City.
- Training Plan: Grind Xenon (Haunter) and Kimchi (Gloom) to Lv30+ on Route 45 to prepare for Kingdra.
- Method: Switch-training. Lead with the trainee, then immediately switch to a high-level Pokémon (Calcifer Lv47 or Gneiss Lv45) to finish the battle.
- Current Status: Calcifer (Lv47) is the primary finisher. Gneiss (Lv45) is low on PP and HP.
- Logistics: Battle all trainers on Route 45 to earn money for additional Revives and Hyper Potions.

# Kingdra Analysis (Gym Leader Clair)
- Type: Water/Dragon.
- Defensive Matchups:
  - Neutral: Electric, Grass, Ice, Ground, Rock, Normal.
  - Resists: Fire (1/4x), Water (1/4x).
  - Weakness: Dragon.
- Observed Moves: Smokescreen, Dragonbreath, Surf.

# Training Log
- Turn 30372: Whited out against Gym Leader Clair.
- Turn 30412: [2025-12-29 00:54 AM] Started grinding session on Route 45.
- Milestone: Xenon reached Lv24 (Turn 30562).
- Milestone: Xenon reached Lv25 and evolved into HAUNTER (Turn 30625).
- Turn 30649: Defeated wild Gligar (Lv24). Yielded 370 EXP (185 to Xenon).
- Turn 30655: Defeated Hiker Parry (Onix Lv29). Received ¥1856. Xenon reached EXP: 12653.

# General Lessons
- Pathfinding: Route 45 is divided into vertical "lanes" by one-way ledges (LEDGE_HOP_DOWN, LEDGE_HOP_LEFT). Once a ledge is jumped, you cannot return north/east without circling back from the map entrance.
- NPC Navigation: If an NPC blocks a path, look for detours. Paths are often wider than one tile.
- Battle: Wild Pokémon on Route 45 (Graveler, Geodude) yield high EXP but use Selfdestruct (Normal) or Magnitude (Ground).
- Strategy Insight: Xenon (Haunter) is immune to Selfdestruct (Normal-type).
- Type Matchups: Normal moves are 0.5x effective against Rock. Ground moves are super effective against Fire. Rock/Ground types are immune to Electric (Thunderpunch).
- Turn 30674: Battling Cooltrainer Kelly (Marill Lv27). Strategy: Switch-train Xenon with Calcifer. Calcifer is using Thunderpunch.
- Turn 30679: Kelly's Marill fainted. Xenon/Calcifer gained 166 EXP. Kelly sent out Wartortle (Lv24). Strategy: Use Thunderpunch.
- Turn 30682: Kelly's first Wartortle fainted. Calcifer gained 735 EXP. Kelly sent out her second Wartortle (Lv24). Strategy: Use Thunderpunch.
- Turn 30684: Defeated Cooltrainer Kelly (Marill Lv27, Wartortle Lv24 x2). Received ¥2304. Xenon reached EXP: 12819. Strategy: Continuing south on Route 45.