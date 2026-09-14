# Victory Road 2F Routing & Active Hypotheses

- Switch Plate B at (9, 16): Unoccupied.
- Boulder 1: Pushed to (5, 3).
- Boulder 2: At (9, 11) in trench. Immovable on north/west.
- Boulder at (13, 13): Pushed south from (13, 12) on Turn 17695. Tested south push on Turn 17709-17710 with Strength active; boulder did not advance south into (13, 14).
- Elevation Boundary at (23, 12): Confirmed impassable from (23, 11) [Tested Turn 17758].

## Verified Empirical Topology & Findings
- Ladder to 3F: Confirmed at (27, 7) with light blue vertical rails and 3 horizontal rungs [Verified Turn 17751, 17786].
- Eastern Ladder Chamber: Spans cols 25-28, rows 7-9. Contains ladder at (27, 7).
- Column 13 Corridor: Traversed on foot on Turn 17609.
- Tile (23, 9): Impassable rock wall blocking southward passage from (23, 8) [Verified Turn 17781].
- Boulder at (22, 3) (SPRITE_6768): Pushed East from (22, 3) to (23, 3) [Turn 17877], then East from (23, 3) to (24, 3) [Turn 17879] with Strength active. 
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
- Tile (23, 7): Ordinary floor with 0 warp effect [Verified Turns 17642, 17785, 17861].
- Progression Paths to 3F:
  1. Primary: Northwest Chamber Ladder at (1, 1) guarded by Pok�maniac at (4, 2), accessed via (5, 4) doorway and solving Boulder 1 puzzle.
  2. Alternate/Exit: Southeast Ladder at (25, 14) behind Barrier Block (23, 14), which requires Switch Plate B at (9, 16) in row 16 lower corridor.

- Northeast Cul-de-sac: Fully surveyed and confirmed enclosed dead end. Bump tests verified (24, 5) and (25, 6) are solid rock walls.
- Immediate Movement: Moving south down column 17 to row 11 to access central/southern floor.
- Key Unverified Puzzle Mechanisms:
  1. Boulder 2 at (9, 11) vs Switch Plate B at (9, 16): Same column (col 9). Need to investigate south push access.
  2. Boulder at (13, 13): Pushed south from (13, 12), lateral movements untested.
  3. Barrier (23, 14) guarding exit ladder (25, 14): Controlled by unactivated switch (likely Switch Plate B).

- Current Position (Turn 18372): (9, 16) standing on Switch Plate B facing Left.
- Empirical Verification (Turn 18372): Column 9 between Switch Plate B (9, 16) and row 12 is a continuous, unobstructed 1-tile wide trench (rows 12-15 are open trench floor). Column 8 is solid rock wall to the west, columns 10-11 form an open checkerboard corridor to the east.

## Empirical Verification (Turn 18374-18377)
- Stood at (9, 12) facing Boulder 2 at (9, 11).
- Confirmed (9, 10) is a solid rock wall directly behind Boulder 2.
- Confirmed Column 9 between (9, 12) and (9, 16) is a completely open 1-tile wide trench.
- Conclusively verified Boulder 2 cannot be pushed onto Switch Plate B. Switch Plate B requires boulder dropped from 3F.
- Columns 13-14 form a wide north-south corridor connecting the row 14 shelf directly up to rows 8-9.
- Empirical Verification (Turn 18385): Successfully traversed from row 16 up through staircase (15, 15) and along column 13 to row 10. Rows 8-9 are completely open connecting west to column 5.

- Visual Confirmation: Ladder to 1F visible at (0, 8); Boulder 1 confirmed sitting at (5, 3).

## Floor Reset Execution (Turn 18403-18404)
- Arrived at (1, 1) on Victory Road 1F via ladder (0, 8).
- Map transition executed: All 2F dynamic boulders are now reset to starting positions!
  - Boulder 1 is reset to (5, 5).
  - Boulder 3 is reset to (4, 14).
  - Boulder 4 is reset to (22, 3).


## Post-Reset Arrival on 2F (Turn 18410-18413)
- Arrived at (0, 8) on Victory Road 2F via ladder.

## Boulder 1 Testing & Western Perimeter Findings (Turns 18413-18452)
- Re-activated Strength with Geodude (ROCKY) at (5, 6) [Turn 18425].
- Pushed Boulder 1 North from (5, 5) to (5, 4) [Turn 18426], then stepped onto (5, 5) [Turn 18427].
- Pushed Boulder 1 North from (5, 4) to (5, 3) [Turn 18428], then stepped onto (5, 4) [Turn 18430].
- Bumping North from (5, 4) into Boulder 1 at (5, 3) confirmed tile (5, 2) is a solid rock obstacle [Turn 18431]; Boulder 1 cannot advance North.
- Doorway (5, 4) is blocked from the south by Boulder 1 at (5, 3); lateral access from (5, 4) is blocked by solid rock walls at (4, 4) and (6, 4).
- Intermediate state Turn 18442_0 visually confirmed Column 0 is blocked at rows 3-5 by solid rock walls at (0, 3..5). Column 0 does not connect north into the chamber.
- Retreated South to (5, 7) [Turn 18440], walked West to (2, 7) along row 7 [Turn 18441].
- Fled wild Onix battle at (2, 7) [Turns 18442-18448].
- Current Position (Turn 18481): (28, 11) facing Up on row 11 corridor.

## Plateau & Eastern Traversal Progress (Turns 18453-18481)
- Traversed row 11 and climbed wooden staircase at (5, 10) to (5, 9) on the elevated plateau [Turn 18454].
- Crossed elevated plateau east to (9, 9) and (13, 8) past column 12 [Turns 18456-18457].
- Navigated south down column 13 corridor to (13, 12) [Turn 18458].
- Traversed east along row 12 toward staircase (21, 15), fleeing wild Onix at (18, 12) [Turns 18460-18463] and wild Geodude at (19, 14) [Turns 18465-18467].
- Descended staircase (21, 15) to row 16 lower corridor at (21, 16), fleeing wild Machop [Turns 18468-18471].
- Traversed row 16 east to column 28 and ascended Eastern Vertical Highway to (28, 14), fleeing wild Onix [Turns 18472-18476].
- Ascended to (28, 11) on row 11 [Turn 18477].
- Executed bump test North into tile (28, 10) on Turn 18479: bumped, confirming (28, 10) is a solid rock wall.

