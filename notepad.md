# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Mechanics (Verified)
- **Mimicry**: Murkrow generally moves in the *same direction* as the Player.
- **Obstacles**: Wall hits cause desync.
- **Tether/Range**: Unclear. Dialogue did not immediately trigger follow on "Down" move.
- **Current State**: Player Moving to (7, 3). Murkrow at (7, 2).

## Plan: Gap 1 Compression (Retry)
1. Move **Up** to (7, 3).
   - If M moves to (7, 1) -> Gap 2.
   - If M stays at (7, 2) -> Gap 1.
2. If Gap 1 (P at 7, 3; M at 7, 2):
   - Move **Down** to (7, 4). Check follow.
3. If Gap 2 (P at 7, 3; M at 7, 1):
   - Move **Up** to (7, 2). M blocked at (7, 0). Gap 1.
   - Then Move **Down**.

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (15, 13) Gap / (15, 12) Floor.
  - (14, 11) Locked Shutter.