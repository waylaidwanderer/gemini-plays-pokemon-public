# Safari Zone West Exploration Scratchpad (Run 15 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 15 Start Turn**: Turn 50478.
- **Current Turn**: Turn 50852.
- **Currently standing at**: (16, 7) on Map 0_219 (Safari Zone West) [Plateau].
- **Steps Taken in Run 15**: 388 overworld steps.
- **Steps Remaining**: 112 steps remaining.

## Run 15 Active Route Phases:
- [DONE] **Phase 1**: Traverse Safari Zone Center (Map 0_220) from (15, 25) to (29, 11) (31 steps)
- [DONE] **Phase 2**: Traverse Safari Zone East (Map 0_217) from (0, 23) to Northwest Transition at (0, 5) (98 overworld steps: 31 to 129)
- [DONE] **Phase 3**: Traverse Safari Zone North (Map 0_218) via Western Plateau to Safari Zone West (Map 0_219) (66 overworld steps: 129 to 195)
- [IN PROGRESS] **Phase 4**: Traverse Safari Zone West (Map 0_219) via Plateau and Southeastern descent to Gold Teeth at (19, 7) and Secret House at (3, 3)
  - **Plan**:
    1. Stand at (17, 14) on the plateau.
    2. Walk Right to (21, 14) and Down to (21, 18) on the ground level via the (21, 17) southeastern stairs.
    3. Walk Right to the eastern ground corridor (Column 25) on Row 18.
    4. Walk Up the eastern corridor to Row 7, then walk West on Row 7 to retrieve the Gold Teeth at (19, 7).
    5. Walk to the Secret House at (3, 3) on the ground level.
- [NEXT] **Phase 5**: Retrieve HM03 Surf from Secret House.

## Socratic Answers / Verified Notes
- **Socratic Question 1 (Step Drift)**: Drift arose from unlogged battle transitions. We will subtract steps instantly on-screen after every single movement chunk.
- **Socratic Question 2 (Stairs adjacent coordinates)**: The BFS plateau check blocked (21, 17) because the staircase tile itself was missing from `plateau_tiles`. For the eastern stairs on Column 17 Row 9, we defined the robust adjacent transition `stairs[(17, 9, 1)] = (18, 9, 0)` and `stairs[(18, 9, 0)] = (17, 9, 1)` and added `(17, 9)` to `plateau_tiles`, which successfully compiled the 5-step optimal descent path.
- **Socratic Question 3 (Pruning obsolete notes)**: Run 14 Socratic answers scratchpad is now obsolete. We will delete `Scratchpad/Socratic_Run14_Answers` to keep our workspace tidy.
- **Socratic Question 4 (Planned Route)**:
  - Walk to (18, 7) on the ground level via ['Down', 'Right', 'Right', 'Up', 'Up'] (5 steps).
  - Retrieve Gold Teeth by turning Right and pressing A (2 inputs).
  - Walk to Secret House at (3, 3) via Row 3: ['Up', 'Up', 'Up', 'Up', 'Left' x15] (19 steps).
  - Total steps required: 24 overworld steps, well within our 163 steps budget.