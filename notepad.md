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
- Status: Switch at B1F (6, 1) ACTIVATED.
- Goal: Verify if Wall at B2F (3, 12) is passable.
- If blocked: Return to B1F and check Gate at (3, 8).
- Hypothesis:
  1. Switch opens B2F (3, 12).
  2. Switch opens B1F (3, 8).
  3. Switches reset on map exit, need to activate BOTH (6, 1) and (24, 1) without leaving.

## Murkrow Status
- Missing. Presumed at Start Area (7, 2) on B2F.