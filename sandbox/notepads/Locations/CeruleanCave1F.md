# Cerulean Cave (Unknown Dungeon) 1F - Layout & Topology

## Map Overview
- **Dimensions**: 30x20 grid (cols 0..29, rows 0..19).
- **Sectors**:
  1. **Entrance Basin (Southeast, cols 20..25, rows 12..17)**:
     - Cave entrance/exit mat at (24..25, 17) connects to Cerulean City NW Waterway Pool (4, 11).
     - Ascending ramp at (21, 11) leads up to Upper Plateau.
     - Entrance Basin has NO direct water access to the Central Waterway.
  2. **Upper Plateau (East/Central, cols 21..25, rows 6..10)**:
     - Reachable from Entrance Basin via ramp at (21, 11).
     - Contains **Ladder B** at (23, 7) <-> 2F (22, 6).
     - Ramp at (25, 9) leads south into dead-end wall at (25, 10).
     - Divided from Central Corridor to the west by solid purple rock wall along Column 20 (rows 6..13).
  3. **Central Corridor & Waterways (cols 8..23, rows 4..17)**:
     - Accessible from NE Terrace via South-facing ramp at (23, 3).
     - Contains **Ladder C** at (18, 9) <-> 2F (19, 7).
     - Contains **Water Ramp** at (17, 15) facing west into water canal at (16, 15).
     - Main north-south waterway runs along cols 8..17 across rows 1..15 leading north to Ladder E.
  4. **Northern Corridor & Landings (cols 0..29, rows 0..3)**:
     - **NE Terrace (cols 23..29, rows 0..3)**: Contains **Ladder D** at (27, 1) <-> 2F (29, 1). Open floor along Row 1 (27..23, 1) and Row 2 (27..23, 2). Solid rock barrier at (22, 1..3) and south border at row 3 (blocked by rock/ledge collision).
  5. **Negative Boundaries & Movement Constraints**:
     - Upper Plateau (23, 6): Facing Up into water (23, 5) yields 'No SURFing on HYDROS here!' due to elevation cliff border.
     - NE Terrace (23, 3): Blocked by solid rock collision to the south.
     - Entrance Basin (20..25, 12..17): Separated from Central Corridor by solid rock along cols 19-20. Accessible to Upper Plateau via ascending ramp at (21, 11).
     - **NW Waterway Landing (cols 0..9, rows 0..3)**: Contains **Ladder E** at (7, 1) <-> 2F (9, 1). Reached via Surfing north along Central Waterway from (17, 15).
     - Ladder E connects to 2F West Sector -> Ladder A at (1, 3) -> B1F (Mewtwo).