# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision**: 
  - If Player is blocked, Murkrow STAYS.
  - If Murkrow is blocked, Murkrow STAYS.
  - Murkrow and Player cannot overlap.

## Strategy: The Validated Solution
- **Goal**: Place M at (22, 14).
- **Current**: P(22, 14), M(22, 13).
- **Plan**:
  1. `Up` -> P(22, 13), M(22, 12).
  2. `Left` -> P(21, 13), M(21, 12).
  3. `Up` -> P(21, 12), M(21, 11).
  4. `Right` -> P(22, 12), M(22, 11).
  5. `Up` -> P(22, 11), M(22, 10).
  6. `Left` -> P(21, 11). M Blocked at (21, 10). Stays (22, 10).
  7. `Up` x2 -> P(21, 9). M Blocked at (22, 9). Stays (22, 10).
  8. `Down` x4 -> P(21, 13), M(22, 14).
  9. `Right` -> P(22, 13).
  10. `Down`, `A`.
- **Action**: Execute Steps 1-6 (Up, Left, Up, Right, Up, Left).