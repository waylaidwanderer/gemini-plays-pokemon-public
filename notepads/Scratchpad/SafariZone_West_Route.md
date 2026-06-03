# Safari Zone West Exploration Scratchpad (Run 11 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 12 Start Turn**: Turn 49165.

## Current Status
- Run 12 starting! Standing in Safari Zone Gatehouse (Map 0_156) at (4, 2) on Turn 49165.
- Exactly 500 overworld steps remaining. Run 12 is beginning!

## Structure for Map 0_219 (Safari Zone West):
### VERIFIED GROUND CONSTRAINTS (PROVEN EMPIRICALLY):
- Column 1 Row 15 & 14 are completely blocked by solid tree walls (TYPE_2889).
- Column 0 Row 16 is completely blocked by western map boundary wall.
- Columns 2 & 3 Row 13 are blocked by water (TYPE_4e8c).
- Column 24 Rows 1-12 are 100% blocked by solid tree walls (TYPE_2889).
- Row 6 Columns 11-16 on the plateau are completely blocked to the North by solid cliff walls.
- Row 25 is completely blocked by a solid wall of trees across Columns 11-15 and 18-29 (proven on Turn 49102).

### SAFARI ZONE RUN 12 OPTIMIZED PATH (500 STEPS BUDGET):
- **Phase 1: Enter Safari Zone Center (Map 0_220) at (15, 25)**
- **Phase 2: Traverse Center to East (Map 0_217)**
  - Path: Right to Column 29, then Up to (29, 11) to transition to East (0, 23).
  - Steps: 14 Right, 14 Up = 28 overworld steps.
- **Phase 3: Traverse Safari Zone East (Map 0_217) to Safari Zone North (Map 0_218)**
  - Path: Walk East along Row 22 to Column 5, bypass Rest House 2 via Row 24, walk East to Column 20.
  - Climb stairs at (20, 21), cross plateau to (12, 21), descend western stairs.
  - Climb northern plateau stairs at (12, 7), walk east to (17, 7), descend eastern stairs.
  - Walk Right to Column 21, North to Row 5, and West along Row 5/4/3 to (0, 5) to transition to North (39, 31).
- **Phase 4: Traverse Safari Zone North (Map 0_218) to Safari Zone West (Map 0_219)**
  - Path: Walk West along Row 31/33 to Column 9, then walk Down to (9, 35) to transition to West (27, 0).
- **Phase 5: Collect Gold Teeth and HM03 Surf in Safari Zone West**
  - Walk South along Eastern ground corridor to (25, 18).
  - Walk Left to (21, 18) and climb plateau stairs at (21, 17) to (21, 16).
  - Walk West across plateau via Row 16 to (6, 18), then descend western stairs at (6, 19) to (6, 20).
  - Walk North to Northwest ground level to retrieve Gold Teeth at (19, 7) (to be verified visually on-screen) and enter Secret House at (3, 3) to get HM03 Surf.
  - Systematic Testing: Stand at Row 5 facing South and attempt to walk Down into Row 6 on Columns 11-16 to test if it's a solid wall or a one-way jump. Citing Socratic Question 2 methodology.