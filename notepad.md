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

## Strategy: The Column 23 Flank
- **Goal**: Use Column 23 (East) to circle around Murkrow.
- **Current**: P(21, 13). M(21, 12).
- **Plan**:
  1. `Right` x2 -> P(23, 13), M(23, 12). (Test Col 23 Openness).
  2. `Up` x2 -> P(23, 11), M(23, 10).
  3. `Left` x3 -> P(20, 11). M Blocked at (21, 10). M Stays (22, 10).
  4. `Down` x4 -> P(20, 15), M(22, 14).
  5. `Right` x2 -> P(22, 15). M Stays (22, 14).
  6. Interact Up.
- **Action**: Execute Steps 1-2 (Right, Right, Up, Up).