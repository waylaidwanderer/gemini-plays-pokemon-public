# Safari Zone West Exploration Scratchpad (Run 8 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).

## Current Status
- Standing at (16, 28) in Safari Zone North (Map 0_218) on Turn 47142. Exactly 297 remaining steps (500 minus 203 overworld steps taken).

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
- Row 5:  [X] Blocked (Verified on Turn 47102)
- Row 4:  [X] Blocked (Verified on Turn 47104)
- Row 3:  [X] Blocked (Verified on Turn 47105)
- Row 2:  [X] Blocked (Verified on Turn 47108)
- Row 1:  [X] Blocked (Trivially blocked; Column 25 Row 1 is solid TYPE_2889 and Column 24 Row 1 is solid TYPE_2889)

## Mathematically Optimized Routing for Run 8 (Refactored):
- Since both the southwest and southeast ground-level passages are blocked, we must use the Western Plateau route.
- **Step 1 (Active)**: Climb the stairs at (16, 27) onto the Western Plateau of Safari Zone North.
- **Step 2**: Walk West across the northern plateau into Safari Zone West's northern plateau.
- **Step 3**: Walk across Safari Zone West's plateau and find the staircase down to the northwest ground level.
- **Step 4**: Retrieve the Gold Teeth and enter the Secret House for HM03 Surf.