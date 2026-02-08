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
- Navigation Logic (Turn 33952):
    - Current: B2F (3, 2) (Mistakenly went down stairs).
    - Goal: Activate Persian Statue Switch at B1F (24, 6).
    - Action: Return to B1F immediately.
    - Route on B1F:
        1. From B1F (3, 2), go North to Row 1.
        2. Walk East along Row 1 to Col 24.
        3. Walk South to (24, 5).
        4. Interact with Statue at (24, 6).
    - Note: This path relies on the "Fake Wall" at B1F (6, 1) being passable (Confirmed).
- Reflection (Turn 33955):
    - Reached Persian Statue at B1F (24, 6) via North/East perimeter to avoid alarms.
    - Action: Activating switch to disable security (hopefully).
    - Threat: Grunt at (22, 5) is close but hasn't engaged yet.
    - Next: Once security is down, move West to Murkrow (7, 2).