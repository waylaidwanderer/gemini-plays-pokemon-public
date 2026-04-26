Pokemon Mansion Navigation & Discoveries:

MECHANICS (DEFINITIVE):
- Exiting to Cinnabar Island resets everything to State A.
- State A (Default):
  - x=9 Dark Grey Shutters (9, 9)/(9, 10): OPEN
  - x=13 Dark Grey Shutters (13, 17..20): OPEN
  - Yellow Shutters (e.g. 16,16, 13,22..23, 9,6/9,7): CLOSED
- State B (Toggled by switch):
  - x=9 Dark Grey Shutters (9, 9)/(9, 10): CLOSED
  - x=13 Dark Grey Shutters (13, 17..20): CLOSED
  - Yellow Shutters (e.g. 16,16, 13,22..23, 9,6/9,7): OPEN

PERMANENT WALLS:
- y=8 solid wall (x=10 to x=15) blocking North/South in the Middle Section.
- y=17 solid wall (x=1 to x=8) blocking North/South in the West Wing.
- (13, 25) and (13, 26) are permanent solid walls (empirically verified Turn 41957).

ROUTE TO 1F MAIN STAIRS (5, 10):
To reach the stairs from the entrance, State A is REQUIRED so you can cross x=9.
1. From Entrance (West Wing South), walk East along y=27 to the East Wing.
2. Walk North in East Wing to (14, 18).
3. Cross West through OPEN Dark Grey Shutter at (13, 18) to reach Middle Section (12, 18).
4. Walk North to (12, 10).
5. Cross West through OPEN Dark Grey Shutter at (9, 10) to reach West Wing North (8, 10).
6. Walk South to (8, 12), West to (5, 12), North to stairs at (5, 10).

ESCAPE TO MAIN STAIRS FROM CURRENT POSITION (Middle Section):
1. If in State B (Yellow Shutters open, Dark Grey closed):
   a. Walk South to (12, 22), cross East through Yellow Shutter (13, 22) to East Wing.
   b. Walk to switch at (18, 25) and toggle to State A.
   c. Follow the Route to 1F Main Stairs above.
2. If in State A (Dark Grey Shutters open, Yellow closed):
   a. Follow the Route to 1F Main Stairs starting from step 3 or 4.