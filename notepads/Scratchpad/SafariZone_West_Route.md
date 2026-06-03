# Safari Zone West Exploration Scratchpad (Run 15 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 15 Start Turn**: Turn 50478.
- **Current Turn**: Turn 50546.
- **Currently standing at**: (0, 5) on Map 0_217 (Safari Zone East).
- **Steps Taken in Run 15**: 129 overworld steps.
- **Steps Remaining**: 371 steps remaining.

## Run 15 Active Route Phases:
- [DONE] **Phase 1**: Traverse Safari Zone Center (Map 0_220) from (15, 25) to (29, 11) (31 steps)
- [DONE] **Phase 2**: Traverse Safari Zone East (Map 0_217) from (0, 23) to Northwest Transition at (0, 5) (98 overworld steps: 31 to 129)
- [IN PROGRESS] **Phase 3**: Traverse Safari Zone North (Map 0_218) from (39, 31) to Safari Zone West (Map 0_219) (34 overworld steps)
  - **Plan**:
    1. Spawn at (39, 31).
    2. Walk West along Row 31: Left 17 steps to (22, 31).
    3. Walk Up along Column 22: Up 8 steps to (22, 23).
    4. Walk Up 1 step onto the Western Plateau stairs at (22, 23) to land at (22, 22) on the plateau.
    5. Walk West across the plateau: Left 3 steps to (19, 22) -> Down 1 step to (19, 23) -> Left 10 steps to Column 9? No, let's verify on-site!
- [NEXT] **Phase 4**: Traverse Safari Zone West (Map 0_219) via Column 9 ground corridor to the Secret House at (3, 3) (57 overworld steps)
- [NEXT] **Phase 5**: Retrieve HM03 Surf from Secret House and retrieve Warden's Gold Teeth at (19, 28) on the ground.

## Socratic Answers / Verified Notes:
- **Column 10 Cliff Blockage (Map 0_217)**: Column 10 on Rows 4-7 consists of solid cliff walls (TYPE_2889), which prevents walking Down directly from (10, 3) to (10, 5). We must use Column 9 to transition Down to Row 5.
- **Step-Budget Synchronization**: We will update the remaining steps after every overworld movement segment immediately to maintain 100% RAM synchronization.