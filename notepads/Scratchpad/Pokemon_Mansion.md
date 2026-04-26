Pokemon Mansion Navigation & Discoveries:

MECHANICS (DEFINITIVE):
- Exiting to Cinnabar Island resets everything to State A.
- State A (Default):
  - x=9 Dark Grey Shutters (9, 9)/(9, 10): OPEN
  - x=13 Dark Grey Shutters (y=17..21): OPEN
  - Yellow Shutters (e.g. 16,16, 13,22..23, 9,6/9,7): CLOSED
- State B (Toggled by switch):
  - x=9 Dark Grey Shutters (9, 9)/(9, 10): CLOSED
  - x=13 Dark Grey Shutters (y=17..21): CLOSED
  - Yellow Shutters (e.g. 16,16, 13,22..23, 9,6/9,7): OPEN

PERMANENT WALLS:
- y=8 solid wall (x=10 to x=15) blocking North/South in the Middle Section.
- y=17 solid wall (x=1 to x=8) blocking North/South in the West Wing.
- x=13 solid wall at (13, 25)/(13, 26). (Empirically verified Turn 41957)

ROUTE TO 1F MAIN STAIRS (5, 10):
State A is REQUIRED to reach the stairs from the entrance!
1. From Entrance (West Wing South), walk East along y=27 to the East Wing.
2. Walk North in East Wing to (14, 18).
3. Cross West through OPEN Dark Grey Shutter at (13, 18) to reach Middle Section (12, 18).
4. Walk North to (12, 10).
5. Cross West through OPEN Dark Grey Shutter at (9, 10) to reach West Wing North (8, 10).
6. Walk South to (8, 12), West to (5, 12), North to stairs at (5, 10).

ESCAPE TO MAIN STAIRS FROM CURRENT POSITION (Middle Section, State B):
1. Walk South to (12, 22) and cross East through Yellow Shutter (13, 22) to East Wing.
2. Walk to switch at (18, 25) and toggle to State A.
3. Follow the Route to 1F Main Stairs above.