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
- **Start Turn:** 39929
- **Clue:** Rocket Grunt: "I hid it in the water in the center of the Gym."
- **Status:** Contradictory data found. Inventory contains 'PASS', suggesting quest completion. 
- **Verified Empty Tiles:** (3,8), (4,8), (3,9), (4,9), (3,3), (4,6), (5,6).
- **Itemfinder History:**
    - (3,7), (4,7): Ping (Prior to Turn 39988).
    - (4,7): Nope! (Turn 40061). 
- **Hypothesis:** The Power Plant quest is already complete. The 'Nope!' at (4,7) indicates the item is no longer there.
- **Next Step:** Verify Magnet Train status in Saffron City.

## Completed Objectives
- **Saffron Gym Challenge:** Marsh Badge obtained (Turn 39878).
- **Power Plant Conflict:** Manager informed of theft. Rocket Grunt defeated.

## Lessons Learned
- **Itemfinder (Crystal):** "Nope!" means no item is within search range. A ping means an item is within range.
- **Gym Clue:** "Center" is relative. 
- **Data Integrity:** Summary turn 39643 says problem resolved; trust this and current inventory over conflicting pings.

## Saffron City Interests
- **Mr. Psychic:** Obtained TM29 Psychic (Turn 39946).
- **Magnet Train:** Station is in Saffron City. Requires PASS and restored power.
- **Copycat:** Lives in Saffron. Reward for returning her doll is the PASS (already in inventory).