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
- Player: (3, 13).
- Murkrow: **MISSING** (Likely reset to (7, 2)).
- Obstacle: Row 12 is a solid wall (Verified by collision).
- Goal: Reach (7, 2) via B1F.

## Strategy: Search & Rescue
- **Path**:
  1. Stairs at (3, 14) -> B1F (3, 14).
  2. Walk to Stairs at (3, 2) in B1F.
  3. Stairs to B2F (7, 2).
  4. Search for Murkrow.
- **Hypothesis**: Murkrow resets to (7, 2) if the puzzle is "failed" or he gets too far.