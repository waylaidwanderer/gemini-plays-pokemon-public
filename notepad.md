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
- Map: B1F (3_49).
- Player: (27, 14).
- Status: Confirmed NO Stairs at (27, 14).
- Goal: Reach Stairs at (3, 14) (Southwest).
- Logic:
  - (3, 14) is `TYPE_8564` (Stairs/Exit).
  - I previously called it a "Dead End" but might have been wrong or blocked by a gate.
  - Switch at (24, 1) is ON. This might have opened the gate at (3, 14).
- Path:
  1. North to Row 5.
  2. West to (9, 5).
  3. North to (9, 3).
  4. West to (3, 3).
  5. South to (3, 14).

## Murkrow Status
- Missing. Presumed at Start Area (7, 2) on B2F.