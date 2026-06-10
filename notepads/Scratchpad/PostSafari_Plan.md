# Post-Safari Zone Route & Progression Plan

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 75675)
- **Active Exploration Mission**: Locate and retrieve the Secret Key.
- **Switch Matrix (State A vs. State B)**:
  - We have toggled Statue 2 (2F, (2, 11)) back to **State A** (Default) on Turn 77818.
  - State A: Gate 1 on 1F (25, 13) is CLOSED, blocking foot access to the Southeast room.
  - State A: Gate 3 on 2F (18, 8)-(19, 8) is OPEN.
  - State A: Gate 4 on 1F East (21, 17) is OPEN.
  - State A: Gate 6 on 2F (9, 4)-(9, 5) is CLOSED.

## Cinnabar Gym Blaine Matchup Preparation Strategy
- **South-Central 1F Pocket Inaccessibility (Turn 77316)**: Under State A, the south-central pocket of 1F (Rows 18-27, Columns 21-23) is completely inaccessible on foot from the rest of 1F due to Column 11 and Row 13 walls being solid TYPE_2889.
- **The B1F Balcony Drop Plan Checklist**:
  - [x] Step 1: Systematically test the 2F West southwest balcony railings (Rows 16 and 17) for active jump-down ledges under State B.
  - [x] Step 2: If State B yields only bumps, backtrack to 2F West (2, 11) and toggle Mewtwo Statue 2 back to **State A** (Default).
  - [x] Step 3: Systematically test the 2F West southwest balcony railings under **State A** to find any active jump-down ledges. (Result: All 4 columns are solid).
  - [x] Step 4: Systematically test the 3F West southwest balcony railings (Row 17, Columns 1 to 5) under **State A** to find any active jump-down ledges! (Result: All 5 columns are 100% solid, impassable railings).
## State A 3F Gate 2 Crossover Analysis & Final Pit A Discovery (Turn 78058)
- **Visual Breakdown of 3F West/East Gate 2**:
  - In State B, Row 8 at Columns 8, 9, 10, 11 consists of closed electronic gates (`TYPE_2889`) represented visually by gold horizontal bars. This completely blocks vertical passage from Row 9 to Row 7.
  - Column 10 is solid rubble (`TYPE_2889`) on Rows 9 to 15, preventing horizontal crossing.
- **The State A Crossover Hypothesis**: Under **State A** (Default), we hypothesize that the electronic gate on Row 8 Columns 8, 9, 10, 11 opens and becomes passable floor (`TYPE_3fe2`). If true, this will unlock direct vertical traversal from 3F West Row 9 (Columns 8 or 9) UP to Row 7.
  - If the hypothesis holds, we can cross horizontally along the Row 7 corridor to Column 12 (3F East), walk vertically down Column 12 to (12, 12) (Pit A), and drop down to reach B1F!
- **Action Plan**:
  1. Descend the stairs at (7, 10) on 3F West to land on 2F West at (7, 11).
  2. Walk Left horizontally along Row 11 to Mewtwo Statue 2 at (2, 11) on 2F West.
  3. Toggle Statue 2 back to **State A** (Default).
  4. Walk Right horizontally along Row 11 back to (7, 11) and climb UP the stairs at (7, 10) to land on 3F West at (7, 11).
  5. On 3F West (now under State A), walk to Column 8 or 9 on Row 9, walk UP onto Row 8 (gate is open!), and cross horizontally along Row 7 to Column 12 (3F East).
  6. Walk Down Column 12 to (12, 12) and fall down Pit A to land on B1F!