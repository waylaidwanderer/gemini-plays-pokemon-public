# Safari Zone West Exploration Scratchpad (Run 9 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 9 Start Turn**: Turn 46938 (Start Time: Tuesday, June 2, 2026).

## Current Status
- Standing at (26, 33) in Safari Zone North (Map 0_218) on Turn 47741. Exactly 379 remaining steps (500 minus 121 overworld steps taken).

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

## Safari Zone East (Map 0_217) Exit Route Plan (ARCHIVED - COMPLETED):
- Successfully completed on Turn 47713. Bypassed central plateau using ground Row 5, transitioning with 0 wild encounters.

## Safari Zone North (Map 0_218) Active Progress & Route:
- **Plan**: Walk West along Row 33 to Columns 8-9, then go South to transition into Safari Zone West at (9, 35).
- **Row 33 Empirical Verification Protocol**:
  - As we walk West on Row 33, we will verify passability of each tile step-by-step.
  - Check for any unexpected collision on Columns 27 to 9. If a collision occurs, log the blocked coordinates immediately.
  - Check the screen to ensure we only step on tall grass at Columns 26 and 25 (the only known grass on this route).
- **Step-by-Step Coordinates**:
  - (28, 33) -> Left -> (27, 33) (ground, TYPE_3fe2)
  - (27, 33) -> Left -> (26, 33) (tall grass, TYPE_fed7)
  - (26, 33) -> Left -> (25, 33) (tall grass, TYPE_fed7)
  - (25, 33) -> Left to Column 9 (ground, TYPE_3fe2)

## Structure for Map 0_219 (Safari Zone West):
### VERIFIED GROUND CONSTRAINTS (PROVEN EMPIRICALLY):
- Column 1 Row 15 & 14 are completely blocked by solid tree walls (TYPE_2889).
- Column 0 Row 16 is completely blocked by western map boundary wall.
- Columns 2 & 3 Row 13 are blocked by water (TYPE_4e8c).
- Column 24 Rows 1-12 are 100% blocked by solid tree walls (TYPE_2889).
- Row 6 Columns 12-16 on the plateau are completely blocked to the North by solid cliff walls.

### ACTIVE ON-FOOT NAVIGATION PATHS (UNVERIFIED):
- Northwest area containing Warden's Gold Teeth and Secret House is accessible ONLY via the southern elevated plateau route (stairs at 21, 17).

## Socratic Quest Answers & Action Plans (Turn 47677):
### 1. Route through Safari Zone North (Map 0_218):
- **Entry**: Enter from Safari Zone East (0, 5) into Safari Zone North (39, 31) (the isolated eastern basin).
- **Step 1**: Walk West along Row 31 (a grass-free, open horizontal corridor) from Column 39 to Column 28.
- **Step 2**: Continue West along Row 33 (which connects the eastern and western ground areas below the central plateau) from Column 28 to Column 9.
- **Step 3**: Walk South from (9, 33) to (9, 35) through the open gap at Columns 8-9 (bypassing the solid building roof at (18, 34)).
- **Step 4**: Take the map transition South at (9, 35) to enter Safari Zone West (Map 0_219) at (27, 0).

### 2. Ground-Level Re-verification Plan in Safari Zone West (Map 0_219):
- **Objective**: Systematically and unambiguously re-verify the passability of Column 2 and Column 3 on Row 13 to prove or disprove any hidden passage.
- **Protocol**:
  1. Navigate to the southwest ground level and stand at (3, 14) on the flat ground.
  2. Face North and attempt to walk Up to (3, 13).
     - Record result: coordinates change to (3, 13) [PASSABLE] or collision occurs [BLOCKED].
  3. Walk Left to (2, 14) on the flat ground.
  4. Face North and attempt to walk Up to (2, 13).
     - Record result: coordinates change to (2, 13) [PASSABLE] or collision occurs [BLOCKED].
  5. Formally log the exact coordinate, button pressed, and outcome (including any specific tile visual/behavioral changes) in the scratchpad. This will serve as absolute proof of work.