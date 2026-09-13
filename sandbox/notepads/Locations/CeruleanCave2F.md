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
   - Central Loop: Ladder C connects north via (19, 5..6) -> (20..21, 5) -> (21..22, 4) -> (20..22, 2..3). Walled off from lower corridors by rock walls at (18..20, 4), (16, 8), (17, 5..8), and (19, 1).

3. **West Sector & Route to Ladder A (B1F Mewtwo)**:
   - Ladder E at (9, 1) <-> 1F Northern Terrace (7, 1) (isolated upper NW ridge).
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
- Column 24 Corridor: Spans rows 11..15. Rows 7..10 are blocked by rock wall.
- Row 11 Thoroughfare: cols 14..24 are open cave floor connecting Column 23 at (23, 11) directly west to Column 19 at (19, 11).
- Row 10 Barrier: Solid rock wall across cols 14..22 blocks direct northward passage from Row 11 (including (15, 10)).
- Central Maze Topology (Verified Turn 47881):
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
- Northwest Sector & Ladder A Route: Ladder A at (1, 3) descends to B1F (Mewtwo) and is accessed via 2F NW sector corridors connected to Ladder E at (9, 1). Solid rock barriers at (2, 3), (3, 4), and (8, 5) separate local paths.
- Column 26 North Corridor: (26, 10..14) is open vertical floor connecting Row 14 at (27..28, 14) north past the (28, 13) rock barrier to Row 9 and the northern sectors.
- Row 14 & 15 Western Barrier: (14, 14) and (14, 15) are solid rock walls blocking direct westward passage from (15, 14..15).
- Row 15 Dead-End Pocket: Row 15 extends east across (16..19, 15). (17, 16) and (19, 16) are solid rock walls below it; (20, 15) is a solid rock wall to the east. Traversal south or east from Row 15 is blocked.
## Verified Central Sector Path Matrix (Turn 48036)
- (19, 3) is a solid rock wall separating (20, 3) from (18, 3).
- Verified open path from (20, 3) to Ladder C (19, 7): (20, 3) -> (20, 2) -> (21..22, 2) -> (22, 3..4) -> (21, 4..5) -> (20..19, 5) -> (19, 6..7) [Ladder C].
- (17, 5..8) and (18, 8) are solid rock walls enclosing the pocket west of Ladder C (19, 7); there is no direct passage west from (18, 6..7) on 2F. 
- Central Pocket Exact Routing: Ladder C (19, 7) connects north via (19, 5..6) -> (20..21, 5) -> (21..22, 4) -> (20..22, 2..3) enclosed upper loop. (22, 5) and (20, 4) are solid rock walls blocking direct passage between (22, 4) and Ladder B (22, 6).
- Column 9 Collision: (9, 6) is a solid rock wall blocking direct southern passage from (9, 5) to Row 7.
- Ladder E Ridge Isolation: Ladder E at (9, 1) arrives on an elevated northern ridge spanning (3..9, 1), (3..9, 3), and (9..16, 5). It is walled off from the lower western corridors and Ladder A (1, 3) by solid rock barriers at (2..3, 1..4), (9, 6), and (12..15, 7). Active systematic tile probing is focused on NW sector corridors.
- Column 24 corridor (24, 1..5) and (25..27, 4) are an enclosed dead-end sector on 2F separated from Ladder D (29, 1). 
- Eastern Sector & Ladder D Routing (Verified Turns 48174-48182):
  - Ladder D at (29, 1) connects south via (29, 3..6) -> (28..25, 6..7) towards (25, 8..9).
  - Row 9 at (25, 9) is blocked to the west by solid rock walls at (24, 9) and (24, 5..10).
- NW Sector Collision Details (Verified Turns 48154-48165):
  - Row 3 is open across cols 3..9 at (3..9, 3), but (3, 4) is a solid rock wall blocking direct southern passage from (3, 3) to Row 5. Column 9 connects (9, 3) down to (9, 5), which connects east along Row 5 (9..16, 5).
- Column 24 Barrier: (24, 7..10) are solid rock walls blocking northward passage from (24, 11).
- Column 25 Barrier: (25, 12..15) are solid rock walls blocking eastward passage from Column 24 to Column 26. Row 11 dead-ends eastward at Column 24.
## Northwest Sector & Ladder A Complete Solution (Verified Turn 48396)
- **Ladder A Location**: (1, 3) -> Descends directly to B1F (Mewtwo).
- **Enclosure & Entry Points**:
  - (2, 3) is solid rock wall blocking direct access from Row 3 east.
  - (0, 3) is open floor directly west of Ladder A at (1, 3).
  - (1, 2) and (0, 2) are open floor north of Ladder A.
  - Column 0 corridor spans (0, 2..6), connecting directly to Row 5 at (0, 5).
  - Row 5 is open floor across (0..7, 5).
  - (6, 6) is open floor connecting Row 5 at (6, 5) south to Row 7 at (6, 7).
  - Row 7 spans open floor across (1..8, 7).
- **Local NW Branch Mapping Protocol**:
  - Note: Direct passage from (5, 3) -> (5, 4) is blocked by rock at (5, 4). Systematic single-tile probing of western vertical corridors (cols 14..6) is required.
## Northern Ridge & NW Sector Analysis (Verified Turn 48529)
- **Ridge Isolation**: Ladder E at (9, 1) arrives on an elevated northern ridge (cols 3..16, rows 0..2) that is completely walled off from the lower floors ((15, 3) is a cliff ledge overlooking lower floor where "No SURFing on HYDROS here!").
- **True Path to Ladder A (1, 3)**: Accessed via **Ladder C** at (18, 9) on 1F <-> (19, 7) on 2F, which connects to the main open floor, Row 9 thoroughfare, Column 13 corridor, and directly to Ladder A (1, 3) on 2F to descend to B1F Mewtwo!
- Column 17/16 Boundary at Row 1-2 (Verified Turn 48568):
  - (17, 2) and (16, 2) are solid rock walls.
  - Row 1 across (14..18, 1) is open cave floor providing the direct east-west thoroughfare between the eastern sector and western sector.
- Column 10 Boundary & Passage (Verified Turn 48580):
  - (10, 0..4) are solid rock walls blocking east-west movement between Column 11 and Column 9.
  - (10, 5) is open cave floor providing the direct passage from Column 11 at (11, 5) west to (9, 5).
