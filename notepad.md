## Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- COUNTER: Impassable Wall. Interact from adjacent tile.
- STAIRCASE: Warp tile that transitions between floors.
- WARP_PANEL: Teleports player between rooms. Interaction is immediate upon entry.

## Core Principles & Strategy
- **Immediate Execution:** Tasks are performed the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Falsification:** Actively try to disprove hypotheses.
- **Root Assumption Audit:** If a complex strategy fails, re-verify the base assumption.

## Battle Mechanics (Verified)
- Status Moves: Misses are reported as "The attack missed!".
- Night Shade: Deals fixed damage equal to user level.
- Type Effectiveness (Psychic): Weak to Bug, Ghost, Dark.
- Type Effectiveness (Ghost): Weak to Ghost, Dark. Immune to Normal, Fighting.

## PC Storage (Box 1)
- SPINARAK (13), SCYTHER (14), SEEL (24), MANTINE (20), KRABBY (22), TENTACOOL (17), KRABBY (10), DRATINI (15)

## Movesets (HM Users)
- KIMCHI (GLOOM): FLASH, CUT
- GNEISS (GRAVELER): STRENGTH
- LAPIS (POLIWAG): SURF, WHIRLPOOL, WATERFALL
- ICARUS (PIDGEOTTO): FLY

## Machine Part Investigation
- **Start Turn:** 39950
- **Foundational Hint:** Rocket Grunt: "I hid it in the water in the center of the Gym."
- **Search Log:**
    - (3, 8), (4, 8), (3, 9), (4, 9): "Nope!" (Out of range).
    - (4, 7), (3, 7): "Ping" (In range).
    - (4, 6), (5, 6): "Nope!" (Out of range).
- **Triangulation (Turn 40041):** 
    - dist(item, (4, 7)) <= 5
    - dist(item, (3, 7)) <= 5
    - dist(item, (3, 8)) > 5
    - dist(item, (4, 6)) > 5
- **Candidate Found:** (8, 7) WATER.
    - dist((8, 7), (4, 7)) = 4 (In range)
    - dist((8, 7), (3, 7)) = 5 (In range)
    - dist((8, 7), (3, 8)) = 6 (Out of range)
    - dist((8, 7), (4, 6)) = 5 (Borderline - if range is exactly 4, this fits perfectly).
- **Plan:**
    1. Move to (7, 7) via (6, 6) and (7, 6).
    2. Use Itemfinder at (7, 7).
    3. If ping, interact with (8, 7).

## Lessons Learned
- **Itemfinder (Crystal):** "Nope!" means no item is within search range (~4 tiles). A ping means an item is within range.
- **Gym Clue:** "Center of the Gym" might refer to the center of the northern pool area or a specific decorative center, not necessarily the inner pool.

## Saffron City Interests
- **Mr. Psychic:** Obtained TM29 Psychic (Turn 39946).
- **Magnet Train:** Inactive until Power Plant fixed. Requires PASS.