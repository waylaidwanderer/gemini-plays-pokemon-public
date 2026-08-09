# Celadon Game Corner Topology & Mechanics

## Building Access & Exits
- West Entrance (Celadon City 20, 36 / Courtyard Plaza): Enters West Room at (3, 0) / (3, 7).
- Main Entrance: Located at Celadon City (17, 27) / (25, 25), enters Main Casino Floor at (3, 7).

## Game Corner Interior Layout & Topology
- Central Aisle (Cols 3..4): Open vertical corridor running from North Wall at y=2 down past y=33.
- Slot Machine Banks:
  - Bank 1 (Cols 1..2, y=2..6)
  - Bank 2 (Cols 5..6, y=2..6)
  - Note: Row 6 is blocked at x=5/6 by counter walls.
- Horizontal Cross-Aisles: Row 1/Row 2 and Row 8/Row 33+ provide open horizontal passages across the casino floor.
- Secret Staircase: Located in the Main Game Corner building behind the poster switch guarded by the Rocket Grunt on the North Wall in the East sector (x=15..18). Defeat the Grunt, press A on the poster to reveal the secret staircase to Rocket Hideout B1F.

## Verified Topology & Obstacle Audit (Turn 45151)
- Bank 2 Counters (x=5..6, y=2..6): Empirically confirmed SOLID (bumped at 6,1->7,1; 6,1->6,2; 5,3->6,3; 5,5->6,5; 5,5->5,6).
- Exit Warp Zone: Row 7 at x=2..4 (red carpet) warps directly outside to Celadon City (17,13).
- Central Aisle (x=3..4, y=1..6): Open floor corridor running North-South.
- Staircase at (4,4): Local exit loop staircase connecting to B1F (5,4) and back to (4,4).
- Tile (5,2) Counter: Empirically confirmed SOLID (bumped at 5,3->5,2 on turn 45157).
- Tile (1,5) Counter: Empirically confirmed SOLID (bumped at 2,5->1,5 on turn 45161).
## Verified Wall Boundaries & Topology Audit (Turn 45561)
- Column 6 Wall: Empirically confirmed SOLID counter wall across y=2..5 (bumped at 6, 2 on turn 45561).
- Stool at (7, 1): Empirically confirmed SOLID (bumped at 6, 1 -> 7, 1 on turn 45706).
- Column 7 Aisle: Enclosed vertical aisle spanning y=2..5 bounded by solid stool at (7, 1) and solid green plant at (7, 6).
- Central Aisle (Cols 3..4): Open vertical corridor connecting Row 1 (y=1) down to Row 7 exit carpet.
- Staircase (4, 4): Entrance to Rocket Hideout B1F (5, 4).
## West Room Topology & Main Casino Access (Turn 45841)
- West Room Interior: Small 8x8 room (x=0..7, y=0..7). Exit red carpet at (2,7)/(3,7) warps to East Celadon City (13,25).
- Door (13, 25) in East Celadon City enters this small 8x8 West Room only, NOT the Main Casino Floor!
- True Main Casino Access: From East Celadon City (13, 26), walk East to Column 17 South Avenue, South to Row 30, East to Column 20, and South to tile (20, 36) warp into Game Corner Plaza. Then enter door (10, 2) in Game Corner Plaza to access the Main Casino floor where the Rocket Grunt and poster switch are located.
- Column 5 (x=5): Open vertical floor aisle running North from Row 12 (5, 12) up to North Wall (5, 2).
- Tile (4, 7): Slot machine counter (bumped at 4, 8 -> 4, 7 on Turn 46024). Vertical aisle to North Wall is Column 5 at x=5.
- Column 7 (x=7): Main open vertical floor aisle running North from Row 9 (7, 9) up to Row 2 North Wall aisle (7, 2).
- Tile (5, 4): Slot machine counter (bumped at 5, 5 -> 5, 4 on Turn 46026). Bypass to Row 2 is via Row 5 cross-aisle to Column 7 at (7, 5) -> (7, 2).
- Tile (7, 2): Slot machine counter (bumped at 7, 3 -> 7, 2 on Turn 46028). Horizontal cross-aisle to East sector is Row 8 at y=8.
- Tile (7, 6): Slot machine counter (bumped at 7, 5 -> 7, 6 on Turn 46030). Southbound bypass to Row 8 is via Row 5 cross-aisle to Column 5 at (5, 5) -> (5, 8).
- Tile (6, 8): Slot machine counter (bumped at 5, 8 -> 6, 8 on Turn 46033). Row 12 (y=12) is the main open Southern Horizontal Cross-Highway connecting West and East sectors across x=1..18.
- Casino Topology: Vertical aisles at Column 5 (x=5), Column 9 (x=9), Column 13 (x=13), and Column 18 (x=18) connect Row 12 Cross-Highway directly North to Row 2 North Wall.
- Tile (10, 12): Solid slot machine bank wall (bumped at 9, 12 -> 10, 12 on Turn 46036). Northbound vertical aisle is Column 9 at x=9.
- Column 9 (x=9): Main open vertical floor aisle running North from Row 12 (9, 12) up to Row 2 North Wall aisle (9, 2).
- Tile (10, 2): Solid wall block (bumped at 9, 2 -> 10, 2 on Turn 46039). Single-step inspection of Row 1 / Row 3 / Row 5 Eastbound passages along Column 9.
- Tile (10, 1): Solid wall block (bumped at 9, 1 -> 10, 1 on Turn 46041). Row 13 / Row 14 is the main open South Entrance Highway running East-West across all casino sectors.
- Master Casino Route: Walk South down Column 9 (x=9) to Row 13 (9, 13), East along Row 13 to Column 18 (18, 13), and North along Column 18 to Rocket Grunt at North Wall (18, 2).
- West Room Boundary (Turn 46044): Tile (10, 13) is solid wall. West Room (x=0..9, y=0..13) has no internal passage to Main Casino floor. Exit carpet is at (4, 13)/(5, 13) warping outdoors to East Celadon City (13, 25).
- Master Route to True Main Casino Floor: Exit West Room to East Celadon City (13, 25), walk East to Column 17 South Avenue (17, 26), South to Row 30 (17, 30), East to Column 20 (20, 30), and South along Column 20 to tile (20, 36) warp into Game Corner Plaza. In Plaza (10, 0), enter door (10, 2) to enter True Main Casino Floor at (3, 7).
- Tile (6, 11): Slot machine counter (bumped at 5, 11 -> 6, 11 on Turn 46058). Row 12 (y=12) is the main open Southern Cross-Highway connecting Column 5 (x=5) to Column 9 (x=9).

