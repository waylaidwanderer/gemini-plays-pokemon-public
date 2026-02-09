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
- **Player**: (21, 13).
- **Murkrow**: (21, 12). (Derived from mimicry).

## Strategy: The Validated Wide Flank
- **Goal**: P(20, 15), M(22, 14). Interact Up from (22, 15).
- **Current**: P(22, 13), M(22, 12).
- **Plan**:
  1. `Left` x2 -> P(20, 13), M(20, 12).
  2. `Up` -> P(20, 12), M(20, 11).
  3. `Right` x2 -> P(22, 12), M(22, 11).
  4. `Up` -> P(22, 11), M(22, 10).
  5. `Left` x2 -> P(20, 11). M Blocked at (21, 10). Stays (22, 10).
  6. `Down` x4 -> P(20, 15), M(22, 14).
  7. `Right` x2 -> P(22, 15).
  8. Face Up, Interact.
- **Action**: Execute Steps 1-3 (Left, Left, Up, Right, Right).