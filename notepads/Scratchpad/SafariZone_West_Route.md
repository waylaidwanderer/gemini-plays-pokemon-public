# Safari Zone West Exploration Scratchpad (Run 12 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 12 Start Turn**: Turn 49165.

## Current Status
- Currently standing at (18, 31) in Safari Zone North (Map 0_218) on Turn 49278.
- Exactly 364 overworld steps remaining (136 overworld steps taken).

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
- **Phase 3: Traverse Safari Zone East (Map 0_217) to Safari Zone North (Map 0_218)** (Current)
  - Path 3A: Complete Segment 1 on ground: Walk East from (17, 24) to (20, 24), then Up to the southern stairs at (20, 21). (Completed on Turn 49211)
  - Path 3B: Climb stairs to (20, 20), walk Left along Row 20 to (12, 20), then walk Down to western stairs (12, 21), and transition to ground at (11, 20). (Completed on Turn 49218)
  - Path 3C: Walk East on Row 8 from (9, 8) to (12, 8), climb northern stairs at (12, 7) onto high plateau at (12, 6). (Completed on Turn 49221)
  - Path 3D: Walk East on plateau to (17, 6), descend eastern stairs at (17, 7) to (17, 8). (Completed on Turn 49228)
  - Path 3E (Active): Walk from (10, 3) to the transition at (0, 5) to transition to Safari Zone North (39, 31).
- **Phase 4: Traverse Safari Zone North (Map 0_218) to Safari Zone West (Map 0_219)**
  - Path: Walk West along Row 31/33 to Column 9, then walk Down to (9, 35) to transition to West (27, 0).
- **Phase 5: Collect Gold Teeth and HM03 Surf in Safari Zone West**
  - Walk South along Eastern ground corridor to (25, 18).
  - Walk Left to (21, 18) and climb plateau stairs at (21, 17) to (21, 16).
  - Walk West across plateau via Row 16 to (6, 18), then descend western stairs at (6, 19) to (6, 20) [Southwest ground level].
  - Walk Left to Column 1 or 2 on Row 20, and systematically test Column 1 and Column 2 to walk North past Row 13 to Row 5 (re-verifying if the water blockage or tree blockage was a testing error, as on-foot passage must be possible here).
  - Walk to (3, 3) for the Secret House, picking up Gold Teeth at (19, 7).
  - Systematic Testing: Stand on Row 6 (high ground of plateau) facing North, and attempt to walk Up (North) into Row 5 (low ground) on Columns 11-16 to test if it's a solid wall or a jumpable ledge. Citing Socratic Question 2 methodology.