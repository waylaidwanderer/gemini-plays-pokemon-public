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
- **Player**: (22, 14).
- **Murkrow**: (22, 13).
- **Status**: Trapped.

## Strategy: The Grand Circle (Column 19)
- **Goal**: Circle around Murkrow using the open space at x=19.
- **Path**:
  1. **Escape**: `Up` -> P(22, 13), M(22, 12).
  2. **Setup**: `Left`, `Up`, `Right`, `Up` -> P(22, 11), M(22, 10).
  3. **Desync X**: `Left` x3 -> P(19, 11). M Blocked at (21, 10). M(22, 10).
  4. **Desync Y**: `Up` x2 -> P(19, 9). M Blocked at (22, 9). M(22, 10).
  5. **Realign**: `Down` x2 -> P(19, 11). M(22, 12).
  6. **Stack**: `Right` x3 -> P(22, 11). M Blocked at (23, 12). M(22, 12).
  7. **Finish**: `Down` x2 -> P(22, 13), M(22, 14).
- **Action**: Execute Escape & Setup (Steps 1-2).