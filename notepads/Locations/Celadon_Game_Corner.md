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