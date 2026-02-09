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
- Player: (22, 13).
- Murkrow: (22, 12).

## Strategy: The Final Sequence
- **Goal**: P(22, 14), M(22, 13). Interact with M, then Door.
- **Execution**:
  1. `Down` -> P(22, 14), M(22, 13).
  2. `Up` -> P blocked by M (Faces Up). M stays (due to P block).
  3. `A` -> Interact with Murkrow (Voice Check?).
  4. `Right` -> Face Door. M blocked by Wall.
  5. `A` -> Interact with Door.