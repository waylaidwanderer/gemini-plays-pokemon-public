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
- Map: B2F (3_50).
- Player: (3, 14).
- Status: Arrived from B1F via stairs.
- Goal: Check if Wall at (3, 12) is passable (opened by B1F switch).
- Logic:
  - B1F Switch at (6, 1) was pressed.
  - If B2F (3, 12) is still a wall, the switch likely opened the Gate at B1F (3, 8).
- Plan:
  1. Move North to check (3, 12).
  2. If blocked, return to B1F.
  3. Navigate to B1F (3, 8) to check the gate.

## Murkrow Status
- Missing. Presumed at Start Area (7, 2) on B2F.