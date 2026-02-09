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

## Strategy: The Validated Slide (Alignment)
- **Status**: P(18, 13). M(18, 11) or (18, 12).
- **Goal**: Reach P(22, 11), M(22, 10).
- **Logic**: Driving Murkrow North into the Grunt at (22, 9) forces alignment.
- **Plan**:
  1. `Right` x4 -> P(22, 13). M(22, 11).
  2. `Up` x2 -> P(22, 11). M(22, 9) [Blocked]. M Stays (22, 10).
  3. `Left` -> Start Desync P(21, 11).
- **Action**: Execute Alignment (Right x4, Up x2).