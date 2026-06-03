# Safari Zone West Exploration Scratchpad (Run 13 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 13 Start Turn**: Turn 49651.

## Current Status
- Currently standing at (3, 4) in Map 0_156 (Safari Zone Gatehouse) on Turn 49654.
- Preparing to start Safari Zone Run 13 (¥84317 remaining).

## Structure for Map 0_219 (Safari Zone West):
### VERIFIED GROUND CONSTRAINTS (PROVEN EMPIRICALLY):
- Column 1 Row 15 & 14 are completely blocked by solid tree walls (TYPE_2889).
- Column 0 Row 16 is completely blocked by western map boundary wall.
- Columns 2 & 3 Row 13 are blocked by water (TYPE_4e8c) (Proven on Turn 49498 by physical bump from 2, 14 to 2, 13).
- Row 0/1/2 Columns 24-25 are blocked by solid tree walls (TYPE_2889) (Proven on Turn 49548 by physical bump).
- Column 24 Rows 1-12 are 100% blocked by solid tree walls (TYPE_2889).
- Row 6 Columns 11-16 on the plateau are completely blocked to the North by solid cliff walls.
- Row 25 is completely blocked by a solid wall of trees across Columns 11-15 and 18-29 (proven on Turn 49102).

### RUN 13 OPTIMIZED PATH (500 STEPS BUDGET):
- **Phase 1: Enter Safari Zone Center (Map 0_220) at (15, 25)**
- **Phase 2: Traverse Center to East (Map 0_217)**
- **Phase 3: Traverse Safari Zone East (Map 0_217) to Safari Zone North (Map 0_218)**
- **Phase 4: Traverse Safari Zone North (Map 0_218) to Safari Zone West (Map 0_219)**
- **Phase 5: Backtrack across West Plateau to Southwest Ground Level (6, 20)**
  - Walk Down the eastern corridor to (25, 18).
  - Walk Left to (21, 18).
  - Climb the stairs at (21, 17) to (21, 16).
  - Walk Left across the plateau to (6, 16).
  - Walk Down to descend the western stairs at (6, 19) to (6, 20).
- **Phase 6: Re-verify Northwest Ground Passage & Retrieve Items**
  - Walk to (6, 20) and re-evaluate the southwest-northwest connection.
  - Re-verify if Column 2 Row 13 water or Column 1 Row 14/15 trees are passable.
  - Walk to the northern ground level, collect the Warden's Gold Teeth at (19, 7) or (9, 7), and visit the Secret House at (3, 3) to get HM03 Surf.

## Systematic Western Blockage Testing Protocol (Run 13)
- Once we reach Southwest ground level (6, 20):
  1. Test Column 1: Walk to (1, 16), face Up, and walk Up onto (1, 15), then (1, 14), then (1, 13). Check if these cosmetic tree tiles are passable.
  2. Test Column 2: Walk to (2, 14), face Up, and walk Up onto (2, 13). Check if water has no collision or is passable.
  3. Log coordinates and collision results to find the open path to the Northwest.