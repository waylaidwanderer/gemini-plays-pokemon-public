Pokemon Mansion Navigation & Discoveries:

MECHANICS (DEFINITIVE):
- Exiting to Cinnabar Island resets everything to State A.
- Shutter Logic: Dark Grey & Yellow shutters are INVERTED relative to each other.
- State A (Default):
  - (9, 9)/(9, 10) Dark Grey Shutter: OPEN
  - x=13 & x=20 Dark Grey Shutters (y=17..21): CLOSED
  - Yellow Shutters (e.g., 16,16 and 13,22): CLOSED
- State B (Toggled by 1F 18,25 switch):
  - (9, 9)/(9, 10) Dark Grey Shutter: CLOSED
  - x=13 Dark Grey Shutters (y=24..26): CLOSED
  - Path through x=13 is OPEN at y=22 and y=23.
  - x=20 Dark Grey Shutters: CLOSED
  - Yellow Shutters: OPEN

- PERMANENT WALLS:
  - The dark grey tiles at x=9 from y=11 to y=16 are permanent walls, NOT shutters!
  - The dark grey tiles at x=20 from y=17 to y=26 are permanent walls, NOT shutters!
  - The yellow pillars at x=13 (y=22..24) are permanent walls. The actual doors are at y=21, y=25, and y=26!

ROUTE TO 1F MAIN STAIRS (State A):
1. Walk to (12, 21), then North to (12, 10).
2. Left to (10, 10), then Left through OPEN Dark Grey Shutter at (9, 10) to (8, 10).
3. Down to (8, 12), Left to (5, 12), Up to stairs at (5, 10).

ESCAPE FROM MANSION:
- The true exit is at x=21 to x=24, y=27.
- If trapped in the East Wing, toggle switch at (18, 25) to State B.
- This opens the x=13 shutters (y=17..23). Walk Left through them.
- From West Wing, navigate South to the exit.
- PERMANENT WALL: y=8 is a solid wall separating the North and South sections on 1F, spanning at least x=10 to x=15. You cannot walk North from (10, 9).