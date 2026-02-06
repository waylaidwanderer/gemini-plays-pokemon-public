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
- **Murkrow**: Fled from B1F (7, 2). Believed to be in B2F Central Room (22, 9).
- **Route**: B1F (3, 2) -> B2F (3, 2) -> B2F North Corridor -> B2F (27, 2) -> B1F (27, 2).
- **Goal**: Reach B1F NE Room to find Hidden Switch #2.
- **Gate 1**: B2F (3, 8) locked. Bypassing via B2F North Corridor.
- **Shutters**: B1F (14, 11) confirmed LOCKED.
- **Stairs B1F (27, 2) <-> B2F (27, 2)**: East side.
- **Stairs B1F (3, 6) <-> B2F (3, 6)**: West Mid.
- **Stairs B1F (27, 14) <-> B2F (27, 14)**: South East.
- Hidden Switch found at B1F (19, 11) opened the path to the Executive.
- **Observation**: Row 13 in South West room is blocked by machines/walls (TYPE_1fdc, TYPE_2889). Gap appears to be at Column 8/9.
- **Password Acquired**: "HAIL GIOVANNI" (Voice ID).

- **Obstacle**: Grunt at B2F (4, 1) is a permanent blocker. Cannot pass.
- **Scientist Mitch**: Defeated.
### Investigation Log (B1F SW Room)
- Target: Hidden Switch #2.
- Checked (Row 14): (9, 14), (10, 14), (11, 14) [Inert].
- Checked (Row 11): (11, 11), (12, 11), (13, 11) [Inert].
- Checked (Row 13): Checking (9-11, 13).
- Checking Row 12 Corridor (Inner Face):
  - (9, 12): Checked N(9,11)/S(9,13) [Inert].
  - (10, 12): Checked N(10,11)/S(10,13) [Inert].
  - (11, 11): Checked (Inert).
- (11, 12): Checked N(11,11)/S(11,13) [Inert].
  - Result: No switch found in Inner Corridor.
- **Next Step**: Investigate Gap at (15, 13) and area behind shutters.
- **Secret Passage**: Confirmed at (19, 10). Connects Northern Corridor to Row 11.
- **Connection**: Appears to lead East into the SE Room (towards Scientist Ross).
- **Hypothesis**: This is the intended path to bypass the wall at (27, 10).
- **Hypothesis**: Must bring Murkrow to the door.
- **Murkrow Strategy**: Murkrow is at B2F (22, 9) (Central Room). Access is blocked from East. Must reach from West (behind Locked Gate).
- **Warp Trap at B1F (26, 9)**: DISABLED.
- Checking SE Room North Bank (Back Side):
  - Checked (23, 10), (22, 10), (21, 10), (20, 10). Result: Negative.
- Checking SE Room South Bank (North Face):
  - Checked (23, 13), (24, 13), (25, 13). Result: Negative.
### Investigation Status
- **B1F SE Room**: CLEARED. All machines checked. No switch.
  - Scientist Ross: Defeated.
  - Secret Passage: Found at (19, 10).
- **B1F SW Room**: CLEARED. All machines checked. No switch.
  - Scientist Mitch: Defeated.

### Current Objective
- Checking NE Room Aisle (Col 28):
  - Checked Rows 4-11. Result: Negative.
  - Checking Rows 12-15 (Col 29) now.
  - Checking Rows 9-11 (Col 27 - West Face) next.
- **Route**: Exit Aisle South at Row 15, then loop up to Col 26.

### Mechanics Verified
- **"Fake Machines"**: Tiles with machine graphics but `TYPE_3fe2` collision are WALKABLE. Used to hide secret passages (e.g., 19, 10).
- **Solid Machines**: `TYPE_2889` are standard collision.

### Route
- Use Secret Passage at (19, 10) to exit SE Room.
- Head East to (26, 9).
- **Murkrow**: Confirmed on B2F (Central Room).
- **Hypothesis**: Path behind Warp Trap leads to stairs accessing B2F Central Room.
- **Map Connectivity**: B2F East Corridor blocked at Row 10 (Wall). Must use B1F to travel between South East and North East.
- Machines at (4, 13), (6, 13), and (7, 13): Confirmed Oath machines. No switch.
- Floor tile at (3, 16) has a Geodude graphic but is walkable. Likely decoration or disabled trap.
- Computers at (9, 14) and (10, 14): Inert.
- Computer at (11, 14): Inert from Right side.
- Corridor at Col 15: Leads to Locked Shutters at (15, 11) and (15, 10).
### Area Status: B1F SW Room
- Needs investigation. Suspected location of Hidden Switch #2.
- Access via B1F SE Room (reached from B2F Stairs at 27,14).

### Key Locations
- **Trap**: B1F (26, 9). Leads to secret passage at (26, 10).
- **Switch #1**: Found at B1F (19, 11).
- **Boss Door**: B2F (23, 14). Needs Voice ID (Murkrow).