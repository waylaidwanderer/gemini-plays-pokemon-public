# Cerulean Cave (Unknown Dungeon) 2F - Layout & Notes

## Connected Component Graph (2F)
- **2F Partitioned Maze Structure**: 2F is divided into distinct sectors separated by solid rock barriers:
  1. **West Sector (cols 1..9, rows 0..5)**: Reachable via Ladder E at (9, 1) <-> 1F (7, 1). Contains Ladder A at (1, 3), which descends directly to B1F (Mewtwo).
  2. **Central Sector (cols 11..21, rows 1..10)**: Reachable via Ladder C at (19, 7) <-> 1F (18, 9). Contains S-Bypass and Row 1 East corridor (11..18, 1).
  3. **Southeast Sector (cols 21..29, rows 6..19)**: Reachable via Ladder B at (22, 6) <-> 1F (23, 7). Contains Column 23, Row 11, Column 24/28, Row 17 South Artery, and PP Up at (29, 9).
  4. **NE Pocket (col 29, rows 1..5)**: Reachable via Ladder D at (29, 1) <-> 1F (27, 1). Isolated dead-end landing.

## Regional Barriers & Collisions (2F)
- **Northern Boundaries (Rows 0..5)**:
  - Column 10 Barrier: Solid rock along (10, 0..5) separating West Sector from Central Sector across rows 0-5.
  - Column 2 Barrier: (2, 0..4) is continuous solid rock.
  - Row 2/4 Barriers: (5..10, 2), (12, 2..4), (14, 2..4), (17, 2..8) are solid rock.
  - Row 4 West Barrier: (1..8, 4) is continuous solid rock wall.
- **Central & Middle Barriers (Rows 6..10)**:
  - Row 6 Barrier: (5..14, 6), (15, 6), (17, 6), (21, 6), (23, 6) are solid rock.
  - Row 8 Barrier: (16..22, 8), (24, 8..10), (28, 8) are solid rock blocking direct passage between Ladder C and southern rows.
  - Row 10 Barrier: (13..19, 10), (22, 8..10), (25, 10..11) are solid rock.
- **Southern Boundaries (Rows 11..19)**:
  - Column 14 Barrier: (14, 14..16) is solid rock blocking direct south passage on Col 14.
  - Column 20 Wall: (20, 12..19) is a solid continuous rock wall.
  - Row 16 Barrier: (14..20, 16) is solid rock. Pocket at (15..19, 15) has rock at (14, 15) and (20, 15).
  - Row 17 South Artery: (21..28, 17) connects Column 21 to Column 28.
  - Column 28/29 Pocket: (29, 7..8), (29, 10..11), (28, 13), (27, 12..13), (27, 15) are solid rock.

## Open Thoroughfares (2F)
- **Central-to-NW S-Bypass (Verified Bidirectional)**: Connects Central Hub (19, 7) to NW Sector (18, 1..3) via (19, 7) <-> (19, 5) <-> (21, 5) <-> (21, 4) <-> (22, 4) <-> (22, 2) <-> (20, 2) <-> (20, 3) <-> (18, 3) <-> (18, 1).
- **Row 1 North Bypass**: (5..16, 1) and (18, 1).
- **Row 3 West Corridor**: (3..9, 3) open continuous floor; connects to Ladder E at (9, 1) via Column 3 North (3, 3) -> (3, 1) -> Row 1 East (4..9, 1).
- **Column 13 Corridor**: (13, 1..5) connects Row 1 to Row 5.
- **Column 23 Corridor**: (23, 7..11) connects Ladder B landing at (22, 7) to Row 11 East corridor.
- **Row 11 Corridor**: (14..23, 11) connects Column 14/15 to Column 23.
- **Row 13 Corridor**: (17..22, 13) connects Column 17 to Column 21/22.
- **Column 21-22 South S-Connector**: (22, 13..15) -> (21, 15..17) connects Row 13 to Row 17 Artery.

## Verified Items (2F)
- Item Pokéball at (29, 9) collected (PP Up).
- Item Pokéball at (13, 6) collected (Max Potion).
- Item Pokéball at (4, 15) collected (TM14 Blizzard).

## Wild Encounters (2F)
- Ditto, Chansey, Venomoth, Kadabra, Dodrio, Rhydon, Electrode, Marowak, Wigglytuff.
