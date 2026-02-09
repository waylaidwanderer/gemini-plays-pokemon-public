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
- Player: (6, 2).
- Status: Statue at (6, 1) has "shiny eyes" but no switch prompt. Stairs at (3, 2) are missing.
- Murkrow: Missing (B2F).

## Strategy: Reset & Rescue
- **Concept**: If I can't find the B1F->B2F(North) stairs, I will exit the HQ and re-enter. This should spawn me at the entrance, revealing the location of the stairs.
- **Path**:
  1. Go South to Warp at (5, 15).
  2. Warp to East Side (25, 2).
  3. Exit via Stairs at (27, 2) to Souvenir Shop.
  4. Re-enter HQ.
  5. If spawned at (3, 2), take stairs down to B2F (7, 2).
  6. Find Murkrow.