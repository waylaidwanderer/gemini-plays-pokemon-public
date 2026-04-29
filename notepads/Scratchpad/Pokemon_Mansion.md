Pokemon Mansion Mechanics:
- STATE A: Yellow Shutters CLOSED. Dark Grey Shutters OPEN (Hypothesis to be re-tested).
- STATE B: Yellow Shutters OPEN. Dark Grey Shutters CLOSED.

TEST PLAN TO REACH 2F NORTH:
1. We must explore the isolated 2F North, accessed via stairs at 1F (5, 10).
2. To reach the stairs, we must enter West Wing North (x<9, y<17).
3. The wall at x=9 (from y=10 to y=16) is made of Dark Grey Shutters.
4. We will navigate to the main switch at (18, 25) and toggle to STATE A.
5. In STATE A, the Yellow Shutter at (13, 22) closes, but we can cross to the x=10 corridor via the permanently open row at y=15.
6. Walk Left along y=15 to (10, 15).
7. Test if the Dark Grey Shutter at (9, 15) is OPEN in State A. If yes, cross West and walk to the stairs at (5, 10).

KNOWN CONSTRAINTS & EMPIRICAL PROOFS:
- B1F East Wing (via 1F 23,22) is a DEAD END.
- x=20 is a solid wall separating East from Center, OPEN at y=15.
- y=16 is a wall in Center, but has a permanent gap at x=11 and x=12.
- (13, 24) and (13, 25) are PERMANENT WALLS.
- The Dark Grey Shutter at (13, 16) is CLOSED in both State A and State B (Tested empirically).