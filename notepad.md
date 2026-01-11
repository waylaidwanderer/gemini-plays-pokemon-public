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
    - (3, 8), (4, 8), (3, 9), (4, 9): Interaction failed. Itemfinder: "Nope!".
    - (4, 7), (3, 7): Itemfinder: "Ping" (In range).
    - (4, 6): Interaction failed (Turn 40047). Itemfinder: "Nope!" (Turn 40006).
    - (3, 6): Untested.
- **Triangulation (Turn 40047):** 
    - The item is NOT at (4, 6).
    - Since (3, 7) and (4, 7) ping, and (3, 8), (4, 8), and (4, 6) are "Nope", the item must be distance > 4 from (3, 8), (4, 8), and (4, 6) but within distance 4 of (3, 7) and (4, 7).
    - This suggests the item is at (2, 7) [Floor], (5, 7) [Floor], or in the northern pool at (2, 6), (3, 5), (4, 5), or (5, 5).
- **Plan (Turn 40047):**
    1. Move Up to (4, 5).
    2. Move Left to (3, 5) and (2, 5).
    3. Use Itemfinder at (2, 5) and (4, 5).
    4. Interact with (4, 5) and (3, 5).

## Lessons Learned
- **Itemfinder (Crystal):** "Nope!" means no item is within search range (~4 tiles). A ping means an item is within range.
- **Gym Clue:** "Center of the Gym" might refer to the center of the northern pool area or a specific decorative center, not necessarily the inner pool.

## Saffron City Interests
- **Mr. Psychic:** Obtained TM29 Psychic (Turn 39946).
- **Magnet Train:** Inactive until Power Plant fixed. Requires PASS.