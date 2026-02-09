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
- Player: (24, 12).
- Status: Relocating to West Side.
- Goal: Check Stairs at (3, 2) (Northwest) to see if Switch at (24, 1) opened them.
- Logic:
  - I haven't checked (3, 2) since pressing the switch.
  - (3, 2) is the standard route to B2F (7, 2).
  - If (3, 2) fails, check (3, 14).
- Path:
  1. Left to (9, 12).
  2. Up to (9, 3) (Through Gap).
  3. Left to (3, 2).

## Murkrow Status
- Missing. Presumed at Start Area (7, 2) on B2F.