# Team Rocket HQ (Mahogany Town)
## Objectives
- **Primary**: Find Murkrow (B2F Middle) for Boss Door password.
- **Secondary**: Find switch to disable alarms/shutters (likely in West Room computers or hidden corner).
- **Hypothesis**: "SlowpokeTail" password usage? Hidden switch in West Room?
- **Blockers**:
  - Central Shutter (15, 11) locked.
  - West Shutter (14, 10) locked.
  - "Mystery Blockages" at (9, 8) and (13, 8).
  - B2F West Corridor is a dead end.

## Key Locations & Findings
- **East Room**:
  - Hidden Path at (19, 8) leads to North computers (Row 4/5).
  - Crates at (27, 10) are empty/non-interactive.
  - Posters at (20, 10), (21, 10) are just the "Oath".
  - Computer at (19, 11) is a display ("Switch is OFF").
- **West Room**:
  - Isolated by Wall at Column 6 (except via Row 16?).
  - Persian Statue at (6, 1) is just a statue.
  - Trap-free path: Column 5 (y=2 to y=14) (Avoids Warp Traps, but has battles).
  - Warp Tile at (5, 15) -> (25, 2) (Entrance/Shop Exit).
  - Grunt at (2, 4): "Don't know where traps are" (Useless).
  - Grunt at (9, 3) is non-interactive/blocking path North.
- **B2F**:
  - Accessed via stairs at (3, 14) (South), (27, 14) (SE), (27, 2) (NE), (3, 2) (NW).
  - (3, 2) Stairs: Leads to isolated NW room on B2F (Connects to (3, 6)?).
  - Murkrow Location: B2F (22, 9) (NE Section). Requires access via Stairs at (27, 2).
  - West Corridor is isolated/dead-end.

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