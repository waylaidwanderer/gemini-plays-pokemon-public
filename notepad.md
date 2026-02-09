# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision Rules**:
  - P Blocked: Murkrow Stays.
  - M Blocked: Murkrow Stays.
  - No Overlap.

## Strategy: The Column 19 Solution
- **Goal**: Use the open column 19 to circle around Murkrow's Y-axis.
- **Start**: P(20, 14), M(20, 13).
- **Phase 1: Setup**
  1. `Up`, `Right` x2 -> P(22, 13), M(22, 12).
  2. `Up` x2 -> P(22, 11), M(22, 10).
- **Phase 2: Desync**
  3. `Left` x3 -> P(19, 11). M(22, 10) (Blocked by Computer at 21, 10).
  4. `Up` x2 -> P(19, 9). M(22, 10) (Blocked by Grunt at 22, 9).
     - **Result**: M is now South of P relative position.
- **Phase 3: Delivery**
  5. `Down` x4 -> P(19, 13), M(22, 14).
  6. `Right` x3 -> P(22, 13). M(22, 14) (Blocked by Door).
  7. Interact Down.
- **Action**: Execute Phase 1 & Start Phase 2 (Up, Right, Right, Up, Up, Left).