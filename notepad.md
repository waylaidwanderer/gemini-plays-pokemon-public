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

## Strategy: The Grand Flank (Verified)
- **Goal**: Place M South of P using Col 19 & Grunt/Desk Blocks.
- **Current**: P(20, 14), M(20, 13).
- **Phase 1: Setup P(22, 11), M(22, 10)**
  1. `Left` -> P(19, 14), M(19, 13).
  2. `Up` x2 -> P(19, 12), M(19, 11).
  3. `Right` x3 -> P(22, 12), M(22, 11).
  4. `Up` -> P(22, 11), M(22, 10).
- **Phase 2: Desync**
  5. `Left` x3 -> P(19, 11). M Blocked (21, 10). Stays (22, 10).
  6. `Up` x2 -> P(19, 9). M Blocked (22, 9). Stays (22, 10).
- **Phase 3: Delivery**
  7. `Down` x4 -> P(19, 13), M(22, 14).
  8. `Right` x3 -> P(22, 13). M Stays (22, 14).
  9. Interact Down.
- **Action**: Execute Phase 1 (Left, Up, Up, Right, Right).