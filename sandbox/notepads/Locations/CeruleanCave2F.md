# Cerulean Cave (Unknown Dungeon) 2F - Layout & Topology

## Overview
- Upper floor maze of Cerulean Cave (Unknown Dungeon).
- Consists of isolated elevated sectors connected to 1F via multiple ladders.
- Contains the descending ladder (Ladder A) to B1F (Mewtwo) located in the Western Sector at (1, 3).

## Verified Landmarks & Sector Topology (2F)
1. **Ladder B**: Located at (22, 6) <-> 1F (23, 7). Central sector.
2. **Ladder C**: Located at (19, 7) <-> 1F (18, 9). Central sector.
3. **Ladder D**: Located at (29, 1) <-> 1F (27, 1). Northeast alcove / Eastern corridor.
4. **Ladder E**: Located at (9, 1) <-> 1F (7, 1). Northwest elevated plateau (rows 0-5, cols 3-18).
5. **SW Ladder**: Located at (3, 11) <-> 1F (3, 11). Southwest Sector entrance leading to Western Corridor.
6. **Ladder A (to B1F Mewtwo)**: Descending ladder to B1F located in western corridor at (1, 3). Accessible via Western Corridor (cols 0-1).

## Verified Sector Structure & Collisions (2F)
- **Northwest Plateau (Ladder E 9, 1)**: Spans rows 0-5, cols 3-18.
- **Path to Ladder A (1, 3)**: From Northwest Plateau, route is (9, 1) -> west along Row 1 to (5, 1) -> (5, 3) -> (6, 3..5) -> Row 5 west through (6..0, 5) -> Column 0 north through (0, 5..3) -> Right onto Ladder A at (1, 3) [Empirically Verified Turn 55198].
- **Eastern Corridor (Ladder D 29, 1)**: Runs south through (29, 1..6) -> (27, 6..7) -> (25, 7..9) -> (26, 9..14) -> (28, 14..16) -> (27, 16..17).
- **Southern Crossover (Rows 11-17)**: (27, 17) -> (21, 17) -> (21, 15) -> (22, 13) -> (17, 13) -> (17, 11) -> (16, 11).
- **Northeast Sector (Ladder D 29, 1)**: Connects down to 1F Northern Mainland at (27, 1). Note: (28, 4) and (29, 2) are solid barriers; movement west across the upper rows is blocked on 2F.
- **Verified Barriers**: (20, 14..17) prevents direct westward passage along Row 17; routing requires looping through (22, 13) and Row 9.