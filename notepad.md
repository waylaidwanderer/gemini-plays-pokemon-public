# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14). Requires Voice ID (Have) and Password ("HAIL GIOVANNI").
- **Secondary**: Find Murkrow at B1F (7, 2).

## Map Knowledge
- **B2F East Wing**: Accessed via NE Stairs (27, 2) or SE Stairs (27, 14).
- **B2F West Wing**: Accessed via NW Stairs (3, 2).
- **Connection East-West**:
  - B2F Row 2: Blocked at (15, 2).
  - B2F Row 11: Blocked by Shutters.
  - B2F Row 13: Open Gap at (15, 13).
- **Secret Passage**: False Computer at B2F (19, 10) connects Central Room to North Corridor.
- **B1F Navigation**:
  - Row 1 Blocked at (6, 1) by Fake Wall.
  - Murkrow is at (7, 2), East of the blockage. Accessible via NE Stairs.

## Route
1. Navigate B2F to NE Stairs (27, 2).
2. Take Stairs to B1F (27, 2).
3. Walk West on B1F to Murkrow (7, 2).
- Navigation Logic (Turn 33939):
    - Problem: Target (22, 5) and Murkrow (22, 9) are in the "North Center" block (Cols 7-22, Rows 3-11).
    - Obstacle: Row 12 appears solid, blocking South access. Cols 6/23 appear solid, blocking East/West access.
    - Hypothesis: Entry is via the West Side.
    - Plan: Attempt to cross "Fake Wall" at (6, 1) to enter West Side. Then check for Warps (e.g., (3, 6)) or other entries.
    - Current Position: (24, 1). Goal: (5, 1).