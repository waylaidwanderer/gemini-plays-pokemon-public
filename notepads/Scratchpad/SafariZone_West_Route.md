# Safari Zone West Exploration Scratchpad (Run 15 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 15 Start Turn**: Turn 50478.
- **Current Turn**: Turn 50579.
- **Currently standing at**: (12, 33) on Map 0_218 (Safari Zone North).
- **Steps Taken in Run 15**: 189 overworld steps.
- **Steps Remaining**: 311 steps remaining.

## Run 15 Active Route Phases:
- [DONE] **Phase 1**: Traverse Safari Zone Center (Map 0_220) from (15, 25) to (29, 11) (31 steps)
- [DONE] **Phase 2**: Traverse Safari Zone East (Map 0_217) from (0, 23) to Northwest Transition at (0, 5) (98 overworld steps: 31 to 129)
- [IN PROGRESS] **Phase 3**: Traverse Safari Zone North (Map 0_218) via Western Plateau to Safari Zone West (Map 0_219) (35 steps)
  - **Plan**:
    1. Backtrack to (22, 23): Walk Up to (18, 32) -> Right x2 to (20, 32) -> Down to (20, 33) -> Right x2 to (22, 33) -> Up x10 to (22, 23) [16 steps]. (Completed)
    2. Climb onto plateau: Walk Up 1 step to (22, 22) [1 step]. (Completed)
    3. Walk across plateau: Left 6 steps to (16, 22) -> Down 4 steps to (16, 26) [10 steps]. (Completed)
    4. Descend western stairs: Down 1 step to (16, 27) [1 step]. (Completed)
    5. Walk to exit: Down 1 step to (16, 28) -> Left 7 steps to (9, 28) -> Down 7 steps to (9, 35) [15 steps]. (In Progress: reached 12, 33, now walking 3 Left and 3 Down to transition)
    6. Transition step: Down 1 step to transition to Safari Zone West (Map 0_219) at (26, 0).
    - **Total Steps to Transition**: 6 overworld steps from current position (12, 33) to transition! Remaining step count will be exactly 305 steps upon transition.
- [NEXT] **Phase 4**: Traverse Safari Zone West (Map 0_219) via Column 9 ground corridor to the Secret House at (3, 3) (56 overworld steps)
  - **Plan**:
    1. Spawn at (26, 0).
    2. Walk Down 18 steps to (26, 18).
    3. Walk Left 17 steps to (9, 18).
    4. Walk Up 15 steps to (9, 3).
    5. Walk Left 6 steps to (3, 3) [Secret House].
- [NEXT] **Phase 5**: Retrieve HM03 Surf from Secret House and retrieve Warden's Gold Teeth at (19, 28) on the ground.

## Socratic Answers / Verified Notes:
- **Socratic Question 1 (Plateau Path details)**: 
  - *Backtrack to (22, 23)*: Up, Right x2, Down, Right x2, Up x10 to (22, 23) (16 steps).
  - *Climb onto plateau (22, 22)*: Up (1 step).
  - *Traverse plateau to (16, 26)*: Left x6, Down x4 (10 steps).
  - *Descend western stairs to (16, 27)*: Down (1 step).
  - *Walk to exit (9, 35)*: Down to (16, 28), Left x7 to (9, 28), Down x7 to (9, 35) (15 steps).
  - *Transition step*: Down (1 step).
  - *Total steps*: 6 steps from current position (12, 33) to transition.
  - *Remaining steps upon map transition*: 311 - 6 = 305 steps remaining.
- **Socratic Question 2 (Plateau Range Correction)**: Map 0_218 plateau y-range has been corrected in our pathfinder to `range(20, 23)` to correctly encompass Row 22 and prevent pathing failure starting from (22, 22).
- **Socratic Question 3 (Step Mismatch)**: Mismatches occur when overworld movement sequences are executed but status updates are deferred. We will update the scratchpad and objectives turn-by-turn.
- **Socratic Question 4 (Safari Zone West Ground Route)**: From spawn at (26, 0) -> Down x18 to (26, 18) -> Left x17 to (9, 18) -> Up x15 to (9, 3) -> Left x6 to (3, 3). Total = 56 steps.