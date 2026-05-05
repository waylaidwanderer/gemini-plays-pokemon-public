# Pokemon Mansion Verified Routing & Rules
- Yellow Shutters are state-dependent. They open and close when switches are toggled.
- Dark grey blocks without white tracks (e.g., B1F x=11 at y=20+) are permanent solid walls.
- Dark grey blocks WITH white tracks (e.g., 1F x=9, B1F x=11 at y=14-19) are ALSO permanent solid walls. They never open in either state.
- Therefore, B1F West (Secret Key) CANNOT be reached from B1F East. We MUST find a drop hole on 3F.
- The Entrance Hallway on 1F is COMPLETELY ISOLATED. We MUST re-enter from Cinnabar Island to reach the 2F stairs.

## MANSION 1F:
1. The switch at (18, 25) toggles states.
- State A: (16, 16) horizontal yellow is OPEN. (13, 23) vertical yellow is CLOSED.
- State B: (16, 16) horizontal yellow is CLOSED. (13, 23) vertical yellow is OPEN.

## MASTER PLAN V36 (The Route to 3F):
1. 1F: Toggle switch at (18, 25) to State B.
2. Navigate to B1F stairs at (23, 22). (Use x=10, y=23 in State B).
3. B1F: Walk North, East to x=26, South to exit at (26, 27) (Accessible in State B).
4. Cinnabar Island: Walk to (6, 3) and enter Mansion.
5. 1F (Entrance Hallway): Walk North to stairs at (5, 10).
6. 2F: State B is active, so yellow shutters at (9, 4)/(9, 5) are open! Walk to stairs at (6, 1).
7. 3F: Reached! Explore for drop hole to B1F West.