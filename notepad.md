# KIMCHI Training (Turn #7531)
- Target: Lv21 (Evolution to Gloom).
- Current Level: 20.
- Strategy: Lead with KIMCHI on Route 43/Lake of Rage. Use Sleep Powder and Cut/Absorb.

# Tile Mechanics
- FLOOR: Traversable. Standard movement.
- WALL: Impassable.
- WATER: Traversable only with Surf (HM03) and Fog Badge. Must be entered from an adjacent land tile while facing the water.
- TALL_GRASS: Traversable. Standard movement. Triggers wild encounters.
- MART_SHELF: Impassable.
- COUNTER: Impassable. Interacting from an adjacent tile allows talking to NPCs behind it.
- WARP_CARPET_DOWN / WARP_CARPET: Traversable. Triggers map transition.
- LADDER / STAIRS / DOOR: Traversable. Triggers map transition.
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt.
- CUT_TREE: Impassable. Can be removed using Cut (HM01) and Hive Badge.
- PC: Impassable. Interacting from below (facing UP) allows access.

# Strategy: Lake of Rage Investigation
- Path: Follow Route 43 North.
- Method: Lead with KIMCHI (Lv20 Oddish). Use Sleep Powder to stall and Absorb/Cut to deal damage.
- Goal: Locate the source of the "rampage" (Red Gyarados).
- Contingencies: If blocked, search for Lance or explore water with Surf.

# General Mechanics & Tools
- Battle: Sweet Scent lowers opponent's evasion. Karate Chop is Fighting-type.
- Tool: find_path_v2 (v7323) handles trees and water-to-land navigation. Note: This tool may fail when targeting Warp tiles directly; target an adjacent tile instead.

# Type Matchups (Observed)
- Ground vs Water/Poison: Super Effective.
- Rock vs Water/Flying: Super Effective.
- Fighting vs Poison: Not Very Effective.
- Fighting vs Rock/Ground: Super Effective.
- Water vs Fire: Super Effective.
- Water vs Rock/Ground: 4x Super Effective.
- Grass vs Water/Fighting: Super Effective.
- Fighting vs Grass/Poison: Not Very Effective.

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

# Mahogany Town Discoveries
- Welcome to the Home of the Ninja.
- Mahogany Mart (11, 7): NPCs mention Gyarados experiments. Suspicious tile at (7, 3) currently inactive.
- Gym (6, 13): Blocked by Fisher at (6, 14).

# Mahogany Pokemon Center Dialogue
- Pokefan M at (8, 1) saw "men in black" at Lake of Rage. Confirms Team Rocket involvement.
- Youngster at (1, 3) stops evolution to learn moves faster.
- Cooltrainer F at (2, 3) mentions evolved Pokemon learn moves more slowly.
- Camper Spencer (Route 43): Sandshrew (Ground), Zubat (Poison/Flying), Sandslash (Ground).