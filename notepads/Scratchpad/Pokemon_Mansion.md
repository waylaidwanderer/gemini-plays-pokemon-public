# Pokemon Mansion Verified Routing & Rules
- Yellow Shutters are state-dependent. They open and close when switches are toggled.
- Dark grey blocks without white tracks (e.g., B1F x=11 at y=20+) are permanent solid walls.
- Dark grey blocks WITH white tracks (e.g., 1F x=9, B1F x=11 at y=14-19) are state-dependent shutters and need empirical testing in both states.

## MANSION B1F WEST (SECRET KEY):
- x=11 (y=14 to y=19) has dark grey shutters. They were CLOSED in State A. We must test them in State B.

## MANSION 1F:
1. The switch at (18, 25) toggles states.
- State A: (16, 16) is OPEN. (13, 23) is CLOSED.
- State B: (16, 16) is CLOSED. (13, 23) is OPEN.
2. We must test the dark grey block at (9, 11) in State A to see if it allows access to the Entrance Hallway.

## MANSION 2F:
1. Path from 2F South to 2F North (stairs at 6, 1) requires walking around the y=9 wall via the x=10 corridor.
2. Then pass West through the vertical yellow shutters at (9, 4)/(9, 5). These shutters must be OPEN (State B) to pass.

## MASTER PLAN V35:
1. 1F: Toggle switch at (18, 25) to State A.
2. Test dark grey block at (9, 11). If OPEN, walk to 2F stairs at (5, 10).
3. If CLOSED, go to B1F via stairs at (23, 22) and explore other options or drop holes from 3F.