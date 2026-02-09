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

## Strategy: The Column 19 Flank (Verified)
- **Goal**: P(22, 13), M(22, 14).
- **Current**: P(21, 13), M(21, 12).
- **Phase 1: Setup**
  1. `Up` -> P(21, 12), M(21, 11).
  2. `Right` -> P(22, 12), M(22, 11).
  3. `Up` -> P(22, 11), M(22, 10).
- **Phase 2: The Flank**
  4. `Left` x3 -> P(19, 11). M Blocked at (21, 10). Stays (22, 10).
  5. `Up` x2 -> P(19, 9). M Blocked at (22, 9). Stays (22, 10).
  6. `Down` x4 -> P(19, 13), M(22, 14).
  7. `Right` x3 -> P(22, 13). M Blocked at (23, 14). Stays (22, 14).
  8. Face Down, Interact.
- **Action**: Execute Phase 1 (Up, Right, Up).