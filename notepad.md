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
- **Root Hypothesis:** The Machine Part is a hidden item on a WATER tile in the inner pool: (3,8), (3,9), (4,8), (4,9).
- **Secondary Hypothesis:** Itemfinder in Crystal pings within 4 tiles but says "Nope!" if standing directly on the hidden item.
- **Search Log:**
    - (3, 8): Itemfinder "Nope!" (Turn 39976). Interaction pending.
    - (4, 7): Itemfinder "Ping" (Turn 39988).
    - (4, 6): Itemfinder "Nope!" (Turn 40006). Interaction pending.
    - (4, 8): Itemfinder "Nope!" (Turn 40008). Interaction pending.
    - (3, 9): Current location. Interaction pending.

## Completed Objectives
- **Saffron Gym Challenge:** Marsh Badge obtained (Turn 39878).
- **Power Plant Conflict:** Manager informed of theft. Rocket Grunt chased from Cerulean Gym to Route 24 and defeated.

## Lessons Learned
- **Itemfinder (Crystal):** Returns "Nope!" if the player is standing directly on the item.
- **Menu Mechanic:** Overworld menu loops; cursor remembers last position.
- **Gym Navigation:** BFS on Map Events is optimal for warp mazes.

## Saffron City Interests
- **Mr. Psychic:** Obtained TM29 Psychic (Turn 39946).
- **Magnet Train:** Inactive until Power Plant fixed. Requires PASS.