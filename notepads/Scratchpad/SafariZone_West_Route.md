# Safari Zone West Exploration Scratchpad (Run 12 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 12 Start Turn**: Turn 49165.

## Current Status
- Currently standing at (26, 0) on Map 0_219 (Safari Zone West) on Turn 49550.
- Exactly 104 overworld steps remaining (396 overworld steps taken in Run 12).

## Structure for Map 0_219 (Safari Zone West):
### VERIFIED GROUND CONSTRAINTS (PROVEN EMPIRICALLY):
- Column 1 Row 15 & 14 are completely blocked by solid tree walls (TYPE_2889).
- Column 0 Row 16 is completely blocked by western map boundary wall.
- Columns 2 & 3 Row 13 are blocked by water (TYPE_4e8c) (Proven on Turn 49498 by physical bump from 2, 14 to 2, 13).
- Row 0/1/2 Columns 24-25 are blocked by solid tree walls (TYPE_2889) (Proven on Turn 49548 by physical bump).
- Column 24 Rows 1-12 are 100% blocked by solid tree walls (TYPE_2889).
- Row 6 Columns 11-16 on the plateau are completely blocked to the North by solid cliff walls.
- Row 25 is completely blocked by a solid wall of trees across Columns 11-15 and 18-29 (proven on Turn 49102).

### SAFARI ZONE RUN 12 OPTIMIZED PATH (500 STEPS BUDGET):
- **Phase 1: Enter Safari Zone Center (Map 0_220) at (15, 25)** (Completed on Turn 49176)
- **Phase 2: Traverse Center to East (Map 0_217)** (Completed on Turn 49187)
- **Phase 3: Traverse Safari Zone East (Map 0_217) to Safari Zone North (Map 0_218)** (Completed on Turn 49314)
- **Phase 4: Traverse Safari Zone North (Map 0_218) to Safari Zone West (Map 0_219)** (Completed on Turn 49445)
- **Phase 5: Backtrack across Plateau to Row 0 Corridor** (Completed on Turn 49530)
- **Phase 6: Traverse Eastern Ground Corridor (Column 23)**
  - From (26, 0), walk Down to (26, 2) and Left to (25, 2).
  - Walk Down Column 25 to (25, 18) (grass-free).
  - Walk Left to Column 23 on Row 18.
  - Walk UP Column 23 to Row 3 (grass-free).
- **Phase 7: Walk West along Row 3 to Secret House (3, 3) and Gold Teeth (19, 7)**
  - Walk Left along Row 3 to (3, 3) to collect HM03 Surf in Secret House.
  - Collect Gold Teeth at (19, 7).