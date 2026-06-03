# Safari Zone West Exploration Scratchpad (Run 13 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 13 Start Turn**: Turn 49681.

## Current Status
- Currently standing at (21, 16) on Map 0_219 (Safari Zone West) on Turn 50041.
- Steps taken in Run 13 so far: 261 overworld steps.
- Exactly 239 steps remaining (from 500 starting steps).

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
- [COMPLETED] **Phase 1: Enter Safari Zone Center (Map 0_220) at (15, 25)**
- [COMPLETED] **Phase 2: Traverse Center to East (Map 0_217)**
- [COMPLETED] **Phase 3: Traverse Safari Zone East (Map 0_217) to Safari Zone North (Map 0_218)**
- [COMPLETED] **Phase 4: Traverse Safari Zone North (Map 0_218) to Safari Zone West (Map 0_219)**
- [IN PROGRESS] **Phase 5: Backtrack across West Plateau to Southwest Ground Level (6, 20)**
  - Walk Down the eastern corridor to (25, 18). [COMPLETED]
  - Walk Left to (21, 18). [COMPLETED]
  - Climb the stairs at (21, 17) to (21, 16). [COMPLETED]
  - Walk Left across the plateau to (6, 16). [IN PROGRESS]
  - Walk Down to descend the western stairs at (6, 19) to (6, 20).
- **Phase 6: Re-verify Northwest Ground Passage & Retrieve Items**
  - Walk to (6, 20) and re-evaluate the southwest-northwest connection.
  - Re-verify if Column 2 Row 13 water or Column 1 Row 14/15 trees are passable.
  - Walk to the northern ground level, collect the Warden's Gold Teeth at (19, 7) or (9, 7), and visit the Secret House at (3, 3) to get HM03 Surf.

## Systematic Western Blockage Testing Protocol (Run 13) - COMPLETED & VERIFIED
- On Turns 49995-49999, we executed systematic foot-testing to investigate southwest-northwest ground-level connectivity:
  1. **Test Column 1 Row 15**: Standing at (1, 16) on Turn 49995, we attempted to walk Up into (1, 15) (TYPE_2889 tree). Result: Collision (remained at 1, 16), physically proving (1, 15) is a solid, impassable tree wall.
  2. **Test Column 2 Row 13**: Standing at (2, 14) on Turn 49998, we attempted to walk Up into (2, 13) (TYPE_4e8c water). Result: Collision (remained at 2, 14), physically proving (2, 13) is blocked by water.
  3. **Test Column 1 Row 14**: Standing at (2, 14) on Turn 49999, we attempted to walk Left into (1, 14) (TYPE_2889 tree). Result: Collision (remained at 2, 14), physically proving (1, 14) is a solid, impassable tree wall.
- **Definitive Conclusion**: There is absolutely NO ground-level passage from the Southwest to the Northwest. The elevated plateau is the only route. We must backtrack across the plateau.

## Socratic Question Answers
### Socratic Question 1
- **Actual Remaining Steps on Turn 49986**: Exactly 287 steps remaining (since we have taken 213 overworld steps in Run 13 so far).
- **How did the desynchronization occur?**:
  - The objectives file was carrying a tracking drift because it hadn't been updated with our actual movement steps, keeping a stale '120 steps remaining' label.
  - The scratchpad had a massive drift of 178 turns and map transition data because it wasn't modified since we left Safari Zone North. It assumed we were still at (26, 23) in North with 267 steps remaining, completely omitting the steps taken during the transition and backtracking loops.
- **How will you correct both files immediately?**:
  - The scratchpad has been updated to Turn 49982 with 457 remaining steps (using 43 steps taken on Map 0_219).
  - The objectives file and scratchpad will be updated on the next turn to reflect the exact remaining step count of 287 steps.

### Socratic Question 2
- **Why did the pathfinder's elevation simulation fail?**:
  - When standing directly on the staircase tile at (21, 17) (TYPE_4b8d), the elevation simulation didn't realize that walking "Down" would actually descend to the ground level (21, 18). It assumed that since the destination was (21, 18), walking Down would simply reach (21, 18).
  - However, because we were on the stairs, walking Down descended us instead of keeping us on the plateau.
- **What did we learn?**:
  - We must step fully onto the plateau (e.g. to (21, 16)) where the tile type is TYPE_2770 before running pathfinder queries to prevent the elevation simulation from getting confused and returning a ground-level path.

### Socratic Question 3
- **Exact planned path and button sequence**:
  - We are at (9, 16) on Turn 49986.
  - We want to reach (6, 20) via the western stairs at (6, 19).
  - Button sequence:
    - Walk Left 3 times: (9, 16) -> (8, 16) -> (7, 16) -> (6, 16) (all TYPE_2770).
    - Walk Down 3 times: (6, 16) -> (6, 17) -> (6, 18) -> (6, 19) (stairs, TYPE_4b8d).
    - Walk Down 1 time: (6, 19) -> (6, 20) (ground level, TYPE_fed7).
    - Total steps: 3 + 3 + 1 = 7 steps.
  - **Remaining step count after landing**:
    - Current: 287 steps.
    - Remaining: 287 - 7 = 280 steps.

### Socratic Question 4
- **Systematic Western Blockage Testing Protocol**:
  - Once we reach (6, 20), we will systematically test:
    1. Walk to (1, 16), face Up, walk Up to (1, 15), (1, 14), (1, 13).
    2. Walk to (2, 14), face Up, walk Up to (2, 13).
  - We will document every coordinate tested, its collision state, and the turn number in `Scratchpad/SafariZone_West_Route`.
  - **How this modifies our route**:
    - If Column 1 is passable, we can walk directly up the west edge from the southwest to the northwest ground level! This bypasses the plateau entirely and saves dozens of steps, allowing us to easily reach the Secret House and Warden's Gold Teeth with ample step budget.