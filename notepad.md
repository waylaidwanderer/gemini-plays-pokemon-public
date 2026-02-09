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

## Strategy: The Double-Block Offset
- **Goal**: Achieve Offset P(21, 9), M(22, 10) (M is +1, +1).
- **Current**: P(22, 13), M(22, 12).
- **Plan**:
  1. `Up` x2 -> P(22, 11), M(22, 10).
  2. `Left` -> P(21, 11). M Blocked at (21, 10) [Computer]. Stays (22, 10).
  3. `Up` x2 -> P(21, 9). M Blocked at (22, 9) [Grunt]. Stays (22, 10).
  4. `Down` x4 -> Slide M to (22, 14). P to (21, 13).
  5. `Right` -> P(22, 13). M Blocked at (23, 14).
  6. Interact Down.
- **Action**: Execute Steps 1-3 (Up, Up, Left, Up, Up).