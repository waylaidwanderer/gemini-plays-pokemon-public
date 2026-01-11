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
- **Triangulation (Turn 40039):** Since it pings at (3, 7) but is "Nope!" at (3, 8) and (4, 6), the item must be North of (3, 7) but West of (4, 6). 
- **Target Area:** Northern pool, West side. Candidates: (1, 6), (2, 6), (1, 5), (2, 5), (1, 4), (1, 3), (2, 3).
- **Plan:**
    1. Use Itemfinder at (5, 6) to confirm out-of-range status.
    2. Move to (3, 7) and confirm ping.
    3. Move to (2, 6) and check.
    4. Move to (1, 6) and check.

## Lessons Learned
- **Itemfinder (Crystal):** "Nope!" means no item is within search range (~4 tiles). A ping means an item is within range.
- **Gym Clue:** "Center of the Gym" might refer to the center of the northern pool area or a specific decorative center, not necessarily the inner pool.

## Saffron City Interests
- **Mr. Psychic:** Obtained TM29 Psychic (Turn 39946).
- **Magnet Train:** Inactive until Power Plant fixed. Requires PASS.