# Team Rocket HQ (Mahogany Town)
## Objectives
- **Primary**: Open Boss Door on B2F (Requires Murkrow Voice + "Raticate Tail").
- **Secondary**: Reach Murkrow via B2F South Corridor (Row 16).
- **Tertiary**: Catch Murkrow (B2F 22,9).

## Mechanics & Traps
- **Switch at B1F (19, 11)**: Toggles Warp Trap destination.
  - **OFF**: Trap at (21, 10) -> Entrance (25, 14).
  - **ON**: Trap at (21, 10) -> Central Corridor (14, 12).
- **Warp Trap at B1F (21, 10)**: Currently set to send to (14, 12).
- **Locked Door (B2F)**: B2F (23, 14). Can be bypassed via gap in South Wall (Row 16).
- **Passwords**:
  - "Raticate Tail" (Entered at B1F 21,11).
  - "Hail Giovanni" (Likely needed for Boss Door).

## Map Connections
- **B1F (Map 3_51)**:
  - (3, 6) Stairs <-> B2F (3, 6) [West Middle] (Separate from NW and SW?)
  - (27, 14) Stairs <-> B2F (27, 14) [South East]
  - (3, 2) Stairs <-> B2F (3, 2) [North West]
  - (27, 2) Stairs <-> B2F (27, 2) [North East]
  - (3, 14) Stairs <-> B2F (3, 14) [South West]
- **B2F (Map 3_50)**:
  - **West Side Structure**: Likely 3 isolated pockets (North, Middle, South) separated by walls on B2F, requiring B1F transitions to hop between them.
  - **Middle Pocket (3, 6)**: Currently exploring. Checked South path.
  - **North Corridor**: Connects NW and NE stairs. (Isolated from Center).
  - **South Corridor (Row 16)**: Connects SW and SE stairs. (Likely access to Center/Murkrow).

## Current Plan
1. **Warp Strategy**: From B1F Entrance (25, 14), go to Warp Trap at (21, 10).
2. **Execution**: Step on trap.
   - If warped to **Central Corridor (14, 12)**: Explore North for stairs to B2F.
   - If warped to **Entrance (25, 14)**: Toggle Switch at (19, 11) then retry trap.
3. **Goal**: Reach B2F North-Central area (Murkrow location).
- **Discovery**: The "Central South" area (x<15, y>9) is a contained pocket reachable via the East Gap (15, 13) or Warp Trap.
- **Blockage**: North access is blocked by Shutter (14, 11) and Row 9 Wall.
- **Hypothesis**: A switch inside this pocket opens the Shutter at (14, 11), allowing access to Silver/Murkrow.
- **Findings**: Machines at (4,13), (6,13), (7,13) contain propaganda. Machine at (5,13) is physically inaccessible. No switches found in this area.
- **Plan**: Moving to B2F NE Stairs (27, 2) to attempt access to B2F North Corridor.
- **Reflection (Turn 26639)**:
  - **Status**: Leaving B1F South Pocket via Gap (15, 13).
  - **Hypothesis**: Access to Murkrow/Silver is via B2F North Corridor.
  - **Plan**: Go to NE Stairs (27, 2). Descend to B2F. Attempt to navigate West to reach the Central/North section. Re-verify if the path is truly blocked at x=23.
  - **Backup**: If blocked, check B2F East section thoroughly for switches or hidden paths.
- **Map Notes**:
  - **Gap**: (15, 13) connects East and West B1F.
  - **Barriers**: Row 12 (x<7) is solid `TYPE_2889`. Cannot walk behind machines.
  - **Trap Confusion**: Records show I warped from (5, 15) before. The "Trap" at (21, 10) might be a misunderstanding or a second trap.
- **Plan**: Test Warp Trap at (5, 15).
  - If Warped to Silver: Proceed.
  - If Warped to Entrance: Switch failed.
  - If No Warp: Proceed to Gap (15, 13) to reach North Pocket via B2F loop.
- **North Access**: To reach (2, 11) (Suspicious Tile) or NW Stairs, I must loop via B2F NE Stairs -> B2F NW Stairs.
- **Discovery**: Column 2 is a wall of trees, but there is a gap at (2, 16).
- **Hypothesis**: Column 1 is a hidden corridor leading North, potentially bypassing the Shutter.
- **Plan**: Navigate South to Row 16, then West to Column 1, then North.
- **Confirmation**: Column 1 is BLOCKED by a wall at Row 4 (TYPE_2889). The "Continuous Corridor" hypothesis was false.
- **Plan**: Walk South on B1F West side to reach SW Stairs (3, 14), then access B2F South Corridor.
- **Goal**: Access B2F North Section to reach Murkrow (22, 9).