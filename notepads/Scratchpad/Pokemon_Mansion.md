Pokemon Mansion Navigation & Discoveries:

MECHANICS (DEFINITIVE):
- Exiting to Cinnabar Island resets everything to State A.
- Switch prompt: YES ("Who wouldn't?") = TOGGLES STATE. NO ("Not quite yet!") = DOES NOTHING.
- State A (Default):
  - Dark Grey Shutters (Vertical, e.g. 20,16..26): OPEN (Walkable)
  - Yellow Shutters (Vertical, e.g. 13,22..23): OPEN (Walkable)
  - Yellow Shutters (Horizontal, e.g. 16,16..17,16): CLOSED (Solid)
- State B (Toggled by switch):
  - Dark Grey Shutters (Vertical, e.g. 20,16..26): CLOSED (Solid)
  - Yellow Shutters (Vertical, e.g. 13,22..23): CLOSED (Solid)
  - Yellow Shutters (Horizontal, e.g. 16,16..17,16): OPEN (Walkable)

PERMANENT WALLS (Never open):
- y=17 solid wall (x=1 to x=8) blocking North/South in the West Wing.
- y=8 solid wall (x=10 to x=15) blocking North/South in the Middle Section. (x=16 is CLEAR!)
- x=13 solid wall (y=17 to y=21) and (y=24 to y=26).
- x=9 solid wall (y=8 to y=17).
- y=27 solid wall blocks connecting West/Middle/East wings.

PATH TO 2F STAIRS (1F):
1. Enter Mansion at (21, 27) (East Wing, State A default).
2. Walk North to y=25.
3. Walk West through open dark grey shutter at (20, 25) to reach switch at (18, 25).
4. Press switch to toggle to State B.
5. Walk North along x=18 to y=16.
6. Walk West through open yellow shutters at (17, 16) and (16, 16).
7. Walk North along x=16 to y=7. (x=16 bypasses the y=8 Middle Section wall!)
8. Walk West through open yellow shutters at (16, 7) and (9, 7).
9. Walk West and South to the main stairs at (5, 10).
- EMPIRICAL PROOF (Turn 42284): y=8 is a solid wall at x=16. The path North along x=16 is blocked. I must find another way to cross to the North section of 1F. Testing x=9.
- HYPOTHESIS (Turn 42287): To reach the 2F stairs, I must go to West Wing South (via y=22 in State B), find a switch there to toggle to State A, then walk North through the open Dark Grey Shutter at (9, 9).
- NEW HYPOTHESIS (Turn 42294): Vertical Yellow Shutters (like at 13,22 and 13,23) are OPEN in State A and CLOSED in State B. Horizontal Yellow Shutters are CLOSED in State A and OPEN in State B. I will toggle the switch to State A and test crossing (13, 22).
- EMPIRICAL PROOF (Turn 42299): The dark grey tiles at (9, 8), (9, 9), and (9, 10) are SOLID in State A. Since dark grey shutters are supposed to be open in State A, this proves they are PERMANENT WALLS disguised as shutters.