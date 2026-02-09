# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision Rules**:
  - P Blocked: Murkrow Stays.
  - Chase Blocked: P cannot move into M's tile even if M moves away (parallel movement fails check).

## Current State
- Player: (20, 13).
- Murkrow: (20, 12).

## Strategy: Reset & Verify
- **Goal**: Move to (22, 13) then test (22, 15) atomically.
- **Execution**:
  1. `Right` x2 -> P(22, 13), M(22, 12).
  2. `Down` -> P(22, 14), M(22, 13).
  3. `Down` -> P(22, 15)? Check walkable.
  4. If walkable: `Down` -> P(22, 16). `Up` -> Talk.