Pokemon Mansion Routing & Switches:
- Switch at 1F (18, 25) toggles global states.
- Switch at 3F (10, 4) toggles YELLOW shutters globally.
  - State A: 3F (15, 6)/(15, 7) OPEN, 3F (15, 10)/(15, 11) CLOSED. 1F (16, 7) CLOSED.
  - State B: 3F (15, 6)/(15, 7) CLOSED, 3F (15, 10)/(15, 11) OPEN. 1F (16, 7) OPEN.

- STAIRS & WARPS:
  - 1F (5, 10) <-> 2F (5, 10) (West Wing)
  - 2F (6, 1) <-> 3F (6, 1) (North Wing)
  - 1F (23, 22) <-> 2F (21, 23) (East Wing)
  - B1F (7, 10) -> 1F (7, 10) (One-way up from B1F West)

- DROP HOLES (DANGER):
  - 2F (7, 10) is an INVISIBLE drop hole. Falls to 1F (7, 10).
  - 3F (16, 14) is a drop hole. Falls to 2F (16, 14).

- *** CRITICAL ROUTING CONSTRAINTS ***
  - 2F (9, 4)/(9, 5) (Vertical Yellow Shutters): CLOSED in State A. OPEN in State B (Verified Turn 39415). This connects 2F East and 2F West.
  - 2F (18, 8)/(19, 8) (Yellow Shutter): OPEN in State A AND State B.
  - 2F (20, 5) (Dark Grey Shutter): CLOSED in State A. Likely a permanent wall.
  - 1F NORTH ACCESS: 1F North has been fully explored (x=1 to x=28) and empirically verified: there are NO stairs to 2F North here.
- 1F Layout notes:
  - 1F Northeast corridor hits a dead end at (28, 1) and turns South at x=26, 27.
- EMPIRICAL PROOF: The switch statue at 1F (2, 5) toggles the global shutter state.
- 1F Shutters & States:
  - 1F (9, 6)/(9, 7) (Vertical Yellow Shutters): OPEN in State A, CLOSED in State B. This is the ONLY East/West crossing on 1F!
  - 1F (24, 13)/(25, 13) (Yellow Shutter): CLOSED in State A. OPEN in State B.
  - 1F (21, 17) (Yellow Shutter): CLOSED in State B.
- The dark grey blocks on 1F (e.g. x=9, y=9 to y=15) are PERMANENT SOLID WALLS, not shutters.
- CURRENT MANSION STATE: B (Trapped on 1F East. Must reset to State A via switch at 1F 18,25)
- Path to 2F North:
  1. Ensure Mansion is State A. Go to 1F (5, 10) stairs -> 2F (5, 10).
  2. Walk to 2F (6, 1) stairs -> 3F (6, 1).
  3. Walk to 3F (10, 4) switch. Press it (Mansion is now State B).
  4. Walk back to 3F (6, 1) stairs -> 2F (6, 1).
  5. Walk to 2F (9, 4). The yellow shutter is now OPEN. Walk East through it to access 2F North-East and find the path to B1F North!
- 1F Wall at x=13: A solid wall blocks East/West movement between y=24 and y=26. Use the gap at y=22 to cross.
- EMPIRICAL TESTING: Bumping into (9, 7) and (9, 11) in current state to confirm they are solid.