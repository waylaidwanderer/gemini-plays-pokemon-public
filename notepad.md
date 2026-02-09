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
- Player: (28, 9).
- Status: Leaving North-East Dead End.
- Insight: Row 10 is a wall. Cannot go South from NE corner.
- Insight: Wall at x=23 blocks access to Grunt at (22, 5) from East.
- Plan:
  1. Go North to Row 1 (Corridor).
  2. Go West to reach Central Area.
  3. Go South to engage Grunt at (22, 5).
  4. Defeat him and check for switches.

## Murkrow Status
- Missing. Presumed at Start Area (7, 2) on B2F.
- Note: BFS failed repeatedly to path from (28, 6) to (26, 13). Path seems clear visually and in XML. Using manual movement.