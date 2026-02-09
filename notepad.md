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

## Strategy: The Validated Flank (Full Sequence)
- **Goal**: P(19, 9), M(22, 10).
- **Current**: P(22, 13), M(22, 12).
- **Sequence**:
  1. `Left` -> P(21, 13).
  2. `Up` -> P(21, 12).
  3. `Right` -> P(22, 12).
  4. `Up` -> P(22, 11). M(22, 10).
  5. `Left` x3 -> P(19, 11). M Stays (22, 10).
  6. `Up` x2 -> P(19, 9). M Stays (22, 10).
- **Action**: Execute Alignment & Desync (Left, Up, Right, Up, Left, Left, Left).