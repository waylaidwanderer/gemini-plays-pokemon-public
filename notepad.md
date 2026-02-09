# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow COPIES player's movement input.
- **Collision**:
  - P Blocked: Murkrow MOVES (Desync Source).
  - M Blocked: Murkrow STAYS.

## Current State
- Player: (21, 13).
- Murkrow: **MISSING** (Not visible at expected coords).
- Door: Checking status.

## Strategy: Recovery
- **Goal**: Check Door. If locked, find Murkrow.
- **Sequence**:
  1. `Right` -> P(22, 13).
  2. `Down` -> P(22, 14).
  3. `Right` -> Face Door.
  4. `A` -> Interact.
  5. If locked, execute search pattern (likely West or reset).