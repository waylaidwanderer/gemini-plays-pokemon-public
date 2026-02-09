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
- Player: (8, 4).
- Murkrow: (8, 3) (Visual Confirmation).
- Goal: Guide Murkrow East to Boss Door (23, 14).
- Constraint: Walls at x=11 block Row 3 & 4.
- Plan:
  1. Move Right to (9, 4). (Murkrow -> 9, 3).
  2. Move Right to (10, 4). (Murkrow -> 10, 3).
  3. Move Down to (10, 5). (Murkrow -> 10, 4).
  4. Move Right to bypass Wall at x=11.

## Murkrow Mechanics
- **Mimicry**: Exact copy of input.
- **Collision**: Wall blocks movement, causing desync if player moves but Murkrow doesn't.

## Murkrow Status
- Missing. Presumed at Start Area (7, 2) on B2F.