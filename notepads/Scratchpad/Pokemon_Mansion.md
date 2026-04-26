Pokemon Mansion Navigation & Discoveries:

MECHANICS (DEFINITIVE):
- Exiting to Cinnabar Island resets everything to State A.
- State A (Default):
  - (9, 9)/(9, 10) Dark Grey Shutter: OPEN
  - x=13 Dark Grey Shutters (y=17..21): OPEN
  - Yellow Shutters (e.g. 16,16, 13,22..23, 9,6/9,7): CLOSED
- State B (Toggled by switch):
  - (9, 9)/(9, 10) Dark Grey Shutter: CLOSED
  - x=13 Dark Grey Shutters (y=17..21): CLOSED
  - Yellow Shutters (e.g. 16,16, 13,22..23, 9,6/9,7): OPEN

- PERMANENT WALLS:
  - x=9 dark grey tiles (y=8 to y=16, except 9,9/10).
  - x=13 dark grey tiles (y=24 to y=26).
  - x=20 dark grey tiles (y=17 to y=26).
  - y=8 solid wall (x=10 to x=15) blocking North/South.

ROUTE TO 1F MAIN STAIRS:
State A:
1. Ensure switch at (18, 25) is in State A.
2. Navigate to (14, 18).
3. Walk Left through OPEN Dark Grey Shutter at (13, 18) to reach (12, 18).
4. Walk North to (12, 10).
5. Walk Left through OPEN Dark Grey Shutter at (9, 10) to reach (8, 10).
6. Walk Down to (8, 12), Left to (5, 12), Up to stairs at (5, 10).

State B:
1. Ensure switch at (18, 25) is in State B.
2. Walk Left to (14, 26), Up to (14, 22).
3. Walk Left through OPEN Yellow Shutter at (13, 22) to West Wing.
4. Walk North to (12, 7).
5. Walk West through OPEN Yellow Shutter at (9, 7).
6. Walk South to stairs at (5, 10).

ESCAPE FROM MANSION:
- The true exit is at x=21 to x=24, y=27.
- From West Wing, cross East via (13, 22) in State B or (13, 18) in State A, then navigate South to the exit.
Turn 42002 Reflection: Failed to cross (13, 18) because I am actually in State B (Dark Grey CLOSED, Yellow OPEN). The open yellow shutter at (13, 22) looks solid (vertical yellow/orange lines) but is walkable in State B.
Turn 42005 Correction: I was NOT in State B. The dark grey shutters at (13, 18) to (13, 21) are indeed OPEN (Walkable/Shutter_Dark_Grey_Open). My failure on turn 41999 was due to a coordinate math error (I walked Down to y=22 instead of Up to y=18). The yellow shutter at (13, 22) is CLOSED. I will proceed to (13, 18) and cross West.
Turn 42007: CRITICAL CORRECTION: (13, 18) is a PERMANENT WALL. The dark grey tiles at x=13 do not open. The ONLY way to cross x=13 is via the Yellow Shutter at (13, 22), which requires State B (RED eyes). Proceeding to switch at (18, 25) to toggle to State B.
Turn 42019 Reflection: In State B, I crossed x=13 via the yellow shutter at (13, 22) and walked North to (12, 9). I realized the y=8 solid wall blocks me from going North to (12, 7). Also, the x=9 dark grey shutters are CLOSED in State B. This means in State B, I am trapped between x=9 and x=13. If x=13 dark grey shutters are truly permanent walls, then I MUST find a switch inside the x=9..13 area to toggle back to State A so I can cross x=9. Exploring this middle section now.