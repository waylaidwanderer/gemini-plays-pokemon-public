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

3. **Northern Ridge Sector**:
   - Ladder E at (9, 1) <-> 1F Northern Terrace (7, 1) (isolated upper NW ridge).

4. **West Sector & Route to Ladder A (B1F Mewtwo)**:
   - Ladder A at (1, 3) descends to B1F (Mewtwo).

## Verified Ladders (2F)
1. **Ladder A**: Located at (1, 3) -> Descends to B1F (Mewtwo).
2. **Ladder B**: Located at (22, 6) <-> 1F (23, 7).
3. **Ladder C**: Located at (19, 7) <-> 1F (18, 9).
4. **Ladder D**: Located at (29, 1) <-> 1F (27, 1).
5. **Ladder E**: Located at (9, 1) on 2F <-> (7, 1) on 1F.

## Verified Items (2F)
- Item Poké Ball at (29, 9) collected (PP Up).
- Item Poké Ball at (13, 6) collected (Max Potion).
- Item Poké Ball at (4, 15) collected (TM14 Blizzard).

## Collision Matrix & Verified Passages (2F)
- Column 24 Corridor: Spans rows 11..15. Rows 7..10 are blocked by rock wall.
- Row 11 Thoroughfare: Open cave floor across cols 14..24 connecting Column 23 at (23, 11) directly west past Column 19 to Column 14.
- Row 10 Barrier: Solid rock wall across cols 14..22 blocks direct northward passage from Row 11 (including (15, 10)).
- Central Maze Barriers (Turn 47881): (14, 14) and (18, 14) are solid rock walls blocking southern passage from Row 13-14.
- Verified Empirical Barriers (Turns 47978-48020):
  - (29, 7): Solid rock wall blocks Column 29 south of (29, 6).
  - (27, 3): Solid rock wall blocks direct passage south from (27, 2).
  - (27, 5): Solid rock wall encloses pocket at (27, 4).
  - (17, 3): Solid rock wall blocks westward movement from (18, 3).
  - (21, 3): Solid rock wall blocks direct passage from (21, 2) south to (21, 4).
  - (19, 1): Solid rock wall blocks direct passage between (20, 1) and (18, 1).
- Row 16 Barrier: Solid rock wall across cols 14..20.
- Columns 16-18 Barrier at Row 8: (16..18, 8) are solid rock walls blocking direct northward passage from Row 9.
- Northwest Sector & Ladder A Route: Ladder A at (1, 3) descends to B1F (Mewtwo). Solid rock barriers at (2, 3), (3, 4), and (8, 5) separate local paths on 2F. Ladder A is accessed via an isolated lower 2F western sector that is completely walled off from Northern Ridge (Ladder E), Eastern Corridor (Ladder D), and Southeast Sector (Ladder B/C).
- Column 26 North Corridor: (26, 10..14) is open vertical floor connecting Row 14 at (27..28, 14) north past the (28, 13) rock barrier to Row 9 and the northern sectors.
- Row 14 & 15 Western Barrier: (14, 14) and (14, 15) are solid rock walls blocking direct westward passage from (15, 14..15).
- Row 15 Dead-End Pocket: Row 15 extends east across (16..19, 15). (17, 16) and (19, 16) are solid rock walls below it; (20, 15) is a solid rock wall to the east. Traversal south or east from Row 15 is blocked.
## Verified Central Sector Path Matrix (Turn 48036)
- (19, 3) is a solid rock wall separating (20, 3) from (18, 3).
- Verified open path from (20, 3) to Ladder C (19, 7): (20, 3) -> (20, 2) -> (21..22, 2) -> (22, 3..4) -> (21, 4..5) -> (20..19, 5) -> (19, 6..7) [Ladder C].
- (17, 5..8) and (18, 8) are solid rock walls enclosing the pocket west of Ladder C (19, 7); there is no direct passage west from (18, 6..7) on 2F. 
- Central Pocket Exact Routing: Ladder C (19, 7) connects north via (19, 5..6) -> (20..21, 5) -> (21..22, 4) -> (20..22, 2..3) enclosed upper loop. (22, 5) and (20, 4) are solid rock walls blocking direct passage between (22, 4) and Ladder B (22, 6).
- Column 9 Collision: (9, 6) is a solid rock wall blocking direct southern passage from (9, 5) to Row 7.
- Ladder E Ridge Isolation: Ladder E at (9, 1) arrives on an elevated northern ridge spanning (3..9, 1), (3..9, 3), and (9..16, 5). It is walled off from the lower western corridors and Ladder A (1, 3) by solid rock barriers at (2..3, 1..4), (9, 6), and (12..15, 7).
- Column 24 corridor (24, 1..5) and (25..27, 4) are an enclosed dead-end sector on 2F separated from Ladder D (29, 1). 
- Eastern Sector & Ladder D Routing (Verified Turns 48174-48182):
  - Ladder D at (29, 1) connects south via (29, 3..6) -> (28..25, 6..7) towards (25, 8..9).
  - Row 9 at (25, 9) is blocked to the west by solid rock walls at (24, 9) and (24, 5..10).
- NW Sector Collision Details (Verified Turns 48154-48165):
  - Row 3 is open across cols 3..9 at (3..9, 3), but (3, 4) is a solid rock wall blocking direct southern passage from (3, 3) to Row 5. Column 9 connects (9, 3) down to (9, 5), which connects east along Row 5 (9..16, 5).
