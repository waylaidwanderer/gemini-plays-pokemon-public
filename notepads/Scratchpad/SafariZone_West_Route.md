# Safari Zone West Exploration Scratchpad (Run 12 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 12 Start Turn**: Turn 49165.

## Current Status
- Currently standing at (17, 14) on Map 0_218 (Safari Zone North) on Turn 49353.
- Exactly 335 overworld steps remaining (165 overworld steps taken in Run 12).

## Structure for Map 0_219 (Safari Zone West):
### VERIFIED GROUND CONSTRAINTS (PROVEN EMPIRICALLY):
- Column 1 Row 15 & 14 are completely blocked by solid tree walls (TYPE_2889).
- Column 0 Row 16 is completely blocked by western map boundary wall.
- Columns 2 & 3 Row 13 are blocked by water (TYPE_4e8c).
- Column 24 Rows 1-12 are 100% blocked by solid tree walls (TYPE_2889).
- Row 6 Columns 11-16 on the plateau are completely blocked to the North by solid cliff walls.
- Row 25 is completely blocked by a solid wall of trees across Columns 11-15 and 18-29 (proven on Turn 49102).

### SAFARI ZONE RUN 12 OPTIMIZED PATH (500 STEPS BUDGET):
- **Phase 1: Enter Safari Zone Center (Map 0_220) at (15, 25)** (Completed on Turn 49176)
- **Phase 2: Traverse Center to East (Map 0_217)** (Completed on Turn 49187)
- **Phase 3: Traverse Safari Zone East (Map 0_217) to Safari Zone North (Map 0_218)** (Completed on Turn 49314)
- **Phase 4: Traverse Safari Zone North (Map 0_218) to Safari Zone West (Map 0_219)** (Active)
  - Current position: (17, 14) [ground level].
  - Planned Route to transition:
    1. Backtrack Down 5 steps to (17, 19).
    2. Walk Right 17 steps to (34, 19).
    3. Walk Up 3 steps to (34, 16) and Up 1 step to (34, 15) to climb onto the Eastern Plateau.
    4. Walk Left 6 steps to (28, 15) and Down 12 steps to (28, 27) (Plateau Stairs DOWN).
    5. Walk Down 1 step to (28, 28) to descend to the ground level of the southern corridor.
    6. Walk Down 3 steps to (28, 31).
    7. Walk Left 19 steps to (9, 31).
    8. Walk Down 4 steps to (9, 35) and transition to Safari Zone West.
- **Phase 5: Collect Gold Teeth and HM03 Surf in Safari Zone West**
  - Walk South along Eastern ground corridor to (25, 18).
  - Walk Left to (21, 18) and climb plateau stairs at (21, 17) to (21, 16).
  - Walk West across plateau via Row 16 to (6, 18), then descend western stairs at (6, 19) to (6, 20) [Southwest ground level].
  - Walk Left to Column 1 or 2 on Row 20, and walk North along Column 1 or 2 on Row 20 to systematically test the ground corridor passability to Row 5 (since North-facing cliff transitions are completely impassable under all circumstances in Gen 1).
  - Walk to (3, 3) for the Secret House, picking up Gold Teeth at (19, 7).