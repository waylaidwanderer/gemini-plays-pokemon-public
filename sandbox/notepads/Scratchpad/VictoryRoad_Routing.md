# Victory Road 2F Routing & Active Hypotheses

- Switch Plate B at (9, 16): Unoccupied.
- Boulder 2: At (9, 11) in trench. Immovable on north/west.
- Elevation Boundary at (23, 12): Confirmed impassable from (23, 11) [Tested Turn 17758].

## Verified Empirical Topology & Findings
- Ladder to 3F: Confirmed at (27, 7) with light blue vertical rails and 3 horizontal rungs [Verified Turn 17751, 17786].
- Eastern Ladder Chamber: Spans cols 25-28, rows 7-9. Contains ladder at (27, 7).
- Column 13 Corridor: Traversed on foot on Turn 17609.
- Tile (23, 9): Impassable rock wall blocking southward passage from (23, 8) [Verified Turn 17781].
 
- Row 5 Barrier: Solid rock wall/cliff across columns 19-24, blocking northern ascent from row 6 [Verified Turn 17792].
- Tile (17, 12): Impassable elevation cliff directly south of (17, 11) [Verified Turn 17819].
- Northeast Cul-de-sac (cols 25-28, rows 0-5): Enclosed dead end with no exits east (col 29 wall) or south (row 6 wall) [Surveyed Turn 17806].

- Barrier (23, 14): Empirically verified SOLID and RAISED on Turn 17953 facing East from (22, 14). Confirms Switch Plate A does not lower this barrier; Switch Plate B at (9, 16) must be solved.
- Tile (22, 12): Solid rock wall directly east of (21, 12) [Empirically verified Turn 17980].
- Tile (24, 8): Solid rock wall directly east of (23, 8) [Empirically verified Turn 17997].

- Verified Facts:
  - Tile (23, 7): Ordinary cave floor with 0 warp effect [Verified Turns 17642, 17785, 17861]. Non-functional ladder graphic.
  - Tile (24, 10): Solid rock wall [Verified Turn 17759].
  - Barrier (23, 14): Solid/raised [Verified 6 independent tests]. Not lowered by Switch Plate A (1, 16).
  - Switch Plate B at (9, 16): Located in row 16 lower corridor. Unoccupied.
  - Exit to 3F: Ladder (25, 14) behind Barrier (23, 14) requires solving Switch Plate B at (9, 16), OR accessing 3F through Northwest/Northeast progression.

- Key Discovery (Turn 18281): Column 17 successfully reached row 3 without needing stairs! Rows 0-3 form an open 4-tile wide east-west corridor across columns 16-24.

## Definitive Topology & Pre-Summarization State (Turn 18285)
- Northeast Cul-de-sac (cols 25-28, rows 0-5): Fully explored. Contains Advice NPC at (26, 3), Max Revive at (26, 5), TM17 at (27, 5). Enclosed on North, East, and South. No progression ladder exists here.
- Eastern Chamber (cols 25-29, rows 7-9): Contains Ladder at (27, 7). 100% enclosed on 2F by solid rock walls on all 4 sides (row 6 wall, row 10 wall, col 24 wall, col 30 wall). This chamber is an exit/arrival drop from 3F, not an overworld entrance to 3F.
- Progression Paths to 3F:
  1. Primary: Northwest Chamber Ladder at (1, 1) guarded by Pok�maniac at (4, 2), accessed via (5, 4) doorway and solving Boulder 1 puzzle.
  2. Alternate/Exit: Southeast Ladder at (25, 14) behind Barrier Block (23, 14), which requires Switch Plate B at (9, 16) in row 16 lower corridor.

- Northeast Cul-de-sac: Fully surveyed and confirmed enclosed dead end. Bump tests verified (24, 5) and (25, 6) are solid rock walls.
- Key Unverified Puzzle Mechanisms:
  1. Boulder 2 at (9, 11) vs Switch Plate B at (9, 16): Same column (col 9). Need to investigate south push access.
  2. Boulder at (13, 13): Pushed south from (13, 12), lateral movements untested.
  3. Barrier (23, 14) guarding exit ladder (25, 14): Controlled by unactivated switch (likely Switch Plate B).

- Empirical Verification (Turn 18372): Column 9 between Switch Plate B (9, 16) and row 12 is a continuous, unobstructed 1-tile wide trench (rows 12-15 are open trench floor). Column 8 is solid rock wall to the west, columns 10-11 form an open checkerboard corridor to the east.

