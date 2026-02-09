# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow COPIES player's movement input.
- **Collision**:
  - P Blocked: Murkrow MOVES (Desync Source).
  - M Blocked: Murkrow STAYS.
  - Overlap: Possible if P blocked and M moves into P's tile.

## Current State
- Player: (21, 13) (After Left/Down).
- Murkrow: (20, 13) (Predicted).
- Grunt: (21, 14) (Blocking).

## Strategy: The Overlap Maneuver
- **Sequence**:
  1. `Left` -> P(21, 13). M(20, 12). (Done)
  2. `Down` -> P Blocked (Grunt). M(20, 13). (Done)
  3. `Right` -> P(22, 13). M(21, 13).
  4. `Right` -> P Blocked (Wall). M(22, 13) (OVERLAP!).
  5. `Down` -> P(22, 14). M(22, 14).
  6. `Right` -> Face Door.
  7. `A` -> Open.