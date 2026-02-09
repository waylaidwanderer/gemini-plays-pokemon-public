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
- **Player**: (21, 13).
- **Murkrow**: (21, 12). (Derived from mimicry).

## Strategy: The "Golden Path" (Verified Logic)
- **Goal**: P(22, 13), M(22, 14).
- **Path**:
  1. **Align**: `Right`, `Up`, `Up` -> P(22, 11), M(22, 10).
  2. **Desync 1 (Computer)**: `Left` -> P(21, 11). M Blocked (21, 10). Stays (22, 10).
  3. **Desync 2 (Extend)**: `Left` -> P(20, 11). M Blocked (21, 10). Stays (22, 10).
  4. **Desync 3 (Grunt)**: `Up` x2 -> P(20, 9). M Blocked (22, 9). Stays (22, 10).
  5. **Delivery**: `Down` x4 -> P(20, 13), M(22, 14).
  6. **Dock**: `Right` x2 -> P(22, 13). M Blocked (Door). Stays (22, 14).
  7. **Interact**: Face Down, A.

- **Action**: Execute Step 1 (Right, Up, Up).