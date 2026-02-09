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

## Current State
- **Player**: (22, 13). (Confirmed by Game State).
- **Murkrow**: Unknown. Likely (22, 12) or (21, 13) or (23, 13).
- **Goal**: Find Murkrow and Open Door.

## Strategy: The Validated Grunt Flip
- **Goal**: Place P(22, 13), M(22, 14).
- **Logic**: Use the Grunt at (22, 9) to block M's upward movement, placing P North of M.
- **Current State**: P(20, 14), M(20, 13).
- **Test**: Press `Right` (P Blocked by Grunt 21, 14).
  - If M moves to (21, 13), we can slide M to column 22.
- **Plan (If Slide Works)**:
  1. `Right` x2 -> P(20, 14). M slides to (22, 13).
  2. `Up` x4 -> P(20, 10). M moves to (22, 9) [Blocked], lands (22, 10).
  3. `Right` -> P(21, 10). M blocked right. Stays (22, 10).
  4. `Up` -> P(21, 9). M blocked up. Stays (22, 10).
  5. `Down` x4 -> P(21, 13), M(22, 14).
  6. `Right`, `A`.
- **Action**: Execute Test (`Right`).