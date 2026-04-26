Pokemon Mansion Navigation & Discoveries:

MECHANICS (DEFINITIVE):
- Exiting to Cinnabar Island resets everything to State A.
- "A secret switch! Press it?" -> YES ("Who wouldn't?") = State B. NO ("Not quite yet!") = State A.
- State A (Default):
  - Dark Grey Shutters (e.g. 9,9/9,10 and 13,25/13,26): OPEN (Walkable)
  - Yellow Shutters (e.g. 13,22..23, 9,6/9,7): CLOSED (Solid)
- State B (Toggled by switch):
  - Dark Grey Shutters (e.g. 9,9/9,10 and 13,25/13,26): CLOSED (Solid)
  - Yellow Shutters (e.g. 13,22..23, 9,6/9,7): OPEN (Walkable, but visually look solid!)

PERMANENT WALLS:
- All dark grey tiles WITHOUT white tracks on the side (e.g. x=13 y=16..21) are PERMANENT WALLS.
- y=8 solid wall (x=10 to x=15) blocking North/South in the Middle Section.
- y=17 solid wall (x=1 to x=8) blocking North/South in the West Wing.

ROUTE TO 1F MAIN STAIRS (5, 10):
State A is REQUIRED to reach the stairs from the entrance!
1. From Entrance (West Wing South), walk East along y=27 to the East Wing.
2. Ensure switch at (18, 25) is in State A (if not, press A and select NO).
3. Walk to (14, 26).
4. Cross West through OPEN Dark Grey Shutter at (13, 26) to reach Middle Section (12, 26).
5. Walk North to (12, 10).
6. Cross West through OPEN Dark Grey Shutter at (9, 10) to reach West Wing North (8, 10).
7. Walk South to (8, 12), West to (5, 12), North to stairs at (5, 10).

ESCAPE TO MAIN STAIRS FROM CURRENT POSITION (Middle Section, State B):
1. Walk South to (12, 22) and cross East through OPEN Yellow Shutter (13, 22) to East Wing.
2. Walk to switch at (18, 26), face Up, press A, select NO to toggle to State A.
3. Follow the Route to 1F Main Stairs above.
Turn 42063 CORRECTION: I am currently in STATE B! I toggled to State B on Turn 42014 and never toggled back. Therefore, my test on Turn 42048 where I bumped into (13, 18) was in State B! Dark Grey shutters are CLOSED in State B. (13, 18..21) are NOT permanent walls, they are dark grey shutters. To escape, I must go to the open Yellow Shutter at (13, 22), cross to the East Wing, and toggle the switch back to State A.