# Verified Game Systems
- Start Menu: 1.POKEDEX, 2.POKEMON, 3.PACK, 4.POKEGEAR, 5.GEM, 6.SAVE, 7.OPTION, 8.EXIT.
- Fly Map: Cursor starts at New Bark Town (5, 4).
- Johto Fly Grid (Verified):
  - Cherrygrove is (Left) from New Bark.
  - Goldenrod is (Up x3, Right) from Cherrygrove.
  - Ecruteak is (Up) from Goldenrod.

# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable, triggers wild encounters.
- HEADBUTT_TREE: Impassable, interact with Headbutt.
- LEDGE_HOP_DOWN: One-way (Down). Traversable from Top to Bottom. Impassable from Bottom to Top.

# Strategy: Ecruteak Shuffle
- Goal: Force first encounter with Entei/Raikou (Lv 40).
- Location: Ecruteak City <-> Route 37 (Left side).
- Repel Trick: Lead Lv 19 (ICARUS) + Super Repel.
- Method:
  1. Transition from Ecruteak to Route 37.
  2. Pace 4 steps in grass at (7, 2).
  3. Transition back to Ecruteak.
  4. Repeat.

# Tracking: Session 4
- Start: Turn 45281.
- Completed Cycles: 34.
- Repel 2: Active (Applied Turn 45627). (~120 steps used).
- Current Status: Starting Cycle 35. Moving to Route 37 grass.
- Lesson: Limit menu_navigator_v2 sequences to 1-3 buttons.

# Quest Log
- Dana's Gift: Route 38 (Waiting).
- Yanma Swarm: Route 35 (Active).