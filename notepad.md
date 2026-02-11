# Murkrow Puzzle: The Jed Ratchet (Mirror Y)

## Assumptions
- **Start**: P(3, 14), M(7, 1).
- **Behavior**: Mimic X, Mirror Y.
- **Blockers**: Jed(18, 12), Computer(19, 2), Grunt(25, 13).

## Execution Log
1. **Move to P(14, 14)**:
   - Action: Right x11.
   - Expected M: (7, 1) -> (18, 1).
   - State: P(14, 14), M(18, 1).

2. **Ratchet 1 (Jed Block)**:
   - Action: Up x11 to P(14, 3).
   - M moves Down x11. Target (18, 12).
   - **Blocked by Jed** at (18, 12).
   - M stops at (18, 11).
   - State: P(14, 3), M(18, 11).

3. **Shift X**:
   - Action: Right x1 to P(15, 3).
   - M moves Right to (19, 11).
   - State: P(15, 3), M(19, 11).

4. **Ratchet 2 (Computer Block)**:
   - Action: Down x11 to P(15, 14).
   - M moves Up x11. Target (19, 0).
   - **Blocked by Computer** at (19, 2).
   - M stops at (19, 3).
   - State: P(15, 14), M(19, 3).

5. **Align Y**:
   - Action: Up x10 to P(15, 4).
   - M moves Down x10 to (19, 13).
   - State: P(15, 4), M(19, 13).

6. **Align X & Finish**:
   - Action: Right x5 to P(20, 4). M -> (24, 13).
   - Action: Left x2 to P(18, 4). M -> (22, 13).
   - Action: Up x1 to P(18, 3). M -> (22, 14) [Plate].
   - **SOLVED**.