# Cerulean Cave (Unknown Dungeon) 2F - Layout & Topology

## Overview
- Upper floor maze of Cerulean Cave (Unknown Dungeon).
- Connects to 1F via multiple ladders and contains the sole descending ladder (Ladder A) to B1F (Mewtwo).

## Connected Component Graph & Routing
1. **Southeast Sector**:
   - Ladder B at (22, 6) <-> 1F (23, 7).
   - South Artery (Row 17, cols 21..28) connects Ladder B to Ladder D at (29, 1).
   - Ladder D at (29, 1) descends to 1F NE Terrace (27, 1), which has a water ramp at (23, 3) leading into the 1F water canal.

2. **Central Sector & Bypass Network**:
   - Ladder C at (19, 7) <-> 1F (18, 9) (Central Corridor / 1F Water Ramp at (17, 15)).
   - Row 1 North Bypass (cols 11..18, row 1) connects Column 15/16 to Column 18/19 and Row 3 (18..20, 3) -> Column 22/23.
   - Row 11 Thoroughfare (cols 12..23, row 11) connects the Southeast Artery (col 23) to Column 12 (12, 11).

3. **West Sector & Route to Ladder A (B1F Mewtwo)**:
   - Ladder E at (9, 1) <-> 1F Northern Terrace (7, 1) (accessed by surfing the 1F water canal and disembarking at water ramp (15, 3)).
   - Northwest loop: (9, 1) -> Row 1 West to (3, 1) -> (3, 3) -> Row 3 East to (9, 3) -> (9, 5) -> Row 5 East.
   - Pathway to Ladder A:
     - Accessible via the Row 9 thoroughfare leading west into Column 0, which connects north directly to Ladder A at (1, 3). Ladder A descends to B1F (Mewtwo's chamber).

## Verified Ladders (2F)
1. **Ladder A**: Located at (1, 3) -> Descends to B1F (Mewtwo).
2. **Ladder B**: Located at (22, 6) <-> 1F (23, 7).
3. **Ladder C**: Located at (19, 7) <-> 1F (18, 9).
4. **Ladder D**: Located at (29, 1) <-> 1F (27, 1).
5. **Ladder E**: Located at (9, 1) <-> 1F (7, 1).

## Verified Items (2F)
- Item Pok� Ball at (29, 9) collected (PP Up).
- Item Pok� Ball at (13, 6) collected (Max Potion).
- Item Pok� Ball at (4, 15) collected (TM14 Blizzard).

- Column 24 Corridor: Open vertical floor across (24, 11) to (24, 15) [Verified Turn 46363].
- Central/South Branches: (14, 11..13), (15, 13..15), and Row 15 (cols 15..19) verified open floor [Turn 46387].
- Row 8 Obstacle: Solid rock wall at (24, 8) blocks eastward traversal from (23, 8) [Turn 46406].
- Verified Pathway to South Artery: From Row 11 (18, 11) -> Left to (17, 11) -> Down to (17, 13) -> East across Row 13 to (22, 13) -> Down to (22, 15) -> Left to (21, 15) -> Down to (21, 17) [South Artery].
- Empirical Barrier & Wall Coordinates (West Sector):
  - (15, 7): Rock wall (blocks westward traversal along Row 7 from (16, 7)).
  - (9, 6) & (10, 6): Rock walls (blocks southward traversal from (9, 5)/(10, 5) towards Row 6/7).
  - (2, 3): Rock wall (blocks westward traversal from (3, 3) along Row 3).
  - (2, 1): Rock wall (blocks westward traversal from (3, 1)).
  - (3, 4): Rock wall (blocks southward traversal from (3, 3) along Column 3).
  - (12, 6): Rock wall (blocks southward traversal from (12, 5) along Column 12).
  - (20, 4): Rock wall (blocks southward traversal from (20, 3) along Column 20).
  - (27, 4): Dead-end alcove (walls at (27, 3), (27, 5), and (28, 4); open only to west at (26, 4)).
  - (7, 4): Rock wall (blocks southward traversal from (7, 3) along Column 7).
  - (6, 4): Rock wall (blocks southward traversal from (6, 3) along Column 6).
  - (5, 4): Rock wall (blocks southward traversal from (5, 3) along Column 5).
  - (4, 4): Rock wall (blocks southward traversal from (4, 3) along Column 4).
  - Row 4 barrier: (2..8, 4) are all rock walls; Row 1..3 West (cols 3..9) connects only via (9, 4) -> (9, 5).
  - (17, 4): Rock wall (blocks eastward traversal from (16, 4) along Row 4).
  - (23, 3): Rock wall (blocks southward traversal from (23, 2) along Column 23).
  - (24, 6): Rock wall (blocks southward traversal from (24, 5) along Column 24).
  - (22, 5): Rock wall (blocks southward traversal from (22, 4) along Column 22 to Ladder B).
  - Path to Ladder C (19, 7): From (22, 4) -> Left 2 to (20, 4) -> Down 2 to (20, 6) -> Left 2 to (18, 6) -> Down 1 to (18, 7) -> Right 1 onto Ladder C at (19, 7).
  - (18, 8): Rock wall (blocks southward traversal from (18, 7) along Column 18).