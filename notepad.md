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
    - (4, 6): Itemfinder: "Nope!" (Turn 40006). Interaction pending.
    - (3, 6): Untested.
- **Triangulation (Turn 40044):** 
    - The item is likely at (4, 6) if the "Nope! when standing on it" hypothesis is correct.
    - If not at (4, 6), it must be a tile that pings at (3, 7) and (4, 7) but is out of range of (3, 8), (4, 8), and (4, 6). This is mathematically difficult with a standard range, suggesting the "standing on it" rule or a very specific range.
- **Plan (Turn 40044):**
    1. Close the Pokemon summary screen (press B multiple times).
    2. Navigate to (4, 6) in the water.
    3. Interact (A button) with (4, 6).
    4. If not found, check (3, 6) and (1, 7).

## Lessons Learned
- **Itemfinder (Crystal):** "Nope!" means no item is within search range (~4 tiles). A ping means an item is within range.
- **Gym Clue:** "Center of the Gym" might refer to the center of the northern pool area or a specific decorative center, not necessarily the inner pool.

## Saffron City Interests
- **Mr. Psychic:** Obtained TM29 Psychic (Turn 39946).
- **Magnet Train:** Inactive until Power Plant fixed. Requires PASS.