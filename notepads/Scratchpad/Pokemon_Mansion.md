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
  - A wall of shutters and statue bases exists at y=16/17.
  - (14, 17)/(15, 17) and (18, 17)/(19, 17): Statue Bases (no statues, solid).
  - State A (Current):
    - Yellow Shutters at (16, 16)/(17, 16): OPEN
  - State B (Observed Turn 39955):
    - Yellow Shutters at (16, 16)/(17, 16): CLOSED
- 1F South Layout:
  - The wall at x=13 is composed of permanent Dark Grey shutters, EXCEPT at y=22 and y=23, which are Yellow Shutters.
  - State A: Yellow Shutters at (13, 22)/(13, 23) are CLOSED.
  - State B: Yellow Shutters at (13, 22)/(13, 23) are OPEN.
  - Scientist NPC at (16, 23).
- Routing to East Wing Switch (18, 25) in State A:
  - From West Wing South, go to (10, 22).
  - Walk North to y=13.
  - Walk East to x=16.
  - Walk South through OPEN yellow shutters at (16, 16).
  - Walk East/South to (18, 25).
- Route to 2F North:
  1. Be in State A.
  2. Enter 1F North via (16, 16).
  3. Walk West to 1F West via (9, 6). (HYPOTHESIS: Shutters at (9, 6) are open in State A. Needs empirical verification).
  4. Press Switch at 1F (2, 5) to enter State B.
  5. Take stairs at 1F (5, 10) to 2F West.
  6. Walk East to 2F North via open shutters at 2F (9, 4).
  7. Take stairs at 2F (6, 1) to 3F.