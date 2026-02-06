# Team Rocket HQ (Mahogany Town)
## Map IDs
- **3_51**: B1F (Main Floor).
- **3_50**: B2F (Basement).

## Current Strategy
1. **Defeat Executive**: Battle the Rocket Executive in the Hidden Office (B1F).
2. **Get Intel**: Learn the password or Murkrow's location.
3. **Capture Murkrow**: Find access to B2F Center Room.
4. **Boss Door**: Use passwords "RATICATE TAIL" and "HAIL GIOVANNI" at B2F (23, 14).

## Tile Mechanics
- **TYPE_8564 (Stairs/Warps)**: Walking ONTO this tile triggers a warp. EXCLUDE from pathfinding when navigating on the same floor.

## Status & Intel
- **Murkrow**: Located at B1F (7, 2). Approach from South via gap at (6, 10), accessible from West side (Stairs 3, 2).
- **Route**: Use B2F North Corridor (Row 1) to cross from West (3, 2) to East (27, 2).
- **Gate 1**: B2F (3, 8) locked. Bypassing via B2F North Corridor.
- **Shutters**: B1F (14, 11) confirmed LOCKED.
- **Stairs B1F (27, 2) <-> B2F (27, 2)**: East side.
- **Stairs B1F (3, 6) <-> B2F (3, 6)**: West Mid.
- **Stairs B1F (27, 14) <-> B2F (27, 14)**: South East.
- Hidden Switch found at B1F (19, 11) opened the path to the Executive.
- **Observation**: Row 13 in South West room is blocked by machines/walls (TYPE_1fdc, TYPE_2889). Gap appears to be at Column 8/9.
- **Password Acquired**: "HAIL GIOVANNI" (Voice ID).

- **Obstacle**: Grunt at B2F (4, 1) is a permanent blocker. Cannot pass.
- **Machine at (7, 13)**: Confirmed as Oath machine. No switch.
- **Boss Door Status**: LOCKED. Requires "Voice ID".
- **Hypothesis**: Must bring Murkrow to the door.
- **Murkrow Strategy**: Murkrow is at B2F (22, 9) (Central Room). Access is blocked from East. Must reach from West (behind Locked Gate).
- **Warp Trap Hypothesis**: The Warp Trap at B1F (26, 9) might transport me to the isolated B1F South area, which connects to the B2F West area behind the gate.
- **Current Plan**:
  1. Go to B1F via Stairs at B2F (27, 14).
  2. Intentionally trigger Warp Trap at B1F (26, 9).
  3. Navigate B1F South/West to find stairs to B2F Central area.
  4. Catch Murkrow.
- **Map Connectivity**: B2F East Corridor blocked at Row 10 (Wall). Must use B1F to travel between South East and North East.