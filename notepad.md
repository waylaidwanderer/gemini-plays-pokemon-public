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
- LEDGE_HOP_RIGHT: One-way (Right). Traversable from Left to Right. Impassable from Right to Left.
- WATER: Traversable with HM03 Surf.
- WARP_CARPET_LEFT/RIGHT: Warp triggers.
- DOOR: Warp trigger.

# Strategy: Ecruteak Shuffle
- Goal: Force first encounter with Entei/Raikou (Lv 40).
- Location: Ecruteak City <-> Route 37 (Left side).
- Repel Trick: Lead Lv 19 (ICARUS) + Super Repel.
- Method:
  1. Transition from Ecruteak to Route 37.
  2. Pace 4 steps in grass at (7, 2).
  3. Transition back to Ecruteak.
  4. Repeat.

# Tile Mechanics
- FLOOR: Traversable. Verified Turn 45281.
- WALL: Impassable. Verified Turn 45281.
- TALL_GRASS: Traversable, triggers wild encounters. Verified Turn 45281.
- HEADBUTT_TREE: Impassable. Verified Turn 45281.
- LEDGE_HOP_DOWN: One-way (Down). Verified Turn 45281.
- LEDGE_HOP_RIGHT: One-way (Right). Verified Turn 45281.
- WATER: Traversable with HM03 Surf. Verified Turn 45281.

# Tracking: Roamer Hunt
- Shuffle Start Turn: 45281.
- Completed Cycles: 78.
- Repel 5: Applied Turn 45841. (~199 steps used).
- Trapper Strategy (for 2nd roamer):
  - Option A: Train Spinarak (AAAAAAAAAA, Lv 13) in PC. It has Spider Web.
  - Option B: Xenon (Haunter, Lv 44) does NOT have Mean Look. Gastly learns it at Lv 13; Xenon likely missed it.
  - Decision: Stick to Master Ball for the first one, then evaluate Spinarak.
- Strategy Note: Statistically, Entei/Raikou will appear within ~50-100 cycles of this shuffle. We are at 78. Continuing until encounter or ~100 cycles before reassessing.
- Lesson: Trust turn history logs for bookkeeping to avoid 'time-slipping' errors.

# Quest Log
- Dana's Gift: Route 38 (Waiting).
- Yanma Swarm: Route 35 (Active).

# Decisive Action Phase: Roamer Hunt
- Commenced Turn: 45872.
- Strategy: Continuous Ecruteak Shuffle using `execute_shuffle_cycle`.
- Goal: Maintain loop until encounter or Repel depletion.
- Resource: 58 Super Repels remaining.
- Trapper: Master Ball reserved for first encounter.