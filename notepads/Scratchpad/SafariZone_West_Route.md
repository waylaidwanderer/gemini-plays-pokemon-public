# Safari Zone West Exploration Scratchpad (Run 15 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 15 Start Turn**: Turn 50478.
- **Current Turn**: Turn 50587.
- **Currently standing at**: (27, 13) on Map 0_219 (Safari Zone West).
- **Steps Taken in Run 15**: 208 overworld steps.
- **Steps Remaining**: 292 steps remaining.

## Run 15 Active Route Phases:
- [DONE] **Phase 1**: Traverse Safari Zone Center (Map 0_220) from (15, 25) to (29, 11) (31 steps)
- [DONE] **Phase 2**: Traverse Safari Zone East (Map 0_217) from (0, 23) to Northwest Transition at (0, 5) (98 overworld steps: 31 to 129)
- [DONE] **Phase 3**: Traverse Safari Zone North (Map 0_218) via Western Plateau to Safari Zone West (Map 0_219) (66 overworld steps: 129 to 195)
- [IN PROGRESS] **Phase 4**: Traverse Safari Zone West (Map 0_219) via Northern Bypass to the Secret House at (3, 3) (47 overworld steps)
  - **Plan**:
    1. Spawn at (27, 0).
    2. Walk Down 13 steps along Column 27 to Row 13: (27, 0) -> (27, 13).
    3. Walk Left 4 steps to Column 23: (27, 13) -> (23, 13) (pass Column 24 gap at Row 13).
    4. Walk Up 10 steps along Column 23 to Row 3: (23, 13) -> (23, 3).
    5. Walk Left 20 steps along Row 3 to Column 3: (23, 3) -> (3, 3) [Secret House].
- [NEXT] **Phase 5**: Retrieve HM03 Surf from Secret House and retrieve Warden's Gold Teeth at (19, 28) on the ground on backtrack (41 overworld steps).

## Socratic Answers / Verified Notes:
- **Socratic Question 1 (Syncing Step Budget)**: Transition to Map 0_219 occurred on Turn 50580. We have successfully synchronized our active objectives and scratchpad to (27, 0) on Map 0_219 with exactly 305 remaining overworld steps.
- **Socratic Question 2 (Map 0_219 Optimized Ground Route)**: Our local BFS discovered an optimized Row 3 northern bypass: Down x13 to (27, 13) -> Left x4 to (23, 13) -> Up x10 to (23, 3) -> Left x20 to (3, 3). Total = 47 steps.
- **Socratic Question 3 (Row 3 Passability & Verification)**: Walking on Row 3 (north of the plateau) completely bypasses the plateau and eliminates the need to traverse Column 9 vertically on Rows 4-20. We will verify Row 3 horizontally tile-by-tile.
- **Socratic Question 4 (Step Budgeting & Priority)**: We have 305 steps remaining. Getting Surf (47 steps) + moving to Gold Teeth (41 steps) + inside house steps = ~100 steps total. We have a huge surplus of ~195 steps. Priority: 1. HM03 Surf, 2. Gold Teeth.