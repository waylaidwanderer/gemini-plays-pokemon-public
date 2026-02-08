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
- **Murkrow (East Wing)**: Found at B1F (22, 8). Interaction from South (22, 9) failed (Bump & A).
- **Strategy**: Flanking to North side (22, 7) to interact from behind.
- **Goal**: Chase this Murkrow to the Boss Door.
- **Boss Door Check**: Door refuses to open. Text: "Only the boss knows the password."
- **New Plan**: The Murkrow on B1F was a dead end. Attempting to reach the Murkrow marked at B2F (22, 9).
- **Route**: B2F (3, 14) Stairs -> B1F (3, 14) -> B1F (5, 15) Warp -> B1F East Wing -> B1F (27, 2) Stairs -> B2F (27, 2).