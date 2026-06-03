# Safari Zone West Exploration Scratchpad (Run 15 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 15 Start Turn**: Turn 50478.
- **Current Turn**: Turn 50562.
- **Currently standing at**: (22, 31) on Map 0_218 (Safari Zone North).
- **Steps Taken in Run 15**: 147 overworld steps.
- **Steps Remaining**: 353 steps remaining.

## Run 15 Active Route Phases:
- [DONE] **Phase 1**: Traverse Safari Zone Center (Map 0_220) from (15, 25) to (29, 11) (31 steps)
- [DONE] **Phase 2**: Traverse Safari Zone East (Map 0_217) from (0, 23) to Northwest Transition at (0, 5) (98 overworld steps: 31 to 129)
- [IN PROGRESS] **Phase 3**: Traverse Safari Zone North (Map 0_218) on the ground level (Row 33 Bypass) to Safari Zone West (Map 0_219) (18 steps)
  - **Plan**:
    1. From (22, 31), walk Down 2 steps to (22, 33).
    2. Walk Left 13 steps along Row 33 to Column 9: (22, 33) -> (9, 33).
    3. Walk Down 2 steps along Column 9 to exit: (9, 33) -> (9, 35).
    4. Walk Down 1 step to transition to Safari Zone West (Map 0_219) at (26, 0).
    - **Total Steps**: 18 steps to transition! (Bypasses the Western Plateau entirely and saves 18 steps!)
- [NEXT] **Phase 4**: Traverse Safari Zone West (Map 0_219) via Column 9 ground corridor to the Secret House at (3, 3) (56 overworld steps)
  - **Plan**:
    1. Spawn at (26, 0).
    2. Walk Down 18 steps to (26, 18).
    3. Walk Left 17 steps to (9, 18).
    4. Walk Up 15 steps to (9, 3).
    5. Walk Left 6 steps to (3, 3) [Secret House].
- [NEXT] **Phase 5**: Retrieve HM03 Surf from Secret House and retrieve Warden's Gold Teeth at (19, 28) on the ground.

## Socratic Answers / Verified Notes:
- **Socratic Question 1 (Plateau vs Ground Path)**: 
  - *Plateau Path*: Walk Up Column 22 to (22, 23) [8 steps], climb stairs to (22, 22) [1 step], walk Left 6 and Down 4 to (16, 26) [10 steps], descend stairs to (16, 27) [1 step], walk Left 7 and Down 8 to (9, 35) [15 steps]. Total = 35 steps.
  - *Ground Path (Row 33 Bypass)*: Walk Down 2 to (22, 33) [2 steps], Left 13 to (9, 33) [13 steps], Down 2 to (9, 35) [2 steps]. Total = 17 steps (18 to transition).
  - *Decision*: We will take the ground-level bypass path as it is over 2x faster, saving 18 steps and leaving exactly 335 steps remaining upon transition!
- **Socratic Question 2 (Plateau Range Correction)**: Map 0_218 plateau y-range has been corrected in our pathfinder to `range(20, 23)` to correctly encompass Row 22 and prevent pathing failure starting from (22, 22).
- **Socratic Question 3 (Step Mismatch)**:Mismatches occur when overworld movement sequences are executed but status updates are deferred. We will update the scratchpad and objectives turn-by-turn.
- **Socratic Question 4 (Safari Zone West Ground Route)**: From spawn at (26, 0) -> Down x18 to (26, 18) -> Left x17 to (9, 18) -> Up x15 to (9, 3) -> Left x6 to (3, 3). Total = 56 steps.