## Empirical Verification (Turn 18374-18377)
- Stood at (9, 12) facing Boulder 2 at (9, 11).
- Confirmed (9, 10) is a solid rock wall directly behind Boulder 2.
- Confirmed Column 9 between (9, 12) and (9, 16) is a completely open 1-tile wide trench.
- Conclusively verified Boulder 2 cannot be pushed onto Switch Plate B. Switch Plate B requires boulder dropped from 3F.
- Columns 13-14 form a wide north-south corridor connecting the row 14 shelf directly up to rows 8-9.
- Empirical Verification (Turn 18385): Successfully traversed from row 16 up through staircase (15, 15) and along column 13 to row 10. Rows 8-9 are completely open connecting west to column 5.


  







## Reconciled Empirical Status of Switch Plate A & Barriers (Turn 18811)
- Boulder 3 is verified resting on Switch Plate A at (1, 16), confirmed across 10 consecutive turns (Turns 18681-18693) where tile (2, 16) was empty floor.
- Moltres confirmed at (7, 7) on central plateau.










## Turn 18918 Ground Truth & Room Reset Strategic Model
- Empirically verified Boulder 2 at (9, 11) is permanently immovable (North blocked by cliff 9, 10; West blocked by wall 8, 11). Confirms Switch Plate B (9, 16) and Barrier (23, 14) guard the 3F return exit, not the entrance to 3F.
- Doorway (5, 4) tests confirmed (4, 4) is a solid wall and Boulder 1 at (5, 3) blocks chamber entry from south.

## Turn 19016 Rigorous Mathematical Sokoban Solution for Boulder 3 & Switch Plate A
- Boulder 3 Starting Position: (4, 14)
- Target Position: Switch Plate A at (1, 16)
- Empirically Verified Walls & Obstacles:
  - (2, 15) is a solid rock pillar.
  - (5, 16) is a solid rock wall.
  - (1, 12) and (1, 13) are solid rock debris.
  - (1..5, 17) is solid southern boundary.
- Canonical 5-Push Solution (verified via BFS):
  1. Position player at (5, 14) facing West. Push Boulder 3 WEST from (4, 14) to (3, 14).
  2. Walk around via (4, 13) to (3, 13) facing South. Push Boulder 3 SOUTH from (3, 14) to (3, 15).
  3. Push Boulder 3 SOUTH from (3, 15) to (3, 16).
  4. Walk around via (4, 15) to (4, 16) facing West. Push Boulder 3 WEST from (3, 16) to (2, 16).
  5. Push Boulder 3 WEST from (2, 16) onto Switch Plate A at (1, 16)!










## Turn 18973 Empirical Confirmation: Boulder 1 East Push Blocked & Row 3 Highway Verified
- Empirical Verification: Tested East push on Boulder 1 at (5, 5) from (4, 5) with Strength active. Boulder did not move; tile (6, 5) is 100% solid rock wall.
- Strategic Deduction:
  1. Boulder 1 cannot be displaced East.
  2. Pushing Boulder 1 North into (5, 3) blocks the row 3 corridor.
  3. Therefore, Boulder 1 MUST REMAIN at (5, 5) to leave tile (5, 3) completely open!
- Ground Truth Topology:
  - Verification Warning: While rows 2-3 are open locally across cols 6-9, permanent records empirically prove that columns 14-15 form a solid rock wall across rows 0-7, terminating westward passage from the eastern upper plateau. Westward traversal from staircase (17, 5) along row 3 cannot reach column 9.
  - Active Investigation: Evaluating how columns 6-9 connect to the central plateau, or investigating the true path to 3F.





## Pre-Commitment Test Matrix: Starting State Boulder 1 at (5, 5)
- Spatial Boundary Facts:
  - (5, 5): Starting boulder position.
  - (6, 5): Verified solid rock wall directly east. Pushing East from (4, 5) is physically impossible.
  - (5, 4): Open doorway in row 4.
  - (4, 4), (6, 4): Verified solid rock walls flanking (5, 4).
  - (5, 3): Open floor inside doorway.
  - (5, 2): Solid rock wall blocking further northward movement from (5, 3).
