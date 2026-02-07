# Team Rocket HQ Status
## Critical Objectives
- **Primary**: Find path to B2F Northeast (Voice ID required).

## Tile Mechanics
- **TYPE_63e2 (Shop 2, 2 & 2, 3)**: Confirmed SOLID OBSTACLE. Appears to be a Cabinet hiding the stairs. Needs a trigger to move.

## Mechanic Discoveries
- **Security Switch (19, 11)**: Turned **ON**.
  - **Effect**: DISABLES floor traps (Voltorb/Geodude encounters).
  - **Effect**: Does NOT open Shutters at (15, 10).
  - **Effect on Warps**: Warp (19, 1) is inactive (Verified). Warp at (16, 7) is INERT (Verified Turn 32287). (12, 8) is a solid crate.

## Exploration Status
- **Computer Room (19, 8)**: Accessed via central corridor (Row 9).
  - Checking computer terminals for passwords/doors.
  - Computers at (19,5) and (18,5) confirmed inert.
- **Murkrow Chase**:
  - NOT at B1F (22, 9) (Visually confirmed Turn 32240).
  - Summary states it fled to B2F (22, 9).
  - Target: Reach B2F East Wing to find Murkrow and Boss Door.
- **East Wing**:
  - "Secret Stairs" (Shop 2, 3): Positioned at (3, 3). Interacting with Cabinet at (2, 3) to trigger stairs. Grunt at (4, 3) is passive.
  - "Back Stairs" (Shop 7, 3) <-> B1F (27, 2) (East Wing)
  - Switch at (22, 14) = Inert.
  - Statue at (24, 1) = Flavor/Inert.
- **West Wing**:
  - Shutters (15, 10) = Locked.
  - Grunt at (12, 10) = Blocking path (can be flanked).
  - Persian Statue (6, 1) = Confirmed Inert (Flavor text only).

## Leads
1. **Cabinet Trigger**: Investigate how to move the cabinet at (2, 2)/(2, 3).
2. **Computer**: Check terminals at (19, 7) and (18, 7).
3. **Murkrow**: Investigate sprite at B2F (7, 9).
- Cabinet at (2, 2) interaction: No response.
- **Secret Stairs Trigger**: Talk to Grunt at (4, 3). He acknowledges finding the stairs.
- Passwords learned (from history): "RATICATE TAIL", "HAIL GIOVANNI".
- Persian Statue at (6, 1) is definitely inert.
- Murkrow likely at B2F (22, 9).
- Row 15 Connectivity: B1F East Wing (Col 24+) is connected to Central/West area via a corridor at Row 15/16.
- B2F Navigation:
  - Stairs at (3, 14) connect to West side.
  - Corridor at Row 14 connects West (3, 14) to East (20, 14).
  - Target: Sprite at (7, 9) (West side).
  - Target: Boss Door at (23, 14) (East side).
- B1F Staircase Inventory: (7, 3) [Up to Shop], (27, 2) [Up to Shop], (3, 14) [Down to B2F].
- Hypothesis: Murkrow is at B2F (7, 9). Access might be blocked by walls.
- Critical Logic:
  - B2F (27, 14) contains stairs (Verified in XML).
  - Current position B2F (20, 14) is blocked from East side by Grunt at (21, 14).
  - Therefore, MUST access B2F East via B1F (27, 14).
  - Action Plan: Return to B1F -> Warp to East Wing -> Search B1F Southeast corner for stairs.
- Switch at (22, 14) confirmed inert (no text box).
- Re-investigating B2F West: I suspected a wall blocked (7, 9) from (3, 14), but I need to verify this physically. If (7, 9) is accessible, that's where the Murkrow is.
Mapping Note: TYPE_2889 is a solid wall/tree. Do not route through it.
- Map Discrepancy: XML shows B2F Stairs at (27, 14), but B1F (27, 14) appears to be a solid wall/dead end. Investigate if stairs are hidden or if map data is misleading.
- Navigation: Jed at (18, 12) blocks direct West path. Must flank via Row 13.
- Silver at B2F (21, 12) blocks the only visible path North from the southern corridor.
- Must find a way to B2F North (Row 9) from B1F (likely Northeast area).