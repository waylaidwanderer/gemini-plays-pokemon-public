# Cerulean Cave (Unknown Dungeon) 2F - Layout & Topology

## Overview
- Upper floor maze of Cerulean Cave (Unknown Dungeon).
- Connects to 1F via multiple ladders and contains the descending ladder (Ladder A) to B1F (Mewtwo).

## Verified Ladders (2F)
1. **Ladder A**: Located at (1, 3) -> Descends to B1F (Mewtwo).
2. **Ladder B**: Located at (22, 6) <-> 1F (23, 7).
3. **Ladder C**: Located at (19, 7) <-> 1F (18, 9) [Isolated 7-tile pocket].
4. **Ladder D**: Located at (29, 1) <-> 1F (27, 1).
5. **Ladder E**: Located at (9, 1) <-> 1F (7, 1) [Northwest Sector entry to Ladder A].

## Planned Master Route to Ladder A (1, 3) -> B1F (via Ladder E Northwest Sector)
- **Floor Identification**: 2F is completely dry with no water tiles. 1F features distinct blue water canals with wave foam across rows 4-5 and 10-11.
- **Master Entry Ladder**: Ladder E at (7, 1) on 1F <-> (9, 1) on 2F.
- **Local Frontier-Exhaustion Protocol from 2F (9, 1)**:
  - Probe Row 1 West: (9, 1) -> (8, 1) -> (7, 1) -> (6, 1) -> (5, 1) -> (4, 1).
  - Probe southward/westward connectors: (4, 1) -> (4, 3) / (3, 3) -> (1, 3) [Ladder A].
  - Systematically test every adjacent tile in the northwest cluster ((3, 3), (2, 3), (1, 3), (0, 3)) using chunked 1-3 step tests.
  - Step into **Ladder A at (1, 3)** to descend to B1F!

## Verified 2F Local Topography (Turn 50616)
- **Column 23 Corridor**: Open north-south path from (23, 7) through (23, 11+).
- **Rock Barrier**: (22, 8..11) is a solid rock wall separating Column 23 from Column 21 on upper rows.
- **Traversal Plan**: When arriving at (22, 6) from Ladder B, use chunked testing (4-6 steps max per chunk) to verify southern passageways and west connections step-by-step.
- **Verified Row 11 & Column 14 Thoroughfares (Turns 50718-50731)**:
  - Row 11 is open from (23, 11) through (14, 11).
  - (16..22, 14) is a solid rock barrier.
  - Column 14 entry is verified at (14, 11). Further southward and westward connections will be verified step-by-step using chunked testing.