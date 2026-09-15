# Cerulean Cave (Unknown Dungeon) 2F - Layout & Topology

## Overview
- Upper floor maze of Cerulean Cave (Unknown Dungeon).
- Connects to 1F via multiple ladders and contains the descending ladder (Ladder A) to B1F (Mewtwo).

## Verified Ladders (2F)
1. **Ladder A**: Located at (1, 3) -> Descends to B1F (Mewtwo).
2. **Ladder B**: Located at (22, 6) <-> 1F (23, 7).
3. **Ladder C**: Located at (19, 7) <-> 1F (18, 9) [Isolated 7-tile pocket].
4. **Ladder D**: Located at (29, 1) <-> 1F (27, 1).
5. **Ladder E**: Located at (9, 1) <-> 1F (7, 1) [Arrival at (9, 1)].

## Master Route to Ladder A (1, 3) -> B1F (Topography & Routing)
- **Floor Identification**: 2F is completely dry with no water tiles. 1F features distinct blue water canals with wave foam across rows 4-5 and 10-11.
- **Northwest Topography & Target**: Ladder A is located at (1, 3). Entry from 1F is via Ladder E at (7, 1) -> 2F (9, 1).
- **Collision Grid (NW Sector)**:
  - (2, 1), (2, 2), (2, 3), (2, 4) are solid rock barriers.
  - (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4) are solid rock barriers.
  - (8, 5) is a solid rock barrier.
  - (9, 6) is a solid rock barrier.
  - (27, 3), (28, 4) are solid rock barriers.
  - (6, 6) is open floor connecting Row 5 and Row 7.
  - Column 2 (rows 1-4) is a vertical rock barrier.

## Verified Southeastern & Southern Topography (Turns 50872-50910)
- **Ladder D Sector**: Ladder D at (29, 1) connects via (28, 1..3) -> (29, 3..6).
- **Row 6 Crossway**: Open between (29, 6), (28, 6), and (27, 6).
- **Column 27**: Open at (27, 6..7). Impassable rock barrier at (27, 8).
- **Row 7 Bypass**: Open west from (27, 7) through (26, 7) to (25, 7).
- **Column 25 Corridor**: Open south from (25, 7) through (25, 8) to (25, 9) [Row 9].
- **Column 26 Vertical Highway**: Open south from (26, 9) through (26, 10..14). Impassable rock barrier at (26, 15).
- **Row 14 East Bypass**: Open east from (26, 14) through (27, 14) to (28, 14).
- **Column 28 South Corridor**: Open south from (28, 14) through (28, 15) to (28, 16).
- **Row 16 / Row 17 Connector**: Open west from (28, 16) to (27, 16), then south to (27, 17) [Row 17].
- **Row 17 Corridor**: Open west from (27, 17) through (26, 17), (25, 17), (24, 17), (23, 17), (22, 17) to terminal alcove at (21, 17). (20, 17), (21, 16), and (21, 18) are solid rock barriers (verified Turn 50919).
- **Column 24 Barrier (Turn 50934)**: (24, 9) is a solid rock barrier. Ladder D sector has no westward connection to the rest of 2F. Full eastern sector is self-contained.
- **East Crossway Obstacle (Verified Turn 51048)**: (23, 4) is a solid rock barrier. Passage from (22, 4) to (24, 4) routes via (22, 2) -> (24, 2) -> (24, 4).
- **Verified Collision & Obstacle Points (Turns 51069-51091)**:
  - (10, 3) and (10, 4) are solid rock barriers.
  - (13, 7) is a solid rock barrier blocking southward passage from (13, 6).
  - (14, 9) is a solid rock barrier.
  - (24, 6) is a solid rock barrier blocking southward passage from (24, 5).
  - (21, 3), (20, 4), and (21, 6) are solid rock barriers.
  - (20, 7) and (21, 7) are solid rock barriers.
  - (22, 5), (23, 5), and (23, 6) are solid rock barriers.
  - (18, 8), (19, 8), (20, 8), (21, 8), (22, 8), and (24, 8) are solid rock barriers forming a wall along Row 8.  - (22, 9) and (22, 10) are solid rock barriers blocking westward passage from Column 23.

## Verified 2F South & Southeast Corridor Topography (Turns 51154-51171)
- **Row 11 Corridor**: Open across cols 14..23.
- **Row 13 Passages**: Open at (14..15, 13) and (17..20, 13). (16, 13) is a solid rock barrier.
- **Row 15 Enclave**: Open at (15..19, 15). Solid rock barriers at (14, 15) and (20, 15).
- **Row 16 Barrier Line**: Solid rock barrier across (14..20, 16) blocking direct vertical transit from Row 15 to Row 17 on the east side.
- **Row 17 Western Corridor**: Open floor across (11..19, 17). Solid rock barrier at (20, 17) separates Western Row 17 from Eastern Row 17 (21..27, 17).
- **Row 18 Southern Boundary**: Continuous solid rock wall across (11..20, 18).

## Verified Central-South 2F Topography (Turn 51204)
- **Row 9 / Row 8 Northern Bridge**: Open across cols 10..19. Bypasses the rock at (14, 9) via (13, 9) <-> (13, 8) <-> (14, 8) <-> (15, 8) <-> (15, 9).
- **Column 12 Highway**: Continuous open vertical corridor across rows 9..15. Connects (12, 9) in the north to (13, 15..17) and Row 17 in the south.
- **Column 10 West Corridor**: Open at (10, 7), (10, 9), and (10, 11..15).
- **Row 11 Main Corridor**: Open floor across cols 14..23 connecting west central sector directly east to Column 23 and Ladder B at (22, 6).