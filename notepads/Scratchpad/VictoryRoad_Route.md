# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (23, 10) on Victory Road 2F East (Map 0_194) | Turn: 107969

## Scientific Testing Plan for Victory Road Exit
We must locate the exact exit warp tile by systematically investigating the 2F East / 1F East pathway.

### Hypothesis 2: 1F East Northeast Corner (Active)
- **Hypothesis**: The true exit of Victory Road is in the northeast corner of 1F East. 
- **Routing Strategy**:
  1. We must take the ladder at (27, 15) on 3F East down to 2F East.
  2. This lands us at (26, 14) on 2F East.
  3. Walk 1 step Left to (25, 14) on 2F East.
  4. Take the ladder at (25, 14) down to 1F East.
  5. Locate and exit through the true exit warp to Route 23 North!

- **Refutation of 2F East (28, 1) Exit**: Standing on (28, 1) on 2F East on Turns 107006 and 107010 explicitly did not trigger any warp, proving it is not the exit. Furthermore, the solid rock wall at Row 6 blocks any vertical access to Row 1 on Columns 24-28. Thus, Hypothesis 2 of going to 2F East (28, 1) is formally disproven.
- **Refutation of 3F East (28, 1) Exit**: Systematic testing of Row 0 and Row 1 on 3F East confirmed all are solid rock walls or non-warping floor, completely disproving Hypothesis 1.

## Current Pathing Instructions:
- We are currently standing on 3F East at (26, 2) facing Left.
- Detour progress: Successfully disproved that we can walk South on Column 27/28 from Row 2, as Row 6 is occupied by a solid rock wall across Columns 24-29.
- Backtracking Route to cross over via 2F East:
  1. From (26, 2), walk Left 3 steps to (23, 2), then Down 5 steps to the ladder at (23, 7).
  2. Take the ladder at (23, 7) DOWN to 2F East.
  3. On 2F East, walk Down Column 23 to Row 11: (23, 7) -> (23, 8) -> (23, 9) -> (23, 10) -> (23, 11).
  4. Walk Right along Row 11 to Column 27: (23, 11) -> (27, 11).
  5. Walk Up Column 27 to Row 7: (27, 11) -> (27, 7).
  6. Take the ladder at (27, 7) UP to 3F East (lands at (26, 8) on 3F East).
  7. From (26, 8) on 3F East, walk Down to (27, 15) ladder and take it DOWN to 2F East plateau.
  8. From (26, 14) on 2F East plateau, walk Left to (25, 14) and descend to 1F East.
  9. Exit Victory Road!
- Let's execute the first step of this backtracking route: walk Left 3 steps to (23, 2) and Down 5 steps to (23, 7).