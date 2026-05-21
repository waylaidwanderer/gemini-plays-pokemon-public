2F Verified Data:
- ELEVATIONS: Color rules are inconsistent. Rely on empirical bump-testing to determine ledges and walls.
- LADDERS: (0,8) goes DOWN to 1F. (23,7) goes UP to 3F. (25,14) goes DOWN to 1F.
- STAIRS: (5,10) connects Level 1 (Low) to Level 2 (High). There are NO STAIRS at (21,15), it is a dead end against a DR wall.
- TRUE BARRIER: Pushing boulder (4,14) to switch (1,16) opens the barrier over the stairs at (21,15). There is no barrier at (3,8).

- EMPIRICAL COLLISION NOTE: Do not declare universal map rules based on isolated tests or tile colors. If a collision occurs, document it as a solid obstacle at that specific coordinate.
- LEDGE AT (17,5): South-facing one-way ledge on 2F. Cannot walk North through it.
- 2F WEST AREA: The DR floor around X=1..4, Y=0..6 contains the ladder at (2,0) which goes UP to 3F (1,1). This ladder must be fully investigated to find the path forward.
\n- NORTHERN CORRIDOR (Y=3..5): Accessed via ramp at (17,5). This area is a dead end blocked by blue rock at Y=6 and X=24. Ladders at Y=7 cannot be reached from here. The only exit is returning to (17,5) and jumping south.
\n- EMPIRICAL UPDATE: The Northern part of 2F West (X=1..7, Y=0..7) is High Ground (Level 2). You can jump South off the ledge at Y=8 to reach the Low Ground (Level 1) at Y=9. From there, you can use the stairs at (5,10) to reach the Southern part of Level 2 where the boulder (4,14) is.
\n- BOULDER SOLUTION (2F West):
  - Boulder resets to (4,14).
  - Walk to (5,14) and push LEFT to (3,14), then (2,14), then (1,14).
  - Walk up to (1,13) and push DOWN to (1,15), then (1,16) onto the switch.
  - This keeps the boulder entirely on the DP Speckled (Level 2) floor!
\n- SEQUENCE BREAK DEBUNKED: The Level 1 (DP) passage East is a DEAD END at X=22 due to chasms and rocks. You MUST solve the 2F West boulder puzzle to open the barrier at (3,8), then walk East across the Central Pit on Level 2 (DR floor).
\n- NAV UPDATE: Testing the X=3 DR bridge to reach the (0,8) ladder from the South.
- CURRENT EMPIRICAL TEST: Boulder at (4,14) must be tested to find the real path to the switch at (1,16). We are moving to (4,13) to test pushing it DOWN or LEFT.