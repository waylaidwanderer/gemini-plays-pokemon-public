# Cerulean Cave (Unknown Dungeon) 2F - Layout & Notes

## Connected Component Graph (2F)
- **Main 2F Connected Maze**: Continuous walkable maze spanning cols 1-29 and rows 1-19.
  - Ladder A1: (1, 3) [Target NW isolated ladder descending to 1F Upper Western Platform].
  - Ladder C: (19, 7) <-> 1F (18, 9) [Central transit hub].
  - Ladder B: (22, 6) <-> 1F (23, 7) [Central-East landing].
  - Ladder D: (29, 1) <-> 1F (27, 1) [Isolated NE landing].
  - Ladder E: (9, 1) <-> 1F (7, 1) [Confirmed visually at (9, 1) on Turn 40906].

## Verified Physical Boundaries & Corridors (2F)
- Solid Rock Collisions verified: (2, 1..4), (5..10, 2), (9, 2), (12, 2..4), (16, 2), (17, 2..8), (10, 1..3), (14, 2..4), (7, 4), (8, 4..5), (11, 4), (20, 4), (8, 5), (15, 6), (5..14, 6), (17, 6), (21, 6), (15, 7), (16, 8), (17, 7), (22, 5), (23, 6), (14, 10), (11, 11), (13, 12), (13, 11..15), (15, 12), (16, 12), (18..20, 12), (22, 12), (16, 13..14), (25, 13..14), (14, 14..16), (15, 14), (22, 8..10), (24, 8..10), (25, 10..11), (17, 10), (17, 14), (18, 14), (19, 14), (20, 12..20 solid wall), (21, 14), (22, 16), (27, 12..13), (27, 15), (28, 8), (28, 13), (29, 7..8), (29, 10..11).
## Open Thoroughfares
- **Central-to-NW S-Bypass (Verified Bidirectional)**: Connects Central Hub (19, 7) to NW Sector (18, 1..3) via (19, 7) <-> (19, 5) <-> (21, 5) <-> (21, 4) <-> (22, 4) <-> (22, 2) <-> (20, 2) <-> (20, 3) <-> (18, 3) <-> (18, 1).
- Row 1 North Bypass: (5..16, 1) and (18, 1).
- Row 3 West Corridor: (3..9, 3) open continuous floor; connects Ladder E at (9, 1) via Row 1 West (3, 1) -> (3, 3) -> Row 3 East (9, 3) -> Column 9 South (9, 5) -> Row 5 East (13, 5).
- Column 13 North-South transit: (13, 1..6) connects Row 1 to Row 5/6.
- Row 5 Highway: West segment (1..7, 5) and East segment (9..16, 5), connected to Row 3 via Column 9 (9, 3..5) around rock at (8, 4..5).
- Column 23 Corridor: (23, 7..11) connects Ladder B landing at (22, 7) to Row 11 East corridor.
- Row 11 Corridor: (17..23, 11) connects Column 17 to Column 23.
- Row 13 Corridor: (17..22, 13) connects Column 17 to Column 21/22.
- Column 21-22 South S-Connector: (22, 13..15) -> (21, 15..17) leads to SE dead-end at (21..27, 17); blocked west by Column 20 rock wall.
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
- **2F NW / SW Sector Isolation**: Ladder A1 at 2F (1, 3) and the western sector (cols 0..7, rows 4..17) are completely isolated from the 2F North Sector (Row 1/3) and South Sector (cols 14..28). Physical access to 2F (1, 3) and the SW sector is solely via 1F transit.
- **Column 16 Barrier (Verified Turn 42288)**:
  - Column 16 runs south from (16, 3..7), but (16, 8) is solid purple rock blocking direct access down to Row 9.
- **South-West Ledge Dead-End (Verified Turn 42387 & 42481)**:
  - The 1F South-Western Ridge (cols 1-6, rows 8-12) accessed via South Ramp at (1, 13) contains NO ladder or warps. Tile (3, 11) on 1F is regular cave floor.
  - The only 4 ladders between 1F and 2F are Ladder B (22, 6 <-> 23, 7), Ladder C (19, 7 <-> 18, 9), Ladder D (29, 1 <-> 27, 1), and Ladder E (9, 1 <-> 7, 1).
  - The fifth ladder in Cerulean Cave is at 1F (1, 3), which leads directly to B1F.
- Verified Rock Collisions: (12, 2..4) is a solid vertical rock column blocking transit between col 11 and col 13 on rows 2-4.
- Verified Rock Collisions: (17, 2..8) and (16, 2) are solid purple rock walls. Passage from Column 16 to Column 18 runs solely via Row 1: (15, 3) -> (15, 1) -> (17, 1) -> (18, 1).
- **Ladder D Isolated Pocket (Verified Turn 42807)**: Ladder D at 2F (29, 1) leads only to an isolated dead-end hook: (29, 1) <-> (28, 1..3) <-> (29, 3..5). All surrounding tiles (28, 4..5), (29, 6), etc. are solid rock. It has NO connection to the main 2F network.