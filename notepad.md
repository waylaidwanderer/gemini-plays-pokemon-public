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

## Strategy: The Grand Circle (Setup Phase)
- **Goal**: Reach P(22, 11), M(22, 10).
- **Current**: P(22, 13), M(22, 12).
- **Plan**:
  1. `Left` -> P(21, 13), M(21, 12).
  2. `Up` -> P(21, 12), M(21, 11).
  3. `Right` -> P(22, 12), M(22, 11).
  4. `Up` -> P(22, 11), M(22, 10).
- **Next**: `Left` x3 to desync.
- **Action**: Execute Setup.