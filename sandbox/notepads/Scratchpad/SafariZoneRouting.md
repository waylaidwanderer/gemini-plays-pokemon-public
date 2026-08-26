# Safari Zone Master Routing & Strategy (Run 13 - Active Turn 16791)

## Step Budget Tracking (Run 13)
- Start: 500 steps (Turn 16791 at Gatehouse/Center (15, 24))
- Waypoint 1 (Center to Area 1 East): 28 steps (Turn 16796 at (0, 22)) -> 472 remaining
- Waypoint 2 (Area 1 East to Area 2 North): 67 steps (Turn 16814 at (39, 31)) -> 405 remaining
- Current Position: (35, 11) at Turn 16861 with ~288 steps remaining.

## Empirical Topology & Obstacle Map
- **Center Area (Area 0)**:
  - Gatehouse: (14..15, 24..25)
  - East Exit: (29, 10) -> Area 1 (0, 22) [Single exterior exit verified]
- **Area 1 (East)**:
  - West Exit: (0, 22) <-> Center (29, 10)
  - Northwest Exit: (0, 4..5) <-> Area 2 North (39, 30..31)
- **Area 2 (North)**:
  - East Entrance: (39, 30..31) from Area 1
  - Central Ridge: Ascent stairs at (22, 23), Descent stairs at (16, 27) [Bypasses Col 17 hedge]
  - Vertical Corridor: Column 12/13 connects rows 5-28
  - Northern Highway: Row 2 links cols 2-38 (bypass trees at cols 11-15 via col 10)
  - Southwest Gazebo: Located at (5, 25) (impassable obstacle)
  - East-Central Rest House: Located at (35, 3) (enterable, NPCs inside)
  - Unsurveyed Sectors:
    1. East-Central Sector (cols 23-38, rows 6-25): Unexplored region east of Central Ridge.
    2. East-Central Plateau: Rows 12-25 south of row 11.
    3. Northwest Sector: West of column 5, rows 2-19.

## Target Objectives (Area 3 Targets)
1. **Gold Teeth**: Required for HM04 Strength from Warden in Fuchsia City.
2. **Secret House**: Attendant gives HM03 (Surf).