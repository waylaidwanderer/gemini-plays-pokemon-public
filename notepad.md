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

## Strategy: The 19-Flank Solution (Corrected)
- **Status**: P(19, 13). M(19, 12). (Deduced).
- **Goal**: Reach P(20, 10), M(22, 9).
- **Plan**:
  1. `Left` -> P(18, 13), M(18, 12).
  2. `Up` x3 -> P(18, 10), M(18, 9).
  3. `Right` x4 -> P moves to (20, 10) (Blocked by PC). M moves to (22, 9).
  4. `Down` -> P(20, 11), M(22, 10).
  5. `Right` -> P(21, 11). M Blocked (23, 10).
  6. `Up` x2 -> P(21, 9). M Blocked (22, 9).
  7. `Down` x4 -> Deliver M to (22, 14).
- **Action**: Execute Steps 1-2 (Left, Up, Up, Up).