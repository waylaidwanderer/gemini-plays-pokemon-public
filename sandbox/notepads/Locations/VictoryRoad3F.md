# Victory Road 3F - Layout, Landmarks & Verified Topology

## Visual Tile Characteristics
- Upper Dark Plateau: Dark checkerboard floor texture across rows 0-11. Contains Northern Highway (Row 1), Central Bridge (cols 6-7), NW Room (cols 0-5), Switch (3, 5), Ladder A (23, 7), Ladder NE (27, 7), Cooltrainer (28, 5).
- Lower Purple Floor: Light purple floor with dots across rows 12-14 (cols 17-26).
- Pit Room: Southern sector (rows 14-17, cols 21-29). Contains Pit at (23, 14), Shutter at (21, 15), and Ladder B at (25, 14).

## Verified 3F Ladders & Floor Connections
1. NW Ladder @ (2, 0): Located in NW Room (cols 0-5). Connects to 2F NW elevated plateau at (1, 1).
2. Ladder A @ (23, 7): Wall ladder on north wall of central sector. Connects to 2F at (23, 7).
3. Ladder NE @ (27, 7): Wall ladder in enclosed NE room (rows 7-9, cols 25-28). Connects to 2F behind switch shutter at (27, 7).
4. Ladder B @ (25, 14): Floor ladder (wall ladder graphic `[=]`) in SE Pit room. Connects to 2F SE sector at (25, 14).

## Verified Mechanics & Observed Objects
- Switch (3, 5) in NW Room: The 3F NW Room contains no pushable boulders.
- Boulder 1 @ (22, 3): Located in northern chamber.
- Boulder 2 @ (13, 12): Located at western chokepoint between rock walls (12, 12) and (14, 12).
- Pit @ (23, 14): Blue checked square tile `[X]`. Note: horizontal movement East from (22, 14) into (23, 14) is physically blocked (verified Turns 34158, 34161).

## Verified Boundaries & Blockades (Empirically Verified Turns 33855-34170)
- Row 2 Highway Connection: Columns 2 through 7 along Row 2 ((2..7, 2)) form an open, unobstructed east-west corridor connecting the NW Room (cols 0-5) directly to the Central Bridge (cols 6-7) and Northern Highway (Row 1)!
- Row 6 Barrier (East): Continuous solid rock wall spans columns 24 through 29 along Row 6, separating the northern plateau from the eastern ladder chamber.
- Column 23 Rock: Tile (23, 9) is a solid purple rock obstacle blocking southward passage from (23, 8) into row 10.
- Row 10 East Barrier: Horizontal purple rock wall spans columns 24 through 29 along Row 10, separating rows 7-9 from rows 11-14.
- Row 11 South-Facing Cliff: Continuous cliff runs along Row 11 across columns 16-27, preventing northward walking from Row 12 into Row 11.
- Column 28-29 Highway: Columns 28 and 29 form an open vertical corridor connecting rows 11-16 to the northern corridors.
- Row 16 Highway: Row 16 connects columns 20 through 28 horizontally across the southern edge of the map.

## Verified Boulder 1 Routing Protocol (Refreshed Visit)
- Initial State: Boulder 1 at (22, 3) in northern chamber, 3F reloaded via NW Ladder.
- Strength: Activated with ATLAS (Turn 34796).
- Step-by-Step Route:
  1. Approach Boulder 1 at (22, 3) via Row 1 Northern Highway.
  2. Stand at (23, 3) -> Push West 2 times from (22, 3) to (20, 3) [Player at (21, 3)].
  3. Reposition behind boulder to (20, 4) / (20, 3) -> Push North 2 times to (20, 1) [Player at (20, 2)].
  4. Reposition to (21, 1) -> Push West along Row 1 Northern Highway all the way to (6, 1) [Player at (7, 1)].
  5. Reposition around boulder to (6, 0) via (7, 0) -> Push South down Column 6 chute across bridge directly to southern floor at row 12!
  6. Push east across southern floor to Pit at (23, 14) and drop boulder into pit.

- Turn 34833: Boulder 1 successfully positioned at (6, 1) at the head of Column 6 chute. Player at (8, 0) stepping to (6, 0) to push South down Column 6.
- Turn 34834: Boulder 1 at (6, 2), Player at (6, 1) facing South. Beginning empirical southward descent down Column 6.
- Turn 34835: Pushed Boulder 1 south from (6, 2) to (6, 3) [Player at (6, 2)]. Verified (6, 4) and (6, 5) are open dark checkerboard bridge floor.