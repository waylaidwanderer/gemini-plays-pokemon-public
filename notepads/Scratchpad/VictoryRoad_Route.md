# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (27, 8) on Victory Road 3F East (Map 0_198) | Turn: 107463

## Scientific Testing Plan for Victory Road Exit
We must locate the exact exit warp tile by systematically investigating each possible floor hypothesis.

### Hypothesis 1: 3F East Northeast Corner
- **Hypothesis**: The true exit of Victory Road is on the 3rd Floor (3F) East in the northeast corner (Columns 27-28, Rows 0-2).
- **Testing Method**:
  1. Push Boulder C2 at (24, 10) Left to (22, 10).
  2. Walk Left along Row 11 to 3F West.
  3. Walk Up Column 13 to Row 2.
  4. Walk Right along Row 2 to (27, 2).
  5. Systematically step on (27, 2), (28, 2), (27, 1), (28, 1), (27, 0), and (28, 0).
  6. Observe if Map ID transitions to Route 23 North (Map 0_34) in the Game State.
- **Status**: Preparing to execute Step 1.

### Hypothesis 2: 2F East Northeast Corner
- **Hypothesis**: The true exit is on 2F East at (28, 1) or (27, 1).
- **Testing Method**:
  1. Once Row 2 of 3F is reached, we can also test if there is an exit warp or ladder.
  2. Note: We previously stood on (28, 1) on 2F East on Turn 106857 and did not exit the cave. This suggests 2F East is NOT the true exit floor.
- **Status**: On hold pending Hypothesis 1.

### Hypothesis 3: 1F East Northeast Corner
- **Hypothesis**: The true exit is on 1F East.
- **Testing Method**:
  1. If 3F East does not contain the exit warp, look for a ladder leading to 1F East on 2F East.
- **Status**: On hold.

## Current Pathing Instructions:
- Stand at (25, 10) facing Left to push Boulder C2.
- Path from (27, 8):
  1. Down to (27, 9)
  2. Left 2 steps to (25, 9) (via (26, 9))
  3. Down to (25, 10) (Facing Left)