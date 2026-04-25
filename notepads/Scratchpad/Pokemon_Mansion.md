Pokemon Mansion Routing & Switches:
- Switch at 3F (10, 4) toggles YELLOW shutters globally.
  - State A: 3F (15, 6)/(15, 7) OPEN, 3F (15, 10)/(15, 11) CLOSED. 1F (16, 7) CLOSED.
  - State B: 3F (15, 6)/(15, 7) CLOSED, 3F (15, 10)/(15, 11) OPEN. 1F (16, 7) OPEN.

- STAIRS & WARPS:
  - 1F (5, 10) <-> 2F (5, 10) (West Wing)
  - 2F (6, 1) <-> 3F (6, 1) (North Wing)
  - 1F (23, 21) <-> 2F (21, 23) (East Wing)
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
  - 1F (24, 13)/(25, 13) (Yellow Shutter): CLOSED in State A (Turn 39145). OPEN in State B after switch at (2, 5) was pressed on Turn 39203 (Verified Turn 39216).
  - 1F (21, 17) (Yellow Shutter): CLOSED in State B (Verified Turn 39218).
- CURRENT MANSION STATE: B (Set at Turn 39406)
- 1F Wall at y=8: A solid wall blocks North/South movement.
- GREY SHUTTERS at 1F (9, 7) and (9, 11) are OPEN in State A, CLOSED in State B. Traps player from reaching (5, 10) in State B!
- Path to 2F North in State B: Take stairs at 1F (23, 21) -> 2F East -> cross rubble at y=3 -> go through open shutter at 2F (9, 4).