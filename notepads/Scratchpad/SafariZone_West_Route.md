# Safari Zone West Exploration Scratchpad (Run 9 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 9 Start Turn**: Turn 46938 (Start Time: Tuesday, June 2, 2026).

## Current Status
- Standing at (10, 15) on the ground level in Safari Zone West (Map 0_219) on Turn 47948. Exactly 202 remaining steps (500 minus 298 overworld steps taken).

## Chronological Exploration History & Discoveries (Archive):
- **Safari Zone East (Map 0_217) Exit Route Plan (ARCHIVED - COMPLETED)**: 
  - Successfully completed on Turn 47713. Bypassed central plateau using ground Row 5, transitioning with 0 wild encounters.
- **Safari Zone North (Map 0_218) Active Progress & Route (ARCHIVED - COMPLETED)**: 
  - Walked West along Row 31 (a grass-free, open horizontal corridor) from Column 39 to Column 28.
  - Walked Up onto the Western Plateau via the stairs at (22, 23) and crossed West to Column 16, then walked Down to ground level at (16, 28).
  - Walked West along Row 28/30 to Column 9, then walked South to transition into Safari Zone West at (9, 35) on Turn 47775.

## Safari Zone West (Map 0_219) Active Route & Plan:
- **Phase 1 (Stairs UP)**: Walk West along Row 18 from Column 27 to Column 21, then walk Up to (21, 17) to climb the stairs onto the plateau. (Completed!)
- **Phase 2 (Plateau Crossing)**: Climb stairs at (6, 19) to (6, 18), cross East to (16, 18), cross North to (16, 6), cross West to (12, 6), and walk Up to (12, 5) to descend to the northern ground level. (Active!)
- **Phase 3 (Ground Navigation to target)**: From (12, 5) on the ground, navigate to find the Warden's Gold Teeth and the Secret House (3, 3) to get HM03 Surf.

### Step-by-Step Path to Northwest Ground via Plateau from (6, 19):
- (6, 19) -> Up -> (6, 18) (climb onto plateau, TYPE_2770)
- (6, 18) -> Right x10 -> (16, 18) (plateau ground, TYPE_2770)
- (16, 18) -> Up x12 -> (16, 6) (plateau ground, TYPE_2770)
- (16, 6) -> Left x4 -> (12, 6) (plateau northern stairs, TYPE_2770/TYPE_4b8d)
- (12, 6) -> Up -> (12, 5) (descend onto northwest ground, TYPE_3fe2)

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

## Structure for Map 0_219 (Safari Zone West):
### VERIFIED GROUND CONSTRAINTS (PROVEN EMPIRICALLY):
- Column 1 Row 15 & 14 are completely blocked by solid tree walls (TYPE_2889).
- Column 0 Row 16 is completely blocked by western map boundary wall.
- Columns 2 & 3 Row 13 are blocked by water (TYPE_4e8c).
- Column 24 Rows 1-12 are 100% blocked by solid tree walls (TYPE_2889).
- Row 6 Columns 12-16 on the plateau are completely blocked to the North by solid cliff walls.

### ACTIVE ON-FOOT NAVIGATION PATHS (UNVERIFIED):
- Northwest area containing Warden's Gold Teeth and Secret House is accessible ONLY via the southern elevated plateau route (stairs at 21, 17).

## Ground-Level Re-verification Plan in Safari Zone West (Map 0_219):
- **Objective**: Systematically and unambiguously re-verify the passability of Column 2 and Column 3 on Row 13 to prove or disprove any hidden passage.
- **Protocol**:
  1. Navigate to the southwest ground level and stand at (3, 14) on the flat ground.
  2. Face North and attempt to walk Up to (3, 13).
     - **Result (Turn 47826)**: Pressed "Up" from (3, 14). Resulted in a direct collision and zero movement. Player remained at (3, 14). This empirically proves that (3, 13) of TYPE_4e8c (water) has solid, impassable collision on foot.
  3. Walk Left to (2, 14) on the flat ground.
  4. Face North and attempt to walk Up to (2, 13).
     - **Result (Turn 47846)**: Pressed "Up" from (2, 14). Resulted in a direct collision and zero movement. Player remained at (2, 14). This empirically proves that (2, 13) of TYPE_4e8c (water) has solid, impassable collision on foot.
  5. Formally log the exact coordinate, button pressed, and outcome (including any specific tile visual/behavioral changes) in the scratchpad. This will serve as absolute proof of work.