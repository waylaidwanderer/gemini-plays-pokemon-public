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
1. **Master Route to Ladder A & B1F (Verified Turn 50487)**:
   - **Entry via Ladder B at 2F (22, 6)**:
     - (22, 6) -> Down to (22, 7) -> East to (23, 7) -> South along Column 23 to Row 11 at (23, 11).
     - Row 11 Highway: Move West across (23..14, 11) to (14, 11).
     - Column 12 Bypass: From (14, 11) -> Down to (14, 12) -> West to Column 12 at (12, 12).
     - Column 12 Corridor: Move North uninterrupted along Column 12 across (12, 12..7) to Row 7 at (12, 7).
     - Row 7 Western Highway: Move West uninterrupted across (12..2, 7) to Column 2 at (2, 7).
     - Column 2 Ascent: Move North (2, 7) -> (2, 6) -> (2, 5) to Row 5 at (2, 5).
     - Row 5 NW Sector: Move West (2, 5) -> (1, 5) -> (0, 5) to Column 0 at (0, 5).
     - Column 0 Ascent: Move North (0, 5) -> (0, 4) -> (0, 3) to Row 3 at (0, 3).
     - **Ladder A Entry**: From (0, 3), step East into **Ladder A at (1, 3)**!
     - Ladder A at (1, 3) descends directly to B1F (Mewtwo).
   - **Northern Ridge & Ladder E at (9, 1)**:
     - Ladder E at (9, 1) connects via (8, 1) -> (8, 3) -> (9, 3) -> (9, 5) -> Row 5 (9..16, 5).
     - Column 9 terminates south at (9, 6) (rock wall).
     - Column 16 connects Row 5 (16, 5) south to (16, 7), terminating at (16, 8) (rock wall).
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
   - Column 26 connects north to (26, 9), leading west along Row 9 across cols 25..15.
- Collision at (25, 7): Tile (25, 7) is a solid rock wall blocking direct northward passage from (25, 8). (25, 9) egress is via Column 26 at (26, 9).
- Collision at (14, 14) (Verified Turn 50304): Tile (14, 14) is a solid rock wall terminating Column 14 southward at (14, 13).
- Collision at (17, 16) (Verified Turn 50306): Tile (17, 16) is a solid rock wall blocking direct southward passage from (17, 15).
- E-W Sector Bridge at Rows 8-9 (Verified Turn 50315): (13, 8), (14, 8), and (15, 8) are open floor tiles forming a northern bypass around the (14, 9) rock wall, connecting Row 9 East (cols 15..19) directly to Row 9 West (cols 10..13) and the western corridors.
- **Ladder C Sector (Verified Turn 50348)**: Ladder C at 2F (19, 7) is an isolated 7-tile pocket consisting of (19, 7), (18, 7), (18, 6), (19, 6), (20, 6), (19, 5), and (20, 5), completely bounded by solid rock walls to the north (rows 4-5), west (col 17), south (row 8), and east (col 21). It has no exit to the rest of 2F. Main 2F thoroughfares must be accessed via Ladder B (22, 6) -> Row 11 -> Column 16 / (13..15, 8) bypass -> Row 3.
- **SE Corridor Collision Details (Verified Turn 50373)**: Tile (28, 17) is a rock wall; Row 17 (cols 21..27) connects to Column 28 via (27, 17) -> (27, 16) -> (28, 16). Tile (27, 15) is a rock wall. Column 28 runs open north through (28, 16..14) connecting to (26, 14) and Column 26.
- **Collision at (25, 11..13) (Verified Turn 50383)**: Column 25 is a solid rock wall across rows 10..13 blocking direct westward passage from (26, 11). Westward egress from Column 26 is via Row 14 (26..22, 14) or Row 17 (28..21, 17).
- **Collision at (14, 15) (Verified Turn 50398)**: Tile (14, 15) is a solid rock wall blocking direct westward passage from (15, 15). Column 14 forms a vertical rock wall on rows 14..16.
- **Collision at (20, 17) (Verified Turn 50410)**: Tile (20, 17) is a solid rock wall blocking direct westward passage from (21, 17) on Row 17. Row 17 East (cols 21..27) and Row 17 West (cols 11..19) are separated by this barrier.
- Collision at (13, 11) (Verified Turn 50486): Tile (13, 11) is a solid rock wall blocking direct westward passage along Row 11 from (14, 11). Westward egress to Column 12 is via (14, 12) -> (12, 12).
- Collision at (13, 12..16) (Verified Turn 50496): Column 13 is a solid rock wall across rows 11..16 blocking direct westward passage from Column 14. Egress to Row 9 West is via Column 26 (26, 9..14) -> Row 9 (cols 26..15) -> (15..13, 8) -> (13..10, 9).