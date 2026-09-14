# Cerulean Cave (Unknown Dungeon) 2F - Layout & Topology

## Overview
- Upper floor maze of Cerulean Cave (Unknown Dungeon).
- Connects to 1F via multiple ladders and contains the descending ladder (Ladder A) to B1F (Mewtwo).

## Verified Ladders (2F)
1. **Ladder A**: Located at (1, 3) -> Descends to B1F (Mewtwo).
2. **Ladder B**: Located at (22, 6) <-> 1F (23, 7).
3. **Ladder C**: Located at (19, 7) <-> 1F (18, 9).
4. **Ladder D**: Located at (29, 1) <-> 1F (27, 1).
5. **Ladder E**: Located at (9, 1) <-> 1F (7, 1).

## Verified Items (2F)
- Item Poké Ball at (29, 9) collected (PP Up).
- Item Poké Ball at (13, 6) collected (Max Potion).
- Item Poké Ball at (4, 15) collected (TM14 Blizzard).

## Verified Topology & Passages
1. **Northern Ridge (Isolated)**:
   - Contains Ladder E at (9, 1).
   - Fully isolated: bounded north by rock walls (4..6, 0), west by (2, 1..3), south by (3..8, 4), and east/south by rock walls at (9, 6), (10, 6), (11, 6), (12, 6), (14, 6), (15, 6), (16, 8), and (17..18, 5).
2. **Southeast & East Sector**:
   - Ladder B at (22, 6) -> move Down to (22, 7), East to (23, 7), South along Column 23 (rows 7..11) to Row 11 at (23, 11).
   - Row 11 Thoroughfare: open floor across cols 14..24.
   - Column 24: spans rows 11..15; dead-ends at (24, 15).
   - Column 26: open vertical corridor spanning rows 9..14.
   - Ladder D at (29, 1) connects south via (29, 3..6) -> (28..25, 6..7) to Column 26 at (26, 9..14).
3. **South-Central & Southern Corridors**:
   - Row 11 connects to Row 13 via Column 17: (17, 11) -> (17, 12) -> (17, 13).
   - Row 13 connects across cols 17..22 to Column 22.
   - Column 22 connects south: (22, 13) -> (22, 14..15) -> (21, 15) -> (21, 16..17) to Row 17.
   - Row 17 spans (21..28, 17), connecting east via Column 28 (28, 16..14) to Column 26 (26, 14).
   - Column 26 connects north to (26, 9), leading west through (25, 9) into the Southwest Corridor toward (4, 15).
- Collision at (25, 7): Tile (25, 7) is a solid rock wall blocking direct northward passage from (25, 8). (25, 9) egress is via Column 26 at (26, 9).
- Collision at (14, 14) (Verified Turn 50304): Tile (14, 14) is a solid rock wall terminating Column 14 southward at (14, 13).
- Collision at (17, 16) (Verified Turn 50306): Tile (17, 16) is a solid rock wall blocking direct southward passage from (17, 15).