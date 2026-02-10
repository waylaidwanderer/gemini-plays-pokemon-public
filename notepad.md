# Team Rocket HQ - Murkrow Puzzle

## Current Status (Turn 36376)
- **Player**: (24, 15). M: (23, 15).
- **Goal**: Open Boss Door at (22, 14).

## The Plan: "Gap Access Strategy"
1. **Move to Gap (Col 26)**:
   - Right 3. P(27,15), M(26,15).
   - Down 1. P(27,16), M(26,14).
2. **Pump M North**:
   - Pump Down x5 against Wall (27,17).
   - M moves 14 -> 9. State: P(27,16), M(26,9).
3. **Align West (Col 22)**:
   - Left 4. P(23,16), M(22,9).
4. **Pump M South to Door**:
   - Up 1. P(23,15), M(22,10).
   - Pump Up x4 against Wall (23,14).
   - M moves 10 -> 14. Target Reached!
5. **Open Door**:
   - M is at (22,14).
   - P is at (23,15).
   - Figure out interaction (Face left? Wait?).

## Mechanics
- **Gap**: Row 14, Cols 26-28 are OPEN.
- **Door**: At (22,14). Statue at (22,15).
- **M Lock**: At (22,14), M is boxed in. This is likely the solution state.