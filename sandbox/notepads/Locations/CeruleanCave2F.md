# Cerulean Cave (Unknown Dungeon) 2F - Layout & Topology

## Overview
- Upper floor maze of Cerulean Cave (Unknown Dungeon).
- Connects to 1F via multiple ladders and contains the sole descending ladder (Ladder A) to B1F (Mewtwo).

## Connected Component Graph & Routing
1. **Southeast Sector**:
   - Ladder B at (22, 6) <-> 1F (23, 7).
   - Connected via Row 11 thoroughfare (cols 14..24) to Column 24 corridor at (24, 11).
   - Ladder D at (29, 1) descends to 1F NE Terrace (27, 1).

2. **Central Sector & Bypass Network**:
   - Ladder C at (19, 7) <-> 1F (18, 9).
   - Northern Corridors: connect the eastern corridors (cols 24..29) and central bypasses west to the Northwest Sector and Ladder A.
   - Row 9 West Thoroughfare: (15..24, 9) is open floor.
   - Row 8 Western Bypass: (13..15, 8) connects Row 9 at (15, 9) to Column 13 corridor.

3. **West Sector & Route to Ladder A (B1F Mewtwo)**:
   - Ladder E at (9, 1) <-> 1F Northern Terrace (7, 1).
   - Northwest Sector: Row 1 West connects (24, 1) -> (9, 1) -> (3, 1) -> (3, 3) -> Ladder A at (1, 3).
   - Ladder A at (1, 3) descends to B1F (Mewtwo).

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

## Collision Matrix & Verified Passages (2F)
- Column 24 Corridor: Spans rows 11..15. Rows 7..10 are blocked by rock wall. To reach NW Sector / Ladder A, take 1F canal to Ladder E (7, 1).
- Row 11 Thoroughfare: cols 14..24 are open cave floor connecting Column 23 at (23, 11) directly west to Column 19 at (19, 11).
- Row 10 Barrier: Solid rock wall across cols 14..22 blocks direct northward passage from Row 11 (including (15, 10)).
- Central Maze Topology (Verified Turn 47881):
  - Ladder C at (19, 7) connects west via (18, 7) -> (18, 8..9) -> (15..17, 9) -> (13..15, 8) to the northern corridors.
  - Row 11 at (15..23, 11) is a lower thoroughfare connecting east to Ladder B at (22, 6) and south via (14..19, 12..15).
- Verified Empirical Barriers (Turns 47978-48020):
  - (29, 7): Solid rock wall blocks Column 29 south of (29, 6).
  - (27, 3): Solid rock wall blocks direct passage south from (27, 2).
  - (27, 5): Solid rock wall encloses pocket at (27, 4).
  - (17, 3): Solid rock wall blocks westward movement from (18, 3).
  - (21, 3): Solid rock wall blocks direct passage from (21, 2) south to (21, 4).
  - (19, 1): Solid rock wall blocks direct passage between (20, 1) and (18, 1).
- Row 16 Barrier: Solid rock wall across cols 14..20.
- Columns 16-18 Barrier at Row 8: (16..18, 8) are solid rock walls blocking direct northward passage from Row 9.
- Northwest Sector & Ladder A Route: Connected via Row 5 (0..6, 5) -> Column 0 (0, 1..5) -> (1, 1) -> (1, 2) -> Ladder A at (1, 3). Note: Direct passage west from (3, 3) to (1, 3) is blocked by solid rock wall at (2, 3). Ladder E at (9, 1) is an elevated ledge connecting west to (3, 1..3) and east via (9, 4) -> Row 5 (11..16, 5) -> Row 1 (12..18, 1) to Ladder C (19, 7).
- Column 26 North Corridor: (26, 10..14) is open vertical floor connecting Row 14 at (27..28, 14) north past the (28, 13) rock barrier to Row 9 and the northern sectors.
- Row 14 & 15 Western Barrier: (14, 14) and (14, 15) are solid rock walls blocking direct westward passage from (15, 14..15).
- Row 15 Dead-End Pocket: Row 15 extends east across (16..19, 15). (17, 16) and (19, 16) are solid rock walls below it; (20, 15) is a solid rock wall to the east. Traversal south or east from Row 15 is blocked.
## Verified Central Sector Path Matrix (Turn 48036)
- (19, 3) is a solid rock wall separating (20, 3) from (18, 3).
- Verified open path from (20, 3) to Ladder C (19, 7): (20, 3) -> (20, 2) -> (21..22, 2) -> (22, 3..4) -> (21, 4..5) -> (20..19, 5) -> (19, 6..7) [Ladder C].
- (17, 5..8) and (18, 8) are solid rock walls enclosing the pocket west of Ladder C (19, 7); there is no direct passage west from (18, 6..7) on 2F. To reach the NW Sector, use Ladder C down to 1F water canal route to Ladder E.
- Central Pocket Exact Routing: Ladder C (19, 7) <-> (19, 6) <-> (19, 5) <-> (20, 5) <-> (21, 5) <-> (21, 4) <-> (22, 4) <-> (22, 5) <-> (22, 6) Ladder B. (20, 4) is a solid rock wall; (20..22, 2) is an enclosed dead-end corridor. To traverse to other 2F sectors, descend via Ladder C (19, 7) to 1F water canal system.