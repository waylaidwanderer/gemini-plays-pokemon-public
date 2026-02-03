# Team Rocket HQ (Mahogany Town)
## Objectives
- **Primary**: Open Boss Door on B2F (Requires Murkrow Voice + "Raticate Tail").
- **Secondary**: Catch Murkrow (currently in B1F North-East section).
- **Tertiary**: Defeat Grunt guarding stairs (B1F West).

## Map Structure
- **Map 3_50 (B2F)**:
  - North Corridor (Row 1): Connects NW Stairs (3, 2) and NE Stairs (27, 2).
  - South Corridor (Row 16): Connects SW Stairs (3, 14) and SE Stairs (27, 14).
  - East Corridor (Column 27): Blocked at Row 10 (Wall). Cannot travel directly between NE and SE stairs on B2F.
  - West Corridor (Column 3): Blocked mid-way.
- **Map 3_51 (B1F)**:
  - West Section: Accessible via NW Stairs (3, 2). Contains Persian Statues.
  - North-East Section: Accessible via NE Stairs (27, 2). Contains Silver & Murkrow.
  - South-East Section: Accessible via SE Stairs (27, 14). Contains Switch.

## Reflection (Turn 26471)
- **Progress**: Found Murkrow, got "Raticate Tail" password. Stuck on Boss Door and Switch puzzle.
- **Hygiene**: Map markers are updated. Notepad plan is current.
- **Strategy**: Trying to toggle switch at (19, 11). Movement is tricky because tiles are walkable.
- **Tools**: Existing tools are sufficient.

## Current Plan
1. **Toggle Switch**: Test interaction with Computer at (19, 11)/(19, 10) from multiple angles.
   - Sequence: Move Down to (19, 12), move Up to (19, 11) (facing Up), press A.
2. **Check Shutter**: If successful, check shutter at (14, 11).
3. **Warp Puzzle**: If switch fails, re-investigate floor tiles in Row 9/10 using `scan_surroundings`.
4. **Boss Door**: Return to B2F door if shutter opens.

## Mechanics & Notes
- **Warp Trap**: B1F (21, 9) is likely the entry point to the hidden B2F room (22, 9) where the Murkrow is trapped.
- **Solid Objects**: Computers at B1F (27, 12) are solid walls.

## Map Structure
- **East Section (Current)**: X > 15. Contains Switch (19, 11), Password PC (21, 11), Warp (21, 9).
- **Central Area**: X 7-14. Contains Silver (7, 2), Murkrow (7, 1), Shutter (14, 11).
- **West Section**: X < 6. Connected to B2F West Stairs.
- **Barriers**: Row 9 Wall, Column 6 Wall, Column 15 Wall (with Shutter).

## Key Items/Passwords
- Password 1: "Raticate Tail" (Obtained).
- Password 2: "Hail Giovanni" (Likely obtained).
- Requirement: Murkrow's Voice for Boss Door.