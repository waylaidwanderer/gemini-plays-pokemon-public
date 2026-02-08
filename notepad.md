# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Immediate**: Turn Switch ON (Safety) and proceed to B2F via (3, 14).

## Exploration State
- **B1F (Current Floor)**
  - **West Wing**: Stairs at (3, 14) -> B2F South-West.
  - **East Wing**: Accessed via Warp (5, 15) -> (25, 2). Stairs at (27, 2) -> Shop.
  - **Switch**: (19, 11). Status: "Turned off" (Cannot toggle). Traps presumed ACTIVE.

- **B2F (Below)**
  - **Boss Door**: (23, 14). Requires Passwords.
  - **Passwords Known**: "RATICATE TAIL", "HAIL GIOVANNI".

## Map Notes
- **"Trap" Warps**: (12, 8) and (19, 1) warp to start (verified).
- **Statues**: Persian statues seem inert or alarm triggers.

## Next Steps
1. Turn Switch ON to disable floor traps.
2. Navigate to B1F Stairs at (3, 14).
3. Go to B2F and interact with Boss Door at (23, 14).
4. Enter Passwords: "RATICATE TAIL" and "HAIL GIOVANNI".
- **Boss Door Update**: Passwords "RATICATE TAIL" and "HAIL GIOVANNI" are not enough. Requires **Voice ID**.
- **Task**: Chasing Murkrow (Found at 22, 8). Need to lead it to... somewhere?
- **Murkrow Interaction**: Direct A-presses and bumping failed. Using tools to verify interactability and exact location.
- **Murkrow Status**: Chased from (21, 9) -> (7, 8) -> (7, 6) -> (9, 4) -> (10, 4). Currently perched on Computer at (10, 4).
- **Interaction Attempts**:
  - West (9, 4): Failed.
  - North (10, 3): Failed.
  - South (10, 5) A-press: Failed.
  - South (10, 5) Bump: Pending.
- **Switch (19, 11)**: "Turned off". Cannot interact. Likely requires a key or event (Murkrow?).
- **Murkrow Status**: Stuck at (10, 4). Interaction failed. Returning to try "flushing" it from different angles or checking the computer it's standing on.
- **Hypothesis**: The Murkrow needs to be chased to the B2F Boss Door to act as the Voice ID.
- **Map Note**: (11, 4) is a solid computer. Murkrow is at (10, 4). Open tiles: (9, 4), (10, 3), (10, 5).
- **Navigation Warning**: Scientist Jed is blocking (18, 12). BFS fails here. Must navigate around via (18, 13).
- **Strategy Update**: Murkrow interaction at (10, 4) seems stuck or complete. Abandoning for now.
- **Security Update**: Persian Statue at (6, 1) says "Its eyes are oddly shiny." No alarm triggered yet.
- **Plan**:
  1. Navigate to B1F Stairs at (3, 14).
  2. Go to B2F and interact with Boss Door at (23, 14).
  3. Check if "Voice ID" is satisfied by previous events.
  4. If locked, check for Jed or other triggers.
- **B2F Navigation**: Grunt at (21, 14) blocks direct path. Attempting to bypass via (21, 13).
- **Correction**: Stairs at B1F (27, 2) lead UP to the Shop (3_48).
- **Navigation Update**: Exited East Wing to Shop (3_48).
- **Navigation Update**: Path to East Wing Stairs at (7, 3) is blocked by a Defeated Grunt at (4, 3).
- **Action**: Manually navigating around the Grunt (Up -> Right -> Down) to reach the stairs.
- **Plan**:
  1. Enter East Wing via Shop Stairs (7, 3) -> B1F (27, 2).
  2. Locate Shutter/Switch in East Wing (Target: 15, 10 area).
  3. Open Shutter to access West Wing.
  4. Resume B2F Boss Door mission.
- **Goal**: Return to West Wing (B1F), verify "Useless Grunt" at (2, 4) and Switch at (19, 11).
- **Hypothesis**: The "Useless Grunt" or the Switch might have changed state or I missed something. Also checking for hidden items/switches in West Wing.
- **Murkrow Status**: Both B1F Murkrows (West & East) seem stuck.
- **Hypothesis**: Need to trigger something else (Switch? Grunt?) to move them.
- **Plan**:
  1. Return to West Wing.
  2. Check "Useless Grunt" at (2, 4).
  3. Re-examine Scientist Jed at (18, 12).
  4. Re-examine Switch at (19, 11).
- **Boss Door Check**: Door refuses to open. Text: "Only the boss knows the password."
- **New Plan**: The Murkrow on B1F was a dead end. Attempting to reach the Murkrow marked at B2F (22, 9).
- **Route**: B2F (3, 14) Stairs -> B1F (3, 14) -> B1F (5, 15) Warp -> B1F East Wing -> B1F (27, 2) Stairs -> B2F (27, 2).
- **Exploration Update**: Shutter at (15, 10) is CLOSED.
- **Pathfinding**: Direct South path is blocked. East side (Cols 24-25) appears open.
- **Action**: Flanking East to bypass the shutter and reach Switch at (19, 11) / Jed at (18, 12).
- **Goal**: Re-examine Switch. If it says "Turned off", determine if that means "Disabled" or "Currently Off".
- **Hypothesis**: If Security is OFF, maybe traps are inert? Need to verify.