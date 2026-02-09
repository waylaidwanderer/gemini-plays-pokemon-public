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
- Player: (15, 13).
- Murkrow: **MISSING** (Not at 20, 12).
- Goal: Check spawn point (7, 2).

## Strategy: Search & Rescue
- **Path**:
  1. Move West to (3, 13).
  2. Check Gate at (3, 8).
  3. If Locked: Stairs at (3, 14) -> B1F -> Stairs at (3, 2) -> B2F (7, 2).
  4. If Open: Walk North to (7, 2).
- **Hypothesis**: Murkrow resets to (7, 2) if the puzzle is "failed" or he gets too far.