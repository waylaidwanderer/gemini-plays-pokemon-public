# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (13, 11) on Victory Road 3F East (Map 0_198) | Turn: 107881

## Scientific Testing Plan for Victory Road Exit
We must locate the exact exit warp tile by systematically investigating the 2F East northeast corner.

### Hypothesis 1: 3F East Northeast Corner (Completed Testing)
- **Hypothesis**: The true exit of Victory Road is on the 3rd Floor (3F) East in the northeast corner (Columns 20-28, Rows 0-2).
- **Testing Method**: Systematically step on and test Row 0 and Row 1 candidate tiles.
- **Empirical Test Results on 3F East**:
  - (28, 2): Stepped on at Turn 107581. Result: No warp triggered.
  - (28, 1): Stepped on at Turn 107589. Result: No warp triggered.
  - (28, 0): Pressed Up at Turn 107590. Result: BUMPED (solid rock wall).
  - (27, 0): Pressed Up at Turn 107599. Result: BUMPED (solid rock wall).
  - (26, 0): Pressed Up at Turn 107602. Result: BUMPED (solid rock wall).
  - (25, 0): Pressed Up at Turn 107606. Result: BUMPED (solid rock wall).
  - (24, 0): Pressed Up at Turn 107610. Result: BUMPED (solid rock wall).
  - (23, 0): Pressed Up at Turn 107617. Result: BUMPED (solid rock wall).
  - (22, 0): Pressed Up at Turn 107621. Result: BUMPED (solid rock wall).
  - (21, 0): Pressed Up at Turn 107632. Result: BUMPED (solid rock wall).
  - (20, 0): Pressed Up at Turn 107639. Result: BUMPED (solid rock wall).
  - (19, 0): Pressed Up at Turn 107645. Result: BUMPED (solid rock wall).
- **Conclusion**: Hypothesis 1 is completely DISPROVEN. No exit warp exists on 3rd Floor (3F) East Row 0 or Row 1 on Columns 20-28.

### Hypothesis 2: 2F East Northeast Corner (Active)
- **Hypothesis**: The exit is at (28, 1) on 2F East, reached by taking the ladder at (26, 8) on 3F East down to (27, 7) on 2F East.
- **Routing Strategy Audit**:
  - Note: (27, 7) on 2F East is inside a completely closed, isolated ground-level pocket on 2F East (bounded by Koga's plateau to the south and the Row 6 rock wall to the north). 
  - If we land at (27, 7) on 2F East, we cannot walk north to Row 1/Row 2 due to the Row 6 solid rock wall across Columns 24-28.
  - Therefore, to access the true northern part of 2F East on ground level, we must utilize the southern ground corridor at Row 16 to cross from 2F East to 2F West, and bypass the plateau.
  - Let's construct a complete unblocked pathing hypothesis via 2F West to reach the northern half of 2F East on ground level.
- **Unblocked 2F West Ground-Bypass Hypothesis**:
  1. We are currently at (9, 2) on 3F East. We must walk to (27, 15) on 3F East and take the ladder DOWN to 2F East (lands at (26, 14) on 2F East plateau level).
  2. From (26, 14), we walk West along the 2F plateau corridor to 2F West (around Column 13/14, Row 12/13).
  3. We descend from the 2F plateau to the southern ground floor at Row 16.
  4. On Row 16, we walk West to Column 9 (near Switch B2 at (9, 16)).
  5. We walk North along Column 9 (which serves as our unblocked vertical passage on the West side) to bypass Koga's plateau and reach the northern ground area at Row 3.
  6. We walk East along Row 3 from Column 9 all the way to Column 27/28 on 2F East.
  7. From Column 27/28, we walk North to Row 1 to reach and test the exit warp at (28, 1) on 2F East!
- **Status**: Active. Navigating back to (27, 15) ladder on 3F East.

### Hypothesis 3: 1F East Northeast Corner (On Hold)
- **Hypothesis**: The true exit is on 1F East.
- **Status**: On hold pending results of Hypothesis 2.

## Current Pathing Instructions:
- Turn 107823: We are currently at (27, 2) on 3F East.
- Step 1: Walk Down 3 times to (27, 5), Left to (26, 5), and Down 2 times to (26, 7) to bypass the Row 6 walls.
- Step 2: From (26, 7), walk South along Column 26 to (26, 14), then Right to (27, 14) and Down to (27, 15) to take the ladder DOWN to 2F East.
- Step 3: From 2F East plateau (26, 14), walk West to 2F West plateau (around Column 13/14, Row 12/13), descend stairs to Row 16, and walk West on Row 16 to Column 9 (near Switch B2 at (9, 16)).
- Step 4: Walk North on Column 9 on 2F West to Row 3, testing the vertical passability past Koga's plateau.
- Step 5: Walk East on Row 3 from Column 9 to Column 27/28 on 2F East.
- Step 6: Walk North on Column 28 to Row 1 to reach and test the exit warp at (28, 1) on 2F East!
- Turn 107863: Tested the 2F East pocket on foot. We descended to 2F East at (23, 7) on Turn 107845, and empirically verified that (24, 7) is a solid rock wall of TYPE_2889. This proves the ground-level pocket on 2F East is split into two isolated halves by Column 24, and we cannot walk between the (23, 7) ladder and the (27, 7) ladder on ground level on 2F East. This disproves the 2F East pocket bypass. We successfully backtracked to 3F East at (23, 7) on Turn 107854.