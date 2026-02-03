# Team Rocket HQ (Mahogany Town)
## Objectives
- **Primary**: Open Boss Door on B2F (Requires Murkrow Voice + "Raticate Tail").
- **Secondary**: Find Hidden Switch in B1F NE Room to open Shutters/Boss Door.
- **Tertiary**: Catch Murkrow.

## Map Structure
- **IDs**: `3_49`/`3_51` = B1F. `3_50` = B2F.
- **B1F**: Divided East/West by Wall at Col 15. Connected via Gap at Row 13.
- **B2F**: Center Boss Door (Locked). West/East sections connected via B1F.

## Current Status
- **Location**: B1F NW Corner (2, 3).
- **Items**: "RATICATE TAIL", "SLOWPOKETAIL".
- **Missing**: Murkrow Voice.
- **Action**: Interrogating Grunt at (2, 4).
- **Next**: Investigate "Traps" south of (2, 4).

## Investigation Log
- **Map Structure**: B1F West Side is divided by a wall at Row 11.
- **Hypothesis**: Use B2F West Corridor to bypass the wall.
  - Path: B1F (3, 14) [Stairs] -> B2F (3, 14) -> North to B2F (3, 6) [Stairs] -> B1F (3, 6).
- **Current Action**: Moving North on B2F from (3, 14) to (3, 6).
- **Hazard**: B2F (2, 8) and (3, 8) are `TYPE_63e2` (Traps/Doors).
- **Plan**: Bypass traps via Col 1 if possible.