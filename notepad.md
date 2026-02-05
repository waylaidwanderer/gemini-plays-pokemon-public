# Team Rocket HQ (Mahogany Town)
## Map IDs
- **3_51**: B1F (Upper/Lower West, East Room).
- **3_50**: B2F (Boss Room, Murkrow, Silver).

## Objectives
- **Primary**: Find Murkrow (B2F Middle) for Boss Door password.
- **Secondary**: Find switch to disable alarms/shutters (likely in West Room computers or hidden corner).
- **Passwords**:
  - "RATICATE TAIL" (Confirmed).
  - "SLOWPOKETAIL" (Possible).
  - "HAIL GIOVANNI" (Confirmed from Murkrow).
  - Boss Door requires TWO. We have them!
- **Boss Door Infiltration**:
  1. Status: At (24, 14). Door at (23, 14) says "Too bad for you." (Access Denied).
  2. Action: Try bottom door tile (23, 15).
  3. Contingency: If that fails, assume "RATICATE TAIL" flag is missing.
  4. Plan B: Return to B1F and speak to Defeated Grunt at (4, 1).
  5. Passwords: "RATICATE TAIL" (Need to Re-Confirm?), "HAIL GIOVANNI" (Confirmed).

## Key Locations & Findings
- **East Room**:
  - Hidden Path at (19, 8) leads to North computers (Row 4/5).
  - Crates at (27, 10) are empty/non-interactive.
  - Posters at (20, 10), (21, 10) are just the "Oath".
  - Computer at (19, 11) is a display ("Switch is OFF").
- **West Room**:
  - Split into North (Rows 2-10) and South (Rows 12-16) by Wall at Row 11.
  - Access to Hidden Office via Fake Wall at (10, 9).
  - **Hidden Office**:
    - Murkrow (Password: "HAIL GIOVANNI").
    - Rocket Executive (Defeated).
    - Bookshelf at (12, 1) contains "Oath".
  - Gap at (6, 10) connects North West Room to Central Corridor.
  - Shutters at (15, 10) and (14, 11) are LOCKED.
- **B2F Navigation Analysis**:
  - **East Strip (Cols 24+)**: Open up to Row 11. Row 10 blocked by Wall/Computers.
  - **Middle Area (Cols 7-23)**: Open at Row 15/16. Blocked at Row 12 (Solid Wall).
  - **West Area (Cols 1-6)**: Isolated by Wall at Col 6.
  - **Problem**: Row 12 blocks Middle approach. Row 10 blocks East approach. Wall at (23, 11) prevents switching lanes between Row 10/12.
  - **Hypothesis**: Secret passage in Row 10 East (Computer?), or Door at (20, 10)/(21, 10) opens from North?
  - **Action**: Check Row 10 East for hidden path. If failed, check B1F Warps again.

## Action Plan
1. **West Room Statues**: Checked (6, 6) and (6, 13) - Nothing.
2. **Re-Check East Room**: 
   - Talking to Scientist Jed (18, 12) -> He warns about warp panel.
   - Next: Interact with Computer at (19, 11).
   - Then: Explore Hidden Path at (19, 8) or (26, 5) to North East area.
3. **Statue Alarms**: Last resort.
## Cleared/Inert Statues & Computers (B1F)
- West Room Statues: (6, 6), (6, 13), (6, 14) [Inert]. (6, 1) [Checked-Inert].
- Hidden Office: (12, 1) [Bookshelf-Oath], (10, 1) [Computer-Oath].
- Checking Now: (11, 1), (13, 1), (14, 1).
- East Room Statues: (24, 1), (24, 5), (24, 6) [Alarm], (22, 14) [Inert].

## Investigation Status
- **Switch Mystery**: Computer says "Switch is OFF".
  - Possibility A: Need to turn it ON (find switch).
  - Possibility B: "Switch is OFF" means the security is active (bad state).
  - Fact: Activated switch at (22, 14).
  - Action: Find SECOND switch. Check all statues again or look for hidden wall switches.
- **Missing Stairs**: Summary said (27, 14) had stairs. It was empty.
- **Action**: Check Computer (19, 11). Then use Python to find ALL warps/stairs on map.
  - Code Analysis: Stairs ONLY at (27, 2) [Exit] and (3, 14) [West].
  - Conclusion: Access to rest of base MUST be via (3, 14) or a specific Warp.
  - Action: Re-explore B2F West Corridor carefully. Look for hidden doors or switches.
- **CRITICAL DISCOVERY**: Row 9 in Central Corridor (Cols 6-15) is a SOLID WALL. This separates the North Central area (with Statue at 12,1) from the South Central area (Row 10).
- **Consequence**: I am trapped in the Upper West Room + Row 10 Corridor loop.
- **North Strip (Row 1-3)**: Verified clear. No statue at (12, 1).
- **Murkrow Access Plan (South Loop)**:
  - **Status**: At B1F (27, 14). Preparing to descend to B2F SE.
  - **Path**:
    1. Descend Stairs at (27, 14) to B2F.
    2. Go West along Row 15/16.
    3. Find way North to Murkrow (22, 9).
- DISCOVERY: Tile (14, 1) is visually a Bookshelf but logically TYPE_3fe2 (Walkable). Potential Hidden Passage!