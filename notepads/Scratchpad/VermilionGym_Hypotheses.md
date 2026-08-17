# Vermilion Gym - Trash Can Mechanics & Empirical Analysis

## Empirical Data Reconciliation
1. **Stationary Toggle Dataset (Turns 2444-2460 & 2574-2580)**:
   - 90+ consecutive checks on tiles (7, 7) and (9, 7) yielded exactly 0 switch triggers.
   - Statistical inference: The hypothesis that Switch 1 re-rolls per check with p = 1/15 is falsified by this dataset ((14/15)^90 ≈ 0.19%). Switch 1 is FIXED upon gym map entry/reset, NOT re-rolled on every empty can check.

2. **Sequential Sweep Dataset (Run #4, Turns 2527-2571)**:
   - All 15 cans were systematically checked in a single session.
   - Possible causes: Script flag state in current long session (200+ turns since blackout entry), or input drop during rapid multi-button execution.

## Corrective Strategy
- **Action 1**: Refresh the Gym map state by exiting through the south door (4..5, 17) to Vermilion City, and immediately re-entering. This triggers `InitGymTrashCans` with a fresh random seed and cleanly initialized script flags.
- **Action 2**: Upon re-entry, conduct a rigorous, single-turn, single-can verification sweep from Col 1 to Col 5 to Col 9.
- **Action 3**: As soon as Switch 1 is found, immediately check its cardinal adjacent cans for Switch 2.
