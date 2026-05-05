# Pokemon Mansion Verified Routing & Rules
- Yellow Shutters are state-dependent. They open and close when switches are toggled.
- Dark grey blocks without white tracks (e.g., B1F x=11) are permanent solid walls.
- Dark grey blocks WITH white tracks (e.g., 1F x=9) need to be empirically tested in State A to see if they open.

## MANSION B1F WEST (SECRET KEY):
- x=11 is a permanent solid wall. B1F West CANNOT be reached from the B1F stairs at (21, 23).
- We MUST find a drop hole on 3F that leads to B1F West.

## MANSION 1F:
1. The switch at (18, 25) controls global shutter states.
2. We must test the dark grey block at (9, 11) in State A to see if it allows access to the Entrance Hallway.

## MANSION 2F:
1. Path from 2F South to 2F North (stairs at 6, 1) requires walking around the y=9 wall via the x=10 corridor.
2. Then pass West through the vertical yellow shutters at (9, 4)/(9, 5). These shutters must be OPEN (State B) to pass.

## MASTER PLAN V33:
1. Return to 1F.
2. Toggle switch at (18, 25) to State A.
3. Navigate to (10, 11) and attempt to walk West into (9, 11) to prove if it is a shutter or a permanent wall.