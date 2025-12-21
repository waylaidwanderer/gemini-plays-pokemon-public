# Tile Mechanics
- FLOOR:
    - Individual: Traversable. Standard movement.
    - Relational: Connects to other walkable tiles and warps.
    - Mechanics: None.
- WALL:
    - Individual: Impassable.
    - Relational: Blocks movement.
    - Mechanics: None.
- WATER:
    - Individual: Traversable only with Surf (HM03) and Fog Badge.
    - Relational: Must be entered from an adjacent land tile while facing the water.
    - Mechanics: Triggers wild water encounters.
- TALL_GRASS:
    - Individual: Traversable. Standard movement.
    - Relational: Connects to other walkable tiles.
    - Mechanics: Triggers wild land encounters.
- MART_SHELF:
    - Individual: Impassable.
    - Relational: Blocks movement.
    - Mechanics: None.
- COUNTER:
    - Individual: Impassable.
    - Relational: Interacting from an adjacent tile allows talking to NPCs behind it (e.g., Nurse Joy, Mart Clerks).
    - Mechanics: Blocks movement but allows interaction.
- WARP_CARPET_DOWN / WARP_CARPET:
    - Individual: Traversable.
    - Relational: Moving onto this tile triggers a map transition (Warp).
    - Mechanics: Entry point determines arrival location on destination map.
- LADDER / STAIRS / DOOR:
    - Individual: Traversable.
    - Relational: Moving onto the tile triggers a map transition.
    - Mechanics: Map transition.
- HEADBUTT_TREE:
    - Individual: Impassable.
    - Relational: Blocks movement.
    - Mechanics: Can be interacted with using Headbutt to trigger encounters.
- CUT_TREE:
    - Individual: Impassable.
    - Relational: Blocks movement.
    - Mechanics: Can be removed using Cut (HM01) and Hive Badge.
- PC:
    - Individual: Impassable.
    - Relational: Interacting from the tile below (facing UP) allows access to the Pokemon Storage System.
    - Mechanics: Accesses PC.

# KIMCHI Training (Turn #7531)
- Target: Lv21 (Evolution to Gloom).
- Current Level: 20.
- Strategy: Lead with KIMCHI on Route 43/Lake of Rage. Use Sleep Powder and Cut/Absorb.

# Strategy: Lake of Rage Investigation
- Path:
    1. Exit Mahogany Town via North Gatehouse (Route 43 entrance).
    2. Follow Route 43 North.
    3. Lead with KIMCHI (Lv20 Oddish). Use Sleep Powder to stall and Absorb/Cut to deal damage and gain EXP.
    4. If wild encounters are too frequent or high-level, switch to Typhlosion (Calcifer) or Graveler (GNEISS) to clear them.
    5. Upon reaching Lake of Rage, explore the shoreline and use Surf to find the "Red Gyarados".
- Contingencies:
    - If Route 43 is blocked by Team Rocket, look for a side path or a specific NPC (like Lance) to clear the way.
    - If the "rampage" involves a battle, prepare GNEISS for Rock-type advantages against Flying/Water.

# General Mechanics & Tools
- Battle: Sweet Scent lowers opponent's evasion (counters Minimize). Karate Chop is Fighting-type.
- Tool: find_path_v2 (v7323) handles trees and water-to-land navigation.

# Type Matchups (Observed)
- Ground vs Water/Poison: Super Effective.
- Rock vs Water/Flying: Super Effective.
- Fighting vs Poison: Not Very Effective.
- Fighting vs Rock/Ground: Super Effective.
- Water vs Fire: Super Effective.
- Water vs Rock/Ground: 4x Super Effective.
- Grass vs Water/Fighting: Super Effective.
- Fighting vs Grass/Poison: Not Very Effective (e.g., Double Kick vs Oddish).

# PC Storage (Box 1)
- ROCKY (ONIX): Lv6, EGG (CLEFFA): Lv5, XFDW (MEOWTH): Lv16, FRITTATA (TOGEPI): Lv5, SHUCKIE (SHUCKLE): Lv15.

# Battle Strategies
- Fisher Tully (Route 42): Qwilfish (Water/Poison).
- Pokemaniac Shane (Route 42): Nidorina (Poison), Nidorino (Poison).
- Hiker Benjamin (Route 42): Diglett (Ground), Dugtrio (Ground), Geodude (Rock/Ground).

# Defeated Trainers
- Fisher Tully (Route 42) at (40, 10).
- Pokemaniac Shane (Route 42) at (47, 8).
- Hiker Benjamin (Route 42) at (49, 9).

# Route 42 Discoveries
- Sign at (45, 9): MT.MORTAR WATERFALL CAVE INSIDE.
- Sign at (54, 8): ROUTE 42 ECRUTEAK CITY - MAHOGANY TOWN.
- Arnie (Bug Catcher) mentioned rare Ditto on Route 35.

# Mahogany Town Discoveries
- Arrived at (0, 7) from Route 42.
- Sign at (1, 5): Welcome to the Home of the Ninja (Mahogany Town).
- Gramps at (5, 9).
- Mahogany Mart (11, 7): NPCs mention Gyarados experiments. Suspicious tile at (7, 3) currently inactive.
- Gym (6, 13): Blocked by Fisher at (6, 14).

# Mahogany Pokemon Center Dialogue
- Pokefan M at (8, 1) saw "men in black" at Lake of Rage. Confirms Team Rocket involvement.
- Youngster at (1, 3) stops evolution to learn moves faster.
- Cooltrainer F at (2, 3) mentions evolved Pokemon learn moves more slowly.