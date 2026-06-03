# Safari Zone West Exploration Scratchpad (Run 8 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).

## Current Status
- Standing at (25, 7) in Safari Zone West (Map 0_219) on Turn 47097. Exactly 306 remaining steps (500 minus 194 overworld steps taken).

## Column 24 Gap Testing Protocol Details (Socratic Quest Resolution):
- **Testing Plan to systematically verify Column 24 on Rows 1-12 without skipping or duplicating**:
  1. Position at (25, 12) (the eastern ground corridor).
  2. For Y = 12 down to 1:
     - Stand at (25, Y).
     - Press Left.
     - If coordinates change to (24, Y), Row Y is PASSABLE. Step Right back to (25, Y).
     - If collision is received and coordinates remain (25, Y), Row Y is BLOCKED.
     - Walk Up 1 step to (25, Y-1) to prepare for the next row.
  3. This ensures 100% systematic, non-redundant testing and absolute coordinate-based verification of every potential gap.

## Chronological Exploration History & Discoveries:
- **Hypothesis M (Eastern Plateau Northern Descent) - DISPROVEN**: 
  - On Turns 46798-46814, we systematically tested the northern cliff edge of the eastern plateau on Rows 13-14 for Columns 18-22 and found 100% solid cliff-wall collision. Hypothesis M is definitively false.
- **Plateau Central Northern Edge (Row 6 Blockage) - DISPROVEN**:
  - On Turns 46615-46651, we systematically tested Row 6 Columns 11-16 and found them to be completely blocked to the North by solid cliff walls. There is no central plateau northern descent.
- **Southwest Ground Level Bypass - DISPROVEN**:
  - On Turns 46874-46882, we descended to the southwest ground level at (6, 20) and walked along Column 1. 
  - We discovered a major breakthrough: Column 1 tree tiles are actually TYPE_3fe2 and have ZERO active collision from Row 16 down to Row 23!
  - However, we proved that Column 1 is completely blocked to the North at Row 15 (1, 15) and Row 14 (1, 14) by solid tree walls (TYPE_2889).
  - Column 0 is also blocked at Row 16 (0, 16) by solid tree/border walls.
  - Thus, there is no direct ground-level pathway along the west edge between the southwest and northwest quadrants.

## Hypothesis N: Eastern Corridor Column 24 Gaps (Active Run 8 Objective)
- **Hypothesis**: There is a hidden, passable gap in Column 24's tree line on Rows 1-12, allowing us to walk West from the eastern ground corridor into the northern ground corridor, bypassing the plateau route entirely.
- **Systematic Foot Testing Plan**:
  1. Complete gatehouse payment and enter Safari Zone Center (Map 0_220).
  2. Follow the optimized path to Safari Zone West (Map 0_219) via Safari Zone Center -> East -> North -> West (Eastern Corridor).
  3. Walk North along Column 25 (the eastern corridor) from Row 18 up to Row 1.
  4. On every single Row from Row 12 up to Row 1, face Left and attempt to walk Left into Column 24 to check for any passable gaps.
  5. Formally record the outcome (pass/collision) for every row tested in this scratchpad.

## Systematic Row-by-Row Passability Log for Column 24:
- Row 12: [X] Blocked (Verified on Turn 47082)
- Row 11: [X] Blocked (Verified on Turn 47084)
- Row 10: [X] Blocked (Verified on Turn 47087)
- Row 9:  [X] Blocked (Verified on Turn 47089)
- Row 8:  [X] Blocked (Verified on Turn 47091)
- Row 7:  [X] Blocked (Verified on Turn 47095)
- Row 6:  [X] Blocked (Verified on Turn 47100)
- Row 5:  [ ] Untested
- Row 4:  [ ] Untested
- Row 3:  [ ] Untested
- Row 2:  [ ] Untested
- Row 1:  [ ] Untested

## Mathematically Optimized Routing for Run 8:
1. **Safari Zone Center**: Walk East to (29, 10) [21 steps] -> transition to Safari Zone East.
2. **Safari Zone East**: Walk East to Column 28, then North along Column 28. Climb the high plateau at (24, 15), walk across to the West side, and climb down the stairs at (12, 21). Walk North along Column 10/9 (grass-free) to Row 8, then East to (12, 8), and climb the northern stairs at (12, 7) onto the northern plateau. Walk East to Column 21, then North to the northeast corridor, exiting at (0, 5) -> transition to Safari Zone North (39, 31) [~55 steps].
3. **Safari Zone North**: Walk West along the grass-free southern corridor (Row 33/31) to (9, 35) -> transition to Safari Zone West (27, 0) [52 steps].
4. **Safari Zone West**: Walk South along Column 25 and begin the Column 24 Gap Testing Protocol.