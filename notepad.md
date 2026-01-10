# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- FLOOR_UP_WALL: Acts as a WALL from the North (cannot be jumped). Verified at (20, 16), (11, 16), (12, 16).
- COUNTER: Impassable Wall. Interact from adjacent tile.
- CAVE_LEDGE: Rock Tunnel B1F Row 26 FLOOR_UP_WALL tiles act as walls from the North.

## Battle Mechanics (Hypotheses)
- Hypothesis: Haunter (XENON) lacks Levitate in this game (Gen 2) and is vulnerable to Ground moves. (Verification needed).

## Kanto Strategy
- **Primary Goal: Complete Kanto Region Journey.**
- **Current Objective: Resolve Power Plant crisis.**
  - Strategy: Retrieve the stolen Machine Part to restore power.
  - Plan: Find Mr. Fuji (Lavender) -> Route 10 -> Power Plant -> Cerulean City (Find thief) -> Cerulean Gym (Retrieve Machine Part).

## PC Storage (Box 1)
1. GLAIVE (Lv14), 2. SELKIE (Lv24), 3. DELTA (MANTINE) Lv20, 4. RANGOON (KRABBY) Lv22, 5. NOMURA (TENTACOOL) Lv17, 6. Ravioli (Lv10), 7. Ouroboros (DRATINI) Lv15

## Rock Tunnel Navigation
- Connections: 1F (27, 13) <-> B1F (3, 3); 1F (15, 9) <-> B1F (17, 9); 1F (5, 3) <-> B1F (23, 3); 1F (27, 3) <-> B1F (25, 23).

## Power Plant Investigation
- **Start Turn:** 39084
- **Status:** Talked to Manager and Officer. A shady character was seen loitering in Cerulean City.
- **Next Step:** Head to Cerulean City to find the thief.

## Route 9 Exploration
- **Start Turn:** 39167
- **Goal:** Find path to Cerulean City (West).
- **Status:**
  - Picnicker Heidi (41, 8): Defeated.
  - Hiker Sidney (39, 15): Defeated.
  - Camper Dean (19, 11): Defeated.
  - Picnicker Edna (12, 15): Defeated.
  - Camper Sid (13, 4): Defeated.
- **Observation:** Southern and middle lanes are blocked by walls/ledges. Access the northern lane (Rows 0-4) via the gap at (15, 5). The path is (15, 6) -> (15, 5) -> (15, 4).
- **Time Tracking:** Started Route 9 Exploration at Turn 39167. (Currently Turn 39319).

## Lessons Learned
- NPCs act as walls and must be navigated around.
- "find_path_v3_fixed" is more reliable than manual directional inputs for navigating around obstacles.
- Sand-Attack lowers accuracy; fixed-damage moves like Night Shade are good for consistency.
- FLOOR_UP_WALL is not jumpable from the North.
- Always check for gaps in ledges for passage.
- (15, 5) is a critical gap to reach the northern lane of Route 9.