- Column 24 Barrier: (24, 7..10) are solid rock walls blocking northward passage from (24, 11).
- Column 25 Barrier: (25, 12..15) are solid rock walls blocking eastward passage from Column 24 to Column 26. Row 11 dead-ends eastward at Column 24.
## Northwest Sector & Ladder A Data
- **Ladder A Location**: Located at (1, 3) -> Descends directly to B1F (Mewtwo).
- **Enclosure & Barriers**:
  - Ladder A at (1, 3) is isolated from upper 2F sectors by confirmed rock walls at (2, 2), (2, 3), (3, 4), (5, 4), (6, 4), (8, 5), (9, 6), and (10, 1).
  - True access to Ladder A / B1F must be accessed from 1F.
## Northern Ridge & NW Sector Analysis (Verified Turn 48529)
- **Ridge Isolation**: Ladder E at (9, 1) arrives on an elevated northern ridge (cols 3..16, rows 0..2) that is completely walled off from the lower floors ((15, 3) is a cliff ledge overlooking lower floor where "No SURFing on HYDROS here!").
- **Isolated Maze Topology**: Ladder E (9, 1), Ladder D (29, 1), Ladder B (22, 6), and Ladder C (19, 7) all lead to isolated sectors on 2F that cannot access Ladder A (1, 3). The true route to Ladder A (1, 3) and B1F Mewtwo must be accessed via unmapped 1F ground/water passages.
- Column 17/16 Boundary at Row 1-2 (Verified Turn 48568):
  - (17, 2) and (16, 2) are solid rock walls.
  - Row 1 across (14..18, 1) is open cave floor providing the direct east-west thoroughfare between the eastern sector and western sector.
- Column 10 Boundary & Passage (Verified Turn 48580):
  - (10, 0..4) are solid rock walls blocking east-west movement between Column 11 and Column 9.
  - (10, 5) is open cave floor providing the direct passage from Column 11 at (11, 5) west to (9, 5).

- Verified Open East-West Passage at (12, 5) (Turn 49086): Tile (12, 5) is completely open dark cave floor connecting (11, 5) directly east to Column 13 (13, 5) and Row 5 (13..16, 5).
- Verified Barriers at (2, 2) and (6, 4) (Turns 49223-49230): Tile (2, 2) is a solid rock wall blocking direct westward access from (3, 2). Tile (6, 4) is a solid rock wall blocking direct southern passage from (6, 3).
- Northern Ridge Exhaustive Boundary Audit (Turn 49247): The Northern Ridge (Ladder E at 9, 1) is completely isolated by confirmed rock walls at: (2, 2), (2, 3), (3, 4), (5, 4), (6, 4), (8, 5), (9, 6), (10, 1), (12, 7), (13, 7), (14, 7), (15, 7), (16, 8), (17, 5), and (18, 5). It has zero physical ground connections to lower 2F or Ladder A.
- **Ladder B Column 23 Corridor**: From Ladder B (22, 6), move Down to (22, 7), East to (23, 7), and South along Column 23 (rows 7..11) to reach Row 11 Thoroughfare at (23, 11). Note that (22, 8..10) are solid rock walls.
- **Row 11 Western Barriers (Turns 49392 & 49395)**:
  - (13, 11) and (13, 12) are confirmed solid rock walls blocking westward traversal from (14, 11..12).
  - Column 14 extends south across (14, 13..14) to open floor on Row 14/15 (cols 15..19).
- **Ladder C (19, 7) Western Maze Access (Hypothesis - Unverified)**:
  - Western traversal from Ladder C (19, 7) across Row 7 requires empirical point-by-point verification.

## Verified Northern Ridge Barriers & Enclosure (Turn 49501)
- **Verified Collision Barriers**:
  - (9, 6), (10, 6), (11, 6), (12, 6), (14, 6), (15, 6) are solid rock walls blocking southern egress from Row 5.
  - (13, 7) is a solid rock wall making (13, 6) a dead-end pocket (Max Potion item ball).
  - (16, 8) is a solid rock wall making (16, 7) a dead-end pocket.
  - (17..18, 5) are solid rock walls blocking direct passage between Row 5 and the central loop.
- **Topology Conclusion**: The Northern Ridge (Ladder E at 7, 1 on 2F) and Row 5 (cols 9..16) form an entirely self-contained upper sector on 2F with no ground passage to the southern half of 2F or Ladder A. Access to the main 2F maze and southwest sector (TM14 Blizzard at 4, 15) must be entered via Ladder B at (23, 7) on 1F.
- **Column 24 South Termination (Turn 49520)**: Column 24 dead-ends at (24, 15); (24, 16) is a solid rock wall. Direct access from Column 24 south into Row 17 is blocked.
- **Column 25 Barrier at Row 10 (Turn 49544)**: Tile (25, 10) is a solid rock wall blocking direct southward passage from (25, 9); detour west via (24, 9..12) or east via (26, 10..14).
- **Eastern Sector Bypass (Turn 49542)**: Tile (26, 6) is a solid rock wall. Bypass to the south: (27, 6) -> Down to (27, 7) -> Left to (26, 7) -> Left to (25, 7) -> opens south into Column 25/26 (rows 8..14).
- **Row 17 Eastern Termination & Row 13 Bypass (Turn 49556)**: Tile (20, 17) is a solid rock wall blocking Row 17 westward at (21, 17). Open bypass to the northwest: (21, 17) -> Up 2 to (21, 15) -> Right to (22, 15) -> Up 2 to (22, 13) -> opens west along Row 13 (21..17, 13).
- **Row 13 Western Barrier & Row 11 Connector (Turn 49566)**: Tile (16, 13) is a solid rock wall blocking Row 13 westward at (17, 13). Connector to Row 11: (17, 13) -> Up 2 to (17, 11) opens west along Row 11 Thoroughfare to (14, 11).