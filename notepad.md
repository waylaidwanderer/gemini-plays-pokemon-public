# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Validated Slide (Reset & Setup)
- **Goal**: Desync at P(21, 11), M(22, 10).
- **Assumption**: P(22, 13), M(22, 12). (Or Reset to it).
- **Sequence**:
  0. `Down`, `Up` -> Ensure P(22, 13), M(22, 12).
  1. `Left` -> P(21, 13), M(21, 12).
  2. `Up` -> P(21, 12), M(21, 11).
  3. `Right` -> P(22, 12), M(22, 11).
  4. `Up` -> P(22, 11), M(22, 10).
  5. `Left` -> P(21, 11). M Blocked at (21, 10). M Stays (22, 10).
- **Action**: Execute Sequence.