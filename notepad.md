# Team Rocket HQ - Murkrow Puzzle

## Current Status (Turn 36375)
- **Player**: (23, 15).
- **Murkrow**: LOST. Need to locate.
- **Goal**: Locate Murkrow and reset puzzle.

## The Plan: "Zig-Zag & Statue Pump"
1. **Setup**: P(24,13), M(24,12).
2. **Move Right**: P(25,13), M(25,12).
3. **Statue Pump East**:
   - Pump Down x5 against (25,14). M moves 12 -> 7.
   - P(25,13), M(25,7).
4. **Move to Gap**:
   - Right 1. P(26,13), M(26,7).
   - Up 1. P(26,12), M(26,8).
   - Pump Up 1 (vs 26,11). M(26,9).
   - State: P(26,12), M(26,9).
5. **Cross West**:
   - Left 2. P(24,12), M(24,9).
6. **Cross South**:
   - Down 4. P(24,16), M(24,5).
7. **Align X**:
   - Left 2. P(22,16), M(22,5).
8. **Pump M to Target**:
   - Pump Up x9 against Statue (22,15). M moves 5 -> 14.
   - P(22,16), M(22,14).
9. **Position P for Interact**:
   - Right 2. P(24,16), M(22,14) (Blocked by Wall).
   - Up 3. P(24,13), M(22,14) (Blocked by Statue).
   - Left 2. P(22,13), M(22,14) (Blocked by Wall).
10. **Interact**:
    - Face Down. Press A.

## Mechanics
- **X**: Parallel.
- **Y**: Mirror.
- **M Lock**: At (22,14), M is locked by Wall(W), Wall(E), Statue(S). Can only move N.