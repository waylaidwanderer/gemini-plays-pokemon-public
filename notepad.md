# Team Rocket HQ (Mahogany Town)
## Map IDs
- **3_51**: B1F (Upper/Lower West, East Room).
- **3_50**: B2F (Boss Room, Murkrow, Silver).

## Objectives
- **Primary**: Find Murkrow (B2F Middle) for Boss Door password.
- **Secondary**: Find switch to disable alarms/shutters (likely in West Room computers or hidden corner).
- **Hypothesis**: "SlowpokeTail" password usage? Hidden switch in West Room?
- **Strategy**:
  - Cross to South via Secret Passage at (19, 10) / (19, 11).
  - Reach East Room and Stairs (27, 2).
  - Murkrow is in B2F NE.
  - If blocked, check Persian Statue at (12, 1) or Computers in North area.

## Key Locations & Findings
- **East Room**:
  - Hidden Path at (19, 8) leads to North computers (Row 4/5).
  - Crates at (27, 10) are empty/non-interactive.
  - Posters at (20, 10), (21, 10) are just the "Oath".
  - Computer at (19, 11) is a display ("Switch is OFF").
- **West Room**:
  - Isolated by Wall at Column 6 (except via Row 16?).
  - Persian Statue at (6, 1) is UNCHECKED (Correction: only (6, 6) was checked).
  - Trap-free path: None verified. Column 5 blocked by wall at Row 11.
  - Warp Tile at (5, 15) -> (25, 2) (Entrance/Shop Exit).
  - Grunt at (2, 4): "Don't know where traps are" (Useless).
  - Grunt at (9, 3) is non-interactive/blocking path North.
- **B2F**:
  - Accessed via stairs at (3, 14) (South), (27, 14) (SE), (27, 2) (NE), (3, 2) (NW).
  - West Room (Cols 1-5): Connects stairs (3, 2), (3, 6), and (3, 14). Isolated from East side by wall at Col 6.
  - Murkrow Location: B2F (22, 9) (NE Section). Requires access via Stairs at (27, 2).

## Action Plan
1. **West Room Statues**: Checked (6, 6) and (6, 13) - Nothing.
2. **Re-Check East Room**: 
   - Talking to Scientist Jed (18, 12) -> He warns about warp panel.
   - Next: Interact with Computer at (19, 11).
   - Then: Explore Hidden Path at (19, 8) or (26, 5) to North East area.
3. **Statue Alarms**: Last resort.
## Cleared/Inert Statues (B1F)
- West Room: (6, 1), (6, 6), (6, 13), (6, 14) [All Checked & Inert].
- East Room: (24, 1), (24, 5), (24, 6) [Alarm], (22, 14) [Inert/Already Hit?].

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
- **Escape Plan**:
  1. **B2F NW Room (Stairs 3,6)**:
     - Check for hidden switches on walls.
     - Re-examine the "Locked Door" at (3, 8).
     - Check if Ledge at (3, 4) is passable/interactive.
  2. **B1F West Room**:
     - Re-check Row 11 Wall.
     - Check Grunt at (9, 3) (Blocking path?).
  3. **Last Resort**: Go all the way back to B1F Entrance via Warp (5, 15) -> (25, 2) and re-explore East Room. (Wait, can I reach (5, 15)? No, blocked by Row 11 wall).
     - I can reach (5, 15) via stairs (3, 14) if I can open the door at B2F (3, 8).
     - So KEY is opening B2F (3, 8).