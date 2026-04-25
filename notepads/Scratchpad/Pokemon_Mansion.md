Pokemon Mansion Routing & Switches:

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
- 1F Central/South Layout (Empirical update):
  - A wall of shutters and statues exists at y=16.
  - (13, 16): Dark Grey Shutter
  - (14, 16) to (15, 17): Statues
  - (16, 16) to (17, 16): Yellow Shutters
  - (18, 16) to (19, 17): Statues
  - (20, 16): Dark Grey Shutter
  - Currently (State B): (13,16), (16,16), (17,16), (20,16) all appear closed.