- Hypotheses & Experimental Protocol:
  1. Test A (Northwest Chamber Entrance Alternative): Investigate if (4, 3) can be reached directly without pushing Boulder 1 into (5, 3). Does pushing Boulder 1 to (5, 4) allow the player to enter (5, 4)? (Blocked by Boulder 1).
  2. Test B (Boulder 3 onto Switch Plate A): Re-evaluate Switch Plate A at (1, 16). Does pushing Boulder 3 onto Switch Plate A alter any barrier other than (23, 14), specifically examining if a barrier lowered on the upper plateau or near Moltres?
  3. Test C (Strength User Verification): Geodude (ROCKY) knows Strength.


## Turn 19046 Definitive Empirical Bump Test: Barrier (23, 14) is SOLID with Switch Plate A Depressed
- Test Setup: Boulder 3 actively depressing Switch Plate A at (1, 16) on this single un-reset floor visit. Player positioned at (22, 14) facing East directly at Barrier (23, 14).
- Action & Outcome: Pressed Right 3 times. Player bumped into (23, 14) and remained at (22, 14) (0 tiles visited).
- Conclusive Finding: Switch Plate A at (1, 16) DOES NOT lower Barrier (23, 14).
- Physical Reality: Barrier (23, 14) is 100% solid and raised. It must be lowered by Switch Plate B at (9, 16) via 3F boulder drop, or another mechanism. Ladder (25, 14) is therefore inaccessible from row 14 west.

- Boundary (10, 8) -> (10, 7): Empirically verified impassable elevation cliff on Turn 19113 (bump test visited 0 tiles). The row 8 northern cliff extends across column 10.

- Column 14 Southern Barrier: Empirically verified on Turns 19156-19158 that (14, 6) and (14, 7) are solid rock walls (bump tests visited 0 tiles). Column 14 is solid across rows 0 through 7.

## Turn 19232 Definitive Ground Truth & Dynamic Floor State
- Active Floor Visit State: Boulder 3 actively depressing Switch Plate A at (1, 16) [Turn 19216, un-reset visit].
- Barrier (23, 14) Reality: Conclusively verified solid on Turn 19046 with Switch Plate A depressed. Barrier (23, 14) is NOT lowered by Switch Plate A; it guards the 3F return drop ladder (25, 14), which is unlocked by dropping the 3F boulder down the hole onto Switch Plate B at (9, 16).
- Progression Imperative: Abandoning redundant trips to Barrier (23, 14). The entrance ladder to 3F must be located and accessed directly.

- Turn 19236: Physical bump test confirmed (13, 7) is solid elevation cliff from (13, 8) with Switch Plate A active (visited 0 tiles).
- Turn 19237: Physical bump test confirmed (12, 7) is solid elevation cliff from (12, 8) with Switch Plate A active (visited 0 tiles).
- Turn 19238: Physical bump test confirmed (11, 7) is solid elevation cliff from (11, 8) with Switch Plate A active (visited 0 tiles).
- Turn 19239: Physical bump test confirmed (10, 7) is solid elevation cliff from (10, 8) with Switch Plate A active (visited 0 tiles).
- Turn 19240: Physical bump test confirmed (9, 7) is solid elevation cliff from (9, 8) with Switch Plate A active (visited 0 tiles).
- Turn 19241: Physical bump test confirmed (8, 7) is solid rock wall from (8, 8) with Switch Plate A active (visited 0 tiles).
- Turn 19242: Physical bump test confirmed (7, 7) is solid elevation cliff from (7, 8) with Switch Plate A active (visited 0 tiles).
- Turn 19243: Physical bump test confirmed (6, 7) is solid elevation cliff from (6, 8) with Switch Plate A active (visited 0 tiles).
- Definitive Falsification (Turn 19243): 100% of row 8 northern boundaries across cols 5-13 have been physically tested and verified impassable with Switch Plate A active. Conclusively falsified that Switch Plate A opens any passage across row 8 or row 7.
- Turn 19256: Tested push on Boulder 1 at (5, 3) from doorway (5, 4) with Strength active: bumped into (5, 2) rock wall (0 tiles visited). Boulder 1 at (5, 3) cannot move north.
- Strategic Directive: Doorway (5, 4) is blocked by Boulder 1 at (5, 3). Routing to upper plateau via staircase (17, 5) to test row 4 corridor at (14, 4) and access the central plateau and Row 3 highway to ladder (1, 1).