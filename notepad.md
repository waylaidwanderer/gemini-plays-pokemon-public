# Team Rocket HQ (Mahogany Town)
## Objectives
- **Primary**: Open Boss Door on B2F (Requires Murkrow Voice + "Raticate Tail").
- **Secondary**: Find Switch for Shutter to access B1F Center.
- **Tertiary**: Catch Murkrow.

## Map Structure & Connections
- **Vertical Segregation**: The map is divided into isolated vertical sections (West, Center, East).
- **West Section**:
  - **NW Stairs (3, 2)**: Connects B1F NW <-> B2F North Corridor.
  - **West Mid Stairs (3, 6)**: Connects B1F West <-> B2F West Pocket (Dead End).
  - **SW Stairs (3, 14)**: Connects B1F SW <-> B2F South Corridor.
- **East Section**:
  - **NE Stairs (27, 2)**: Connects B1F NE <-> B2F North Corridor.
  - **SE Stairs (27, 14)**: Connects B1F SE <-> B2F South Corridor.
- **Central Section (Goal)**:
  - **B1F Center**: Contains Silver, Murkrow, and potentially the Boss Door switch.
  - **Access**: Currently blocked by shutters/walls.
  - **Entry Hypothesis**: Must be accessed via a Warp Trap or a hidden switch in the "Trap Room" on B1F East.

## Trap Room Investigation (B1F East)
- **Goal**: Find switch to open Shutter (14, 11) or disable Warp Trap (21, 11).
- **Mechanic**: Computers at row ends (x=19, x=26) are **FALSE/WALKABLE**.
- **Checklist**:
  - [x] Acquired "RATICATE TAIL".
  - [x] Acquired "SLOWPOKETAIL".
  - [ ] Acquire Murkrow (Voice required for Boss Door).
  - [ ] Find path to B1F Center (likely via switch in B1F East/Trap Room).
  - [ ] Open Boss Door at B2F (23, 14).

## Key Items & Passwords
- **Password 1**: "Raticate Tail" (Found, Entered).
- **Password 2**: "SLOWPOKETAIL" (Found).
- **Objective**: Use passwords at the Boss Door.
- **Correction**: Computer at (26, 10) is SOLID. The "False Computer" passage might be in the NE Room (x=19?).
- **Map Note**: B1F SE Room explored. Dead end. Wall at x=18/19 blocks access to Center.
- **Plan**: Go to B2F, head North, take NE Stairs to B1F NE Room (False Computer search).
- **Anomaly**: In Turn 26800, moving West from (19, 1) seemingly warped me to (5, 1) past the wall at x=6. This suggests a one-way warp or a screen transition I missed.
- **Plan**: Use B2F to cross back to the East side (NE Stairs), then investigate the NE room thoroughly for the "False Computer".
- **Correction**: Confirmed B1F (3, 6) is a dead end segment (blocked North by ledge, South by locked door).
- **Plan**: Return to B2F via stairs at (3, 6).
- **Plan**: Navigate South on B2F to (3, 14).
- **Plan**: Traverse B2F South Corridor East to (27, 14), then North to NE Stairs (27, 2).
- **Goal**: Reach B1F NE Room via B2F NE Stairs.
- **Risk**: Potential warp tiles in the North Corridor (y=1). In Turn 26800, moving West from (19, 1) warped me to (5, 1). Moving East might be safe or trigger a trap.
- **Hypothesis**: The "False Computer" passage is in the B1F Trap Room/NE Area. Need to find a way in.
- **Map Note**: B1F West Corridor is segmented by a wall at y=4. (3, 2) is isolated from (3, 6).
- **Observation**: There is a door at (3, 8). Need to check if it opens.
- **Map Discrepancy**: Mental Map lists (3, 11) as `TYPE_2889` (Wall), but visually it appears to be a corridor. This caused BFS to fail.
- **Plan**: Manually test connectivity at (3, 11) by moving South. If blocked, the West strip is segmented.
- **Blockage Alert**: Grunt encountered near B1F (3, 1) who blocks the path East. Dialog suggests he's defeated or passive, but he remains an obstacle.
- **Plan**: Test B2F (3, 11) wall. If solid, re-examine B1F North Corridor or search for hidden switches in West Mid pocket.
- **Status**: Confirmed on B1F (3_50) at (3, 2). Warp successful.
- **Plan**: Traverse B1F North Corridor East to (18, 2) to bypass the Grunt and avoid the suspected warp trap at (19, 1).
- **Goal**: Reach the NE "Trap Room" to find the secret switch for the Boss Door/Shutters.
- **Note**: Keeping to Row 2 (Bottom Lane) to avoid obstacles.
- **Correction**: Row 2 on B1F is BLOCKED by walls from x=6 to at least x=15. Must use Row 1.
- **Plan**: Navigate East on Row 1 to (17, 1).
- **Hazard**: Suspected warp trap at (19, 1).
- **Hypothesis**: The trap might be avoidable if Row 2 opens up near x=18, or if it's one-way.
- **Goal**: Reach B1F NE Room (Trap Room) to find the secret switch.