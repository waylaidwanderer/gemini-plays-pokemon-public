Pokemon Mansion Routing & Switches:
- Switch at 3F (10, 4) toggles YELLOW shutters globally.
  - State A: 3F (15, 6)/(15, 7) OPEN, 3F (15, 10)/(15, 11) CLOSED. 1F (16, 7) CLOSED.
  - State B: 3F (15, 6)/(15, 7) CLOSED, 3F (15, 10)/(15, 11) OPEN. 1F (16, 7) OPEN.

- STAIRS & WARPS:
  - 1F (5, 10) <-> 2F (5, 10) (West Wing)
  - 2F (6, 1) <-> 3F (6, 1) (North Wing)
  - 1F (23, 21) <-> B1F (21, 23) (East Wing - Dead End)
  - B1F (7, 10) -> 1F (7, 10) (One-way up from B1F West)

- DROP HOLES (DANGER):
  - 2F (7, 10) is an INVISIBLE drop hole. Falls to 1F (7, 10).
  - 3F (16, 14) is a drop hole.

- *** CRITICAL ROUTING CONSTRAINTS ***
  - 2F CONNECTION: 2F South connects to 2F North via a gap at x=20.
  - Path: From 2F (5, 10), walk East along y=7 to (20, 7). Walk North through the shutter at (20, 5) [OPEN IN STATE A] to reach (20, 3). From (20, 3), walk West into 2F North to reach stairs at (6, 1).
  - 1F NORTH ACCESS: 1F North has been fully explored (x=1 to x=28) and empirically verified: there are NO stairs to 2F North here.
- 1F Layout notes:
  - 1F Northeast corridor hits a dead end at (28, 1) and turns South at x=26, 27.
- EMPIRICAL PROOF: The switch statue at 1F (2, 5) toggles the global shutter state.
- 1F Shutters & States:
  - 1F (24, 13)/(25, 13) (Yellow Shutter): CLOSED in State A (Turn 39145). OPEN in State B after switch at (2, 5) was pressed on Turn 39203 (Verified Turn 39216).
  - 1F (21, 17) (Yellow Shutter): CLOSED in State B (Verified Turn 39218).
- Shutter-free path between North and South 1F: 1F (10, 7) <-> 1F (12, 7) <-> 1F (12, 11) <-> 1F (5, 11).
- Turn 39246 Reflection:
  - Immediate Execution: Correcting my mistake by returning to the switch at (2, 5) to restore State A, then I will use the shutter-free path at x=12.
  - Error Analysis: Deleting my notes about the shutter-free path caused me to hallucinate an inescapable airlock puzzle. I must be extremely careful when editing notes to preserve known routing constraints.
- 2F (18, 8)/(19, 8) (Yellow Shutter): OPEN in State B (Verified Turn 39281).