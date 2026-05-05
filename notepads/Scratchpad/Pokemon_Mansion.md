# Pokemon Mansion Verified Routing & Rules
- Yellow Shutters are state-dependent.
  - Horizontal yellow shutters (e.g. 16,16) are OPEN in State A, CLOSED in State B.
  - Vertical yellow shutters (e.g. 13,22, and 16,7) are OPEN in State B, CLOSED in State A.
- Dark grey blocks without white tracks are permanent solid walls (e.g. 9,9).

## MASTER PLAN V42 (The True Escape):
1. Current State: (16, 16) is OPEN, (13, 22) is CLOSED, (9, 9) dark grey shutters are CLOSED.
2. Toggle switch at 1F (18, 25). This reverses all shutters!
3. New State: (16, 16) closes, (13, 22) OPENS, (9, 9) OPENS.
4. Walk West to x=14, North to y=22, West through OPEN (13, 22) to x=12.
5. Walk North to y=15 corridor, West to x=9.
6. Walk North through OPEN dark grey shutters at (9, 9) into the Entrance Hallway!
7. Take stairs at (5, 10) to 2F.