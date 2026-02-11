# Murkrow Solution: The Col 27 Loop (Mirror Y)

## Start State
- P(14, 14), M(18, 1).

## Execution Plan
1. **Pass Computers (Y=1)**:
   - Move **Right x9** to P(23, 14). M -> (27, 1).
   - State: P(23, 14), M(27, 1).

2. **Cross to South (Col 27)**:
   - Move **Up x13** to P(23, 1). M -> (27, 14).
   - *Note: Col 27 is clear of walls/computers.*
   - State: P(23, 1), M(27, 14).

3. **Pass Grunt (Y=14)**:
   - Move **Left x4** to P(19, 1). M -> (23, 14).
   - *Note: Row 14 is clear at Col 25.*
   - State: P(19, 1), M(23, 14).

4. **Position for Ratchet**:
   - Move **Down x1** to P(19, 2). M -> (23, 13).
   - State: P(19, 2), M(23, 13).

5. **Y-Ratchet (Wall 12)**:
   - Move **Down x13** to P(19, 15).
   - M tries Up. Blocked by Wall at Row 12. Stays (23, 13).
   - State: P(19, 15), M(23, 13).

6. **X-Ratchet (Grunt)**:
   - Move **Right x6** to P(25, 15).
   - M moves Right. Blocked at (24, 13) by Grunt(25, 13).
   - Target Offset -1 achieved.
   - State: P(25, 15), M(24, 13).

7. **Finish**:
   - Move **Left x2** to P(23, 15). M -> (22, 13).
   - Move **Up x1** to P(23, 14). M -> (22, 14).
   - **ENTER**.