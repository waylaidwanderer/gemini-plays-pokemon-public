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
- Map: B2F (3_51).
- Player: (7, 4).
- Status: Guiding Murkrow.
- Murkrow: At (7, 3).
- Behavior Confirmed: Exact Mimicry (Player Down -> Murkrow Down).
- Plan:
  1. Move Right to (8, 4).
  2. Murkrow should move Right to (8, 3).
  3. Continue guiding East towards column 23.

## Murkrow Mechanics
- **Mimicry**: Moves in the SAME direction as the player.
- **Collision**: If blocked, it stays put (allowing desync).

## Murkrow Status
- Missing. Presumed at Start Area (7, 2) on B2F.