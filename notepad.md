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
    - (3, 8): Interaction failed (Turn 40013, 40015). Itemfinder: "Nope!".
    - (4, 8): Interaction failed (Turn 40019). Itemfinder: "Nope!".
    - (3, 9): Interaction failed (Turn 40017).
    - (4, 9): Interaction failed (Turn 40018).
    - (4, 7): Itemfinder: "Ping" (Turn 39988).
    - (3, 7): Itemfinder: "Ping" (Turn 39534).
    - (4, 6): Itemfinder: "Nope!" (Turn 40006).
- **Hypothesis (Turn 40030):** The Machine Part is in the northern part of the pool, likely at (3, 6), (5, 6), or (3, 5). The Itemfinder pings at (3, 7) and (4, 7) suggest it is within 4 tiles of the center walkway.
- **Plan (Turn 40030):**
    1. Surf from (3, 7) to (3, 6).
    2. Interact with (3, 6).
    3. If not found, use Itemfinder at (3, 6) to re-triangulate.

## Lessons Learned
- **Itemfinder (Crystal):** "Nope!" means no item is within search range (~4 tiles). A ping means an item is within range. It does NOT mean you are standing on it.
- **Menu Mechanic:** Overworld menu loops; cursor remembers last position.
- **Gym Navigation:** BFS on Map Events is optimal for warp mazes.

## Saffron City Interests
- **Mr. Psychic:** Obtained TM29 Psychic (Turn 39946).
- **Magnet Train:** Inactive until Power Plant fixed. Requires PASS.