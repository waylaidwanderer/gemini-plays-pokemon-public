# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal. Jump down from lower Y to higher Y. Verified on Route 6.
- WARP_CARPET: Step on or walk off map edge to transition. Verified on Route 5/27.
- WARP_PANEL: Teleports between rooms. Verified in Saffron Gym.
- COUNTER: Impassable Wall. Must interact from an adjacent tile. Verified in Centers/Radio Tower.
- FLOOR_UP_WALL: Impassable Wall when approached from below (South). Functions as a one-way ledge from North to South. Verified on Route 8.

## Kanto Strategy
- **Primary Goal: Complete Kanto Region Journey.**
- **Current Objective: Resolve Power Plant Crisis.**
  - Started Turn: 38311
  - Purpose: Unlock Magnet Train and Snorlax path.
  - Plan:
    1. Find Mr. Fuji in Lavender Town (Soul House at 13, 11).
    2. Head north to Route 10.
    3. Use Surf (LAPIS) and Flash (KIMCHI) to navigate to the Power Plant.
    4. Speak with the Manager.
    5. Retrieve the stolen Machine Part from Cerulean Gym.

## Saffron City Notes
- Silph Co: Center (16, 29).
- Pokemon Center: (9, 29).
- Magnet Train Station: (8, 3).
- Saffron Gym: (34, 3). Leader: Sabrina. Path: (1,A) (1, 5) <-> (2,B) (11, 9).

## Battle History: vs Sabrina
- Attempt 1 (Turn 38625): FAILED (White out). Espeon (Lv 46) used Psychic and Sand-Attack to sweep the team.
- Analysis: Type disadvantage (Graveler, Haunter, Gloom) and speed gap (Typhlosion) were critical. Need Dark/Bug moves or higher levels for GNEISS/Calcifer.

## PC Storage (Box 1)
1. GLAIVE (SCYTHER) Lv14
2. SELKIE (SEEL) Lv24
3. DELTA (MANTINE) Lv20
4. RANGOON (KRABBY) Lv22
5. NOMURA (TENTACOOL) Lv17
6. Ravioli (KRABBY) Lv10
7. Ouroboros (DRATINI) Lv15

## Lavender Town Notes
- (0, 8): Entrance from Route 8.
- Mart: (1, 5).
- Pokemon Center: (5, 5).
- Volunteer Pokemon House: (5, 9).
- Name Rater's House: (7, 13).
- Soul House: (13, 11).
- Radio Tower: Northeastern part of town. 1F Receptionist (6, 6), Manager (9, 1), Officer (15, 1) blocks stairs.
- House (3, 13): Lavender Speech House. Pokefan F (2, 3) is here.

## Lessons & Observations
- Root Hypothesis Check: Building labels must be verified by Map ID or NPC interaction (dialogue) before being documented as permanent markers. (Turn 38852)
- Counter/Wall Behavior: Counters act as WALL tiles and must be interacted with from an adjacent tile. Verified in Centers and Radio Tower.
- Tool Maintenance: Fixed find_path tool (v3) to handle autopress_buttons correctly by returning button strings.
- Navigation: Ledges at y=5 and y=9 are one-way (down). Path at x=19 is clear of ledges to reach the northern map boundary.

## Route 10 Progress
- Started Turn: 38868
- Goal: Reach Power Plant.
- Pokefan Robert (8, 12): DEFEATED. (Quagsire Lv 33).
- Hiker Jim (17, 3): DEFEATED. (Machamp Lv 35).

## Rock Tunnel Navigation
- Started: Turn 38914, Saturday, January 10, 2026.
- (11, 25): Entrance from Route 10 South.
- Strategy: Use Flash (KIMCHI) to navigate. Head for northern exit to reach Power Plant area.
- (10, 15): TM47 Steel Wing found.
- Navigation: (11, 14) and surrounding tiles are FLOOR_UP_WALL, blocking passage north from the entrance corridor. Must find alternate route.
- Discovery: Ladder at (27, 13) on 1F leads to B1F at (3, 3).
- B1F Navigation: Exploring east from the ladder area. Currently at (8, 8).
- Discovery: Ladder at (15, 9) on 1F leads to B1F at (17, 9).
- 1F Navigation: Exploring northern section above the ledges. Currently at (15, 9).