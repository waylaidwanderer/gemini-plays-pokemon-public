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
   - Row 1 North Bypass (cols 11..24, row 1) connects Column 24 directly west to Northwest Sector.
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
- Column 24 Corridor: Open vertical floor across (24, 1..15) connecting Row 15 to Row 1 North Bypass.
- Row 11 Thoroughfare: cols 14..24 are open cave floor connecting Ladder B sector to Column 24.
- Row 10 Barrier: Solid rock wall across cols 13..22.
- Row 16 Barrier: Solid rock wall across cols 14..20.
- Columns 16-18 Barrier at Row 8: (16..18, 8) are solid rock walls blocking direct northward passage from Row 9.
- Row 1 North Bypass: Continuous open floor across cols 3..24 at Row 1 leading straight to Ladder A chamber.