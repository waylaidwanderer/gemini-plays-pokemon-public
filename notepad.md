# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- WARP_CARPET: Step on or walk off map edge to transition.
- WARP_PANEL: Teleports between rooms.
- COUNTER: Impassable Wall. Interact from adjacent tile.
- FLOOR_UP_WALL: One-way ledge (North to South). Wall from South to North.
- CAVE_LEDGE: Rock Tunnel B1F Row 26 FLOOR_UP_WALL tiles act as walls from the North.

## Kanto Strategy
- **Primary Goal: Complete Kanto Region Journey.**
- **Current Objective: Resolve Power Plant crisis.**
  - Strategy: Retrieve the stolen Machine Part to restore power.
  - Plan: Find Mr. Fuji (Lavender) -> Route 10 -> Power Plant -> Cerulean City (Find thief) -> Cerulean Gym (Retrieve Machine Part).

## PC Storage (Box 1)
1. GLAIVE (Lv14), 2. SELKIE (Lv24), 3. DELTA (MANTINE) Lv20, 4. RANGOON (KRABBY) Lv22, 5. NOMURA (TENTACOOL) Lv17, 6. Ravioli (Lv10), 7. Ouroboros (DRATINI) Lv15

## Rock Tunnel Navigation
- Strategy: Use Flash (KIMCHI). Head north for Power Plant exit.
- Connections: 1F (27, 13) <-> B1F (3, 3); 1F (15, 9) <-> B1F (17, 9); 1F (5, 3) <-> B1F (23, 3); 1F (27, 3) <-> B1F (25, 23).
- B1F Landmarks: (7, 25) IRON picked up.

## Observed Pokemon (Kanto)
- Rock Tunnel: Geodude (Lv11-14), Zubat (Lv12), Haunter (Lv17), Onix (Lv16).

## Power Plant Investigation
- **Start Turn:** 39084
- **Status:** Talked to Manager and Officer. A shady character was seen loitering in Cerulean City.
- **Officer (4, 14):** Confirmed a thief broke in; latest report points to Cerulean City.
- **Gym Guide (6, 11):** Info on Magnet Train power.
- **Gym Guide (2, 9):** Info on stolen part.
- **Gym Guide (5, 5):** Offered to trade MAGNETON for DUGTRIO. (Declined).
- **Officer (9, 3):** Guarding the generator room.
- **Manager (14, 10):** Furious about the stolen generator part; needs the Machine Part returned.
- **Next Step:** Head to Cerulean City to find the thief.

## Lessons Learned
- NPCs act as walls and must be navigated around.
- "find_path_v3_fixed" is more reliable than manual directional inputs for navigating around obstacles.
## Route 9 Exploration
- Goal: Find path to Cerulean City (West).
- Observation: Blocked at X=34 in Row 8. Vertical walls at X=30, 32, 33, 35, 41, 55.
- Hypothesis 1: Path is through Row 14 (South). Reachable via Row 13 jumps at X=48.
- Hypothesis 2: Path is through Row 0 (North). Reachable via Surf to Row 1 at X=39/40.
- Hypothesis 3: Path involves Surfing West from X=42 in Row 2/3.
- Plan: Head to (44, 14) to explore the southern path first.