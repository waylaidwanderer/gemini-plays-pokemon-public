# Safari Zone Master Routing & Strategy (Run 13 -> Run 14)

## Step Budget Tracking (Run 13 - Wrapping Up)
- Start: 500 steps (Turn 16791 at Gatehouse/Center (15, 24))
- Waypoint 1 (Center to Area 1 East): 28 steps (Turn 16796 at (0, 22)) -> 472 remaining
- Waypoint 2 (Area 1 East to Area 2 North): 67 steps (Turn 16814 at (39, 31)) -> 405 remaining
- Current Position: (7, 3) in Center Area at Turn 16891 with ~170 steps remaining.
- Action: Returning to Gatehouse at (15, 24) to start Run 14 with fresh 500 steps.

## Empirical Topology & Disproven Hypotheses
- **Center Area (Area 0)**:
  - Western Boundary: Solidly blocked by Rest House (cols 3-5, rows 2-3) and Picnic Tables (col 6, rows 3 & 5). Continuous solid obstacle wall. DO NOT attempt to exit west from Center Area.
  - Southern Boundary: Rows 24-25 map boundary wall; Gatehouse at (14..15, 24..25).
  - Valid Exits: East exit at (29, 10) -> Area 1 (0, 22). North border at (20, 0) and (14, 0) connects to Area 2.
- **Area 1 (East)**:
  - West Exit: (0, 22) <-> Center (29, 10).
  - Northwest Exit: (0, 4..5) <-> Area 2 North (39, 30..31).
  - Lower Ridge: Stairs at (12, 21) and (20, 21).
  - Northern Plateau: Stairs at (24, 15).
- **Area 2 (North)**:
  - East Entrance: (39, 30..31) from Area 1.
  - East-Central Rest House: Located at (34..37, 2..3), door at (35, 3), sign at (36, 4).
  - East-Central Elevated Plateau: Ascent stairs at (34, 15) leading onto plateau spanning cols 33-38. (UNSURVEYED).
  - Central Ridge: Ascent stairs at (22, 23), Descent stairs at (16, 27).
  - Central Vertical Corridor: Column 12/13 connects rows 5-28.
  - Northern Highway: Row 2 links cols 2-38 (bypass trees at cols 11-15 via col 10).
  - Western Boundary (Column 0): Solid bushes/trees along rows 0-33; statues at (0, 34), (1, 34..35).
  - South Boundary (Row 36): Warps south into Center Area at (20, 0) and (14, 0).

## Run 14 Master Execution Blueprint (500 Step Budget)
1. **Waypoint 1: Center Area Traversal** [28 steps]:
   - From (15, 24): Up 3 to (15, 21) -> Right 10 to (25, 21) -> Up 11 to (25, 10) -> Right 4 to (29, 10) into Area 1 (East) at (0, 22).
2. **Waypoint 2: Area 1 (East) Traversal** [67 steps]:
   - From (0, 22): Down 2 to (0, 24) -> Right 20 to (20, 24) -> Up 3 across Lower Ridge stairs (20, 21) -> Left 8 to (12, 20) -> Down 2 across stairs (12, 21) to (12, 22) -> Left 3 to (9, 22) -> Up 14 along col 9 to (9, 8) -> Right 3 to (12, 8) -> Up 3 across Upper Ridge stairs (12, 7) to (12, 5) -> Right 5 to (17, 5) -> Down 3 across stairs (17, 7) to (17, 8) -> Right 3 to (20, 8) -> Up 6 along col 20 to (20, 2) -> Left 13 along row 2 to (7, 2) -> Down 3 to (7, 5) -> Left 8 to (0, 5) into Area 2 (North) at (39, 31).
3. **Waypoint 3: Area 2 (North) Target Exploration** [~405 steps remaining]:
   - Survey East-Central Plateau via stairs at (34, 15) and remaining unexamined corridors for Area 3 (West) connection.
4. **Target Objectives (Area 3)**:
   - Retrieve **Gold Teeth**.
   - Enter **Secret House** in northwest to receive **HM03 (Surf)**.
