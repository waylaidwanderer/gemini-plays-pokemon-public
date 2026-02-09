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
- Map: B1F (3_50).
- Player: (18, 15).
- Objective: Reach SE Stairs at (27, 14) to bypass Boss Door or find alternate route.
- Obstacle: Grunt at (21, 14) and potentially Gate/Wall at (23, 14).
- Connectivity:
  - Row 12 West (0-23) is SOLID WALL (TYPE_2889).
  - Row 12 East (24-29) is Walkable (TYPE_3fe2).
  - Row 14: Blocked by Grunt at (21, 14).
  - TYPE_2889 = Wall. TYPE_3fe2 = Floor.
- Action:
  1. Interact with Grunt at (21, 14).
  2. If defeated, check gate at (23, 14).
  3. If gate is locked/solid, backtrack.

## Murkrow Status
- Missing. Presumed at Start Area (7, 2) on B2F.