## Verified Outdoor Plaza & West Room Topography (Turn 46384)
- Game Corner West Room (x=0..7, y=0..7): A self-contained 8x8 interior room. Both Plaza Door A (10, 21) and Door B (17, 27) warp into the exact same indoor exit mat at (3, 7).
- Game Corner Plaza Outdoor Barriers: Double barrels at Column 11 (x=11, y=28..29) and Column 14 (x=14, y=18..23).
- Unblocked Outdoor North Route: From (12, 28), walk Up 2 to Row 26 (12, 26), Left 2 to Column 10 (10, 26), and North along Column 10 to tile (10, 0) warp back to Celadon City (20, 36).
## Verified Unblocked Route Through Game Corner Plaza (Turn 46394)
- Column 10 at y=23 is blocked by a brick wall ledge.
- Column 15 (x=15) is an OPEN vertical grass corridor running all the way North from Row 28 (15, 28) past Row 19 (15, 19) to Row 0 (15, 0) warp back into Celadon City (20, 36).
## EMPIRICAL PROOF (Turn 46561)
- Door (10, 33) in Game Corner Plaza enters ONLY the 8x6 Prize Exchange room (x=0..7, y=0..5) with exit carpets at (3, 5)/(4, 5).
- Door (20, -3) in Game Corner Plaza (x=20, y=-3) is the TRUE MAIN ENTRANCE DOORWAY to the Main Game Corner Casino Floor (building with "GAME" sign at 25, 2).