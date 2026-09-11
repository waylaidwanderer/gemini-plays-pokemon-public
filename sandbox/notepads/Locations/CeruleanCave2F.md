# Cerulean Cave (Unknown Dungeon) 2F - Layout & Notes

## Connected Component Graph (2F)
- **2F Partitioned Maze Structure**: 2F is divided into 3 distinct, physically separated sub-graphs by solid purple rock barriers:
  1. **West Sector (cols 1..9, rows 0..5)**: Reachable via Ladder E at (9, 1) <-> 1F (7, 1). Contains Ladder A at (1, 3), which descends directly to B1F (Mewtwo).
  2. **Central/East Sector (cols 11..29, rows 1..19)**: Reachable via Ladder C at (19, 7) <-> 1F (18, 9) and Ladder B at (22, 6) <-> 1F (23, 7). Contains items (Max Potion, TM14 Blizzard, PP Up) and S-Bypass. Physically blocked from West Sector across rows 0-5 by solid Column 10 rock wall.
  3. **NE Pocket (col 29, rows 1..5)**: Reachable via Ladder D at (29, 1) <-> 1F (27, 1). Isolated dead-end landing.

## Verified Physical Boundaries & Corridors (2F)
- Solid Rock Collisions verified: (2, 1..4), (5..10, 2), (9, 2), (12, 2..4), (16, 2), (17, 2..8), (10, 1..3), (14, 2..4), (7, 4), (8, 4..5), (11, 4), (20, 4), (8, 5), (15, 6), (5..14, 6), (17, 6), (21, 6), (15, 7), (16, 8), (17, 7), (22, 5), (23, 6), (22, 9), (14, 10), (11, 11), (13, 12), (13, 11..15), (15, 12), (16, 12), (18..20, 12), (22, 12), (16, 13..14), (25, 13..14), (14, 14..16), (15, 14), (22, 8..10), (24, 8..10), (25, 10..11), (17, 10), (17, 14), (18, 14), (19, 14), (20, 12..20 solid wall), (21, 14), (22, 16), (27, 12..13), (27, 15), (28, 8), (28, 13), (29, 7..8), (29, 10..11).
## Open Thoroughfares
- **Central-to-NW S-Bypass (Verified Bidirectional)**: Connects Central Hub (19, 7) to NW Sector (18, 1..3) via (19, 7) <-> (19, 5) <-> (21, 5) <-> (21, 4) <-> (22, 4) <-> (22, 2) <-> (20, 2) <-> (20, 3) <-> (18, 3) <-> (18, 1).
- Row 1 North Bypass: (5..16, 1) and (18, 1).
- Row 3 West Corridor: (3..9, 3) open continuous floor; connects to Ladder E at (9, 1) via Column 3 North (3, 3) -> (3, 1) -> Row 1 East (4..9, 1). Note: (9, 2) is solid rock blocking direct north passage from (9, 3) to (9, 1).
- Column 13 Corridor: (13, 1..5) connects Row 1 to Row 5. Tile (13, 6) is a 1-tile dead-end pocket (Max Potion collected Turn 40906; (13, 7) empirically verified solid rock on Turn 43000).
- Row 5: East segment (11..16, 5) and West segment (1..7, 5). Note: Probed moving Left from (11, 5) on Turn 44425 and blocked by solid rock collision at (10, 5), indicating no direct passage between (11, 5) and (9, 5) across Row 5. Row 3 (3..9, 3) connects Column 9 (9, 3) west to Column 3 (3, 3) and Ladder A (1, 3).
- Column 23 Corridor: (23, 7..11) connects Ladder B landing at (22, 7) to Row 11 East corridor.
- Row 11 Corridor: (17..23, 11) connects Column 17 to Column 23.
- Row 13 Corridor: (17..22, 13) connects Column 17 to Column 21/22.
- Column 21-22 South S-Connector: (22, 13..15) -> (21, 15..17) connects Row 13 to Row 17 Artery.
- Row 17 South Artery: (21..28, 17) connects Column 21 to Column 28/29.

## Verified Items (2F)
- Item Pokéball at (29, 9) collected (PP Up).
- Item Pokéball at (13, 6) collected (Max Potion).
- Item Pokéball at (4, 15) collected (TM14 Blizzard).

## Wild Encounters (2F)
- Ditto, Chansey, Venomoth, Kadabra, Dodrio, Rhydon, Electrode, Marowak, Wigglytuff.
## Disproven Routes & Collision Barriers
- **Row 16 Central Rock Wall (Turn 41901-41902)**: (14..20, 16) is a continuous solid purple rock wall. The pocket at (14..15, 13..15) has NO southern connection to Row 17.
- **Row 14 Column 14 Barrier (Verified Turn 42177)**:
  - Row 11 runs clear from (23, 11) west to (14, 11). (13, 11) is solid rock.
  - Column 14 runs south from (14, 11) to (14, 13) only. Tile (14, 14) is solid purple rock blocking direct southern passage along Column 14.
  - From (14, 13), passage turns east towards (15, 13).
- **Row 4 West Barrier (Verified Turns 42252 & 42769)**: (1..8, 4) is a continuous solid purple rock wall (tested at cols 3, 4, 5, 6, 7, 8).
- **Column 2 Barrier (Verified Turn 42769)**: (2, 0..4) is continuous solid rock. (3, 1) -> (2, 1) is blocked.
- **Column 16 Barrier (Verified Turn 42288)**:
  - Column 16 runs south from (16, 3..7), but (16, 8) is solid purple rock blocking direct access down to Row 9. Tile (16, 7) is a dead-end pocket.
- **South-West Ledge Dead-End (Verified Turn 42387 & 42481)**:
  - The 1F South-Western Ridge (cols 1-6, rows 8-12) accessed via South Ramp at (1, 13) contains NO ladder or warps. Tile (3, 11) on 1F is regular cave floor.
  - The 4 ladders between 1F and 2F are Ladder B (22, 6 <-> 23, 7), Ladder C (19, 7 <-> 18, 9), Ladder D (29, 1 <-> 27, 1), and Ladder E (9, 1 <-> 7, 1). Ladder A is at (1, 3) and descends directly to B1F!
- **Ladder D Isolated Pocket (Verified Turn 42807)**: Ladder D at 2F (29, 1) leads only to an isolated dead-end hook: (29, 1) <-> (28, 1..3) <-> (29, 3..5). All surrounding tiles (28, 4..5), (29, 6), etc. are solid rock. It has NO connection to the main 2F network.
- **2F Central Network Isolation (Verified Turn 42887 & 44425)**: The Central/East network on 2F (cols 11..29) connects Ladder C at (19, 7) to Row 1 North Bypass (11..18, 1), but is blocked from Ladder E at (9, 1) by the Column 10 rock wall and has no direct southern ground connection across Row 8.
- **Row 15/16 South Boundary (Verified Turns 43064-43071)**:
  - Column 15 runs south from Row 13 to (15, 13) only; tile (15, 14) is solid purple rock blocking southern passage along Column 15.
  - Row 15 pocket spanning (15..19, 15) is a dead end bounded by rock to the north (Row 14), south (Row 16), and east (20, 15).
- **Ladder C Landing Southern Barrier (Verified Turn 43693)**: Tile (18, 8) is solid purple rock (empirically blocked moving Down from (18, 7)). The Ladder C landing at (18..19, 5..7) is completely bounded to the south by Row 8 rock wall ((16..22, 8)); there is NO passage south into Row 9 from Ladder C landing.
- **Column 10 Barrier (Empirically Verified Rows 0-5 on Turns 44425 & 44547-44548)**:
  - Column 10 contains purple rock wall from (10, 0) down to (10, 5) blocking direct east-west passage across Rows 0-5.
  - Tile (10, 1) is solid purple rock. Row 1 North Bypass does NOT connect across Column 10.
  - The 2F West sector containing Ladder A at (1, 3) (which descends to B1F/Mewtwo) and Ladder E at (9, 1) is separated from the 2F Central/East sector (cols 11..29) across rows 0-5.
- **2F Sub-Graph Layout**:
  - **West Sector (Contains Ladder E (9, 1) and Ladder A (1, 3))**:
    - Spans cols 1..9, rows 0..5. Ladder A at (1, 3) descends to B1F.
  - **Central/East Sector (Reachable via Ladder C at (19, 7) <-> 1F (18, 9))**:
    - Spans cols 11..29, rows 1..19. Contains S-Bypass, Row 1 East corridor (11..18, 1), and Ladder B landing (22, 6). Contains items (Max Potion, TM14, PP Up).
  - **NE Sector (Reachable via Ladder D at (29, 1))**:
    - Isolated landing.