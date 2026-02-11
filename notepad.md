# Murkrow Puzzle: Computer Ratchet Strategy (Row 19)

## Phase 1: Setup
1. **Reset**: P(3, 14), M(7, 1).
2. **Move Right**:
   - P Right 11 to (14, 14).
   - M Right 11 to (18, 1).
3. **Jed Alignment**:
   - P Up 11 to (14, 3).
   - M Down 11 to (18, 12) -> Hits Jed -> M(18, 11).
   - State: P(14, 3), M(18, 11).

## Phase 2: The Computer Ratchet
4. **Pass Jed**:
   - P Right 1 to (15, 3). M to (19, 11).
5. **Ratchet via Computer (19, 2)**:
   - P Down 11 to (15, 14).
   - M Up 11. Blocked by Solid Computer at (19, 2).
   - M stops at (19, 3).
   - State: P(15, 14), M(19, 3).

## Phase 3: Positioning
6. **Y-Align to 13**:
   - P Up 10 to (15, 4).
   - M Down 10 to (19, 13).
   - State: P(15, 4), M(19, 13).
7. **X-Align to 22**:
   - P Right 7 to (22, 4).
   - M Right 7 -> Hits Grunt(25, 13) -> M(24, 13).
   - P Left 2 to (20, 4).
   - M Left 2 to (22, 13).
   - State: P(20, 4), M(22, 13).

## Phase 4: Trigger
8. **Open Door**:
   - P Up 1 to (20, 3).
   - M Down 1 to (22, 14).
   - **Success!**