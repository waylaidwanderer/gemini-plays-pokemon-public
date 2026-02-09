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

## Strategy: The Column 19 Flank (Correction & Execution)
- **Status**: Game State shows P(22, 13). Previous move `Up, Right, Up` desynced or lagged?
- **Goal**: Reach P(22, 11), M(22, 10).
- **Correction**:
  1. `Up` x2 -> P(22, 11). M(22, 10).
- **Desync Phase**:
  2. `Left` x3 -> P(19, 11). M Blocked at (21, 10). Stays (22, 10).
  3. `Up` x2 -> P(19, 9). M Blocked at (22, 9). Stays (22, 10).
  4. `Down` x4 -> P(19, 13), M(22, 14).
  5. `Right` x3 -> P(22, 13). M(22, 14).
  6. Interact.
- **Action**: Execute Correction + Desync (Up, Up, Left, Left, Left).