# Strategy: Switch Room Puzzle (Map 3_54)
- Goal: Clear path to ladder at (23, 3).
- Puzzle Start (Reset): Turn 9462.
- Method: Systematic mapping and following Strategist advice.
- Current Status (Turn 9624):
    - Switch 3 (2, 1): ON
    - Switch 2 (10, 1): ON
    - Switch 1 (16, 1): ON
- Reset Phase: Turning Switch 1 OFF now.
- Observations:
    - All switches ON -> All shutters in Row 6, 8, 9 appear CLOSED (WALL).
    - This suggests the final state for the 3-2-1 sequence is NOT "all switches ON".
- Switch Logic Table (Hypothesis):
    - Switch 1: Toggles {16, 6; 17, 6; 12, 8; 12, 9}.
    - Switch 2: Toggles {10, 6; 6, 8; 6, 9}.
    - Switch 3: Toggles {12, 8; 12, 9}.
- Historical Data:
    - Test 3.1: Switch 1 ON alone -> (16, 6) & (17, 6) OPEN.
    - Test 3.2: Switch 2 ON alone -> (10, 6), (6, 8), (6, 9) OPEN.
    - Test 3.3: Switch 3 ON alone -> (2, 6), (3, 6) were already floor. (12, 8) stayed WALL.
- Plan:
    1. Confirm shutter states at (16, 5).
    2. Consult Strategist with verified All-ON state.
    3. Adjust switches to reach the goal.

# Area Notes
## Underground Warehouse Switch Room (3_54)
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Trainers: Rocket Grunt (17, 2), Burglar Eddie (4, 8), Rocket Grunt (Puzzle) 2 (11, 3), Rocket Grunt (Puzzle) 3 (3, 2).
- Exit: Ladder at (23, 3) leads to the Director's location.
- Rival: Rival Malice defeated at (20, 4).