# Victory Road 2F - Verified Layout & Matrix

## Floor Elevation & Physical Topography
- Lower Cave Floor (Light Purple / Dots): Rows 8-16, Columns 1-26.
- Upper Plateau (Dark Checkerboard): Rows 0-7, Rows 11-13 in central-east sections.
- Impassable South-Facing Cliffs:
  - Row 7 cliff (cols 5-14): Separates Row 7 (upper plateau) from Row 8 (lower floor). Cannot walk North from Row 8 onto Row 7.
  - Row 11 cliff (cols 21-27): Separates Row 11 (upper plateau) from Row 12 (lower floor). Cannot walk South or North between Row 11 and Row 12.
- Vertical Rock Dividers:
  - Column 12 rock wall (y=10..15): Separates western floor (cols 1-5) from central floor (cols 13-26).
  - Column 14-15 rock wall (y=0..7): Solid rock wall dividing northern upper plateau east/west.

## Verified Ladders & Connectivity Matrix
1. **Ladder 1F <-> 2F (Southwest Ladder)**:
   - Coordinates: (0, 8) on 2F <-> (1, 1) on 1F.
   - Access: Sits at (0, 8) in western lower corridor.
2. **NW Ladder to 3F**:
   - Coordinates: (1, 1) on 2F <-> (2, 0) on 3F.
   - Location: Northwest corner of 2F upper plateau. Connects to 3F NW room.
3. **Ladder A to 3F (Central-East Ladder)**:
   - Coordinates: (23, 7) on 2F <-> (23, 7) on 3F.
   - Location: Wall ladder on 2F east sector upper plateau. Connects to 3F at (23, 7).
4. **Ladder B to 3F (SE Pit Room Ladder)**:
   - Coordinates: (25, 14) on 2F <-> (25, 14) on 3F.
   - Location: Southeast room on 2F lower purple floor.
5. **Ladder NE to 3F (Exit Chamber Ladder)**:
   - Coordinates: (27, 7) on 2F <-> (27, 7) on 3F.
   - Location: Northeast chamber behind shutter at (27, 10). Leads to 3F final exit.

## Switches & Shutters on 2F
- **Switch 1 @ (1, 16) - Verified Master Protocol**:
  1. Default State: Boulder at (4, 14), Switch 1 at (1, 16).
  2. Stand at (5, 14) -> Push Left 1 time to (3, 14) [Boulder at (3, 14), Player at (4, 14)].
  3. Reposition to (3, 13) via (4, 13) -> (3, 13).
  4. Stand at (3, 13) -> Push Down 2 times along Column 3 to (3, 16) [Boulder at (3, 16), Player at (3, 15)].
  5. Reposition to (4, 16) via (4, 15) -> (4, 16) (standing on open floor east of boulder).
  6. Stand at (4, 16) -> Push Left 2 times along row 16 onto Switch (1, 16) [Boulder at (1, 16), Player at (2, 16)].
  7. Outcome: Switch 1 activates, lowering Shutter 1 at (5, 10) and Shutter 3 at (21, 15).
- **Pit Drop Landing**: Falling through 3F Pit drops player to 2F around (22, 16) / (23, 16).

## NW Sector & Lower Floor Access
- SW Ladder (0, 8) connects directly to Columns 2-3 Highway via (0, 6) -> (1, 6) -> (2, 6..7).
- Row 4 contains a rock divider at (0..4, 4) and (6..8, 4) with (5, 4) open north of Boulder (5, 5).
- **NW Boulder Constraint (Verified Turn 36671)**: Pushing Boulder from (5, 5) to (5, 4) and then (5, 3) dead-ends against the solid rock obstacle at (5, 2). Lateral access at (4, 4)/(6, 4) is blocked by solid rock walls, so the NW plateau cannot be passed through this corridor; 3F must be accessed via the Eastern Wing ladders.
- Columns 2-3 Highway: Columns 2 and 3 form an unobstructed 2-tile wide vertical highway spanning rows 6 through 16, connecting the upper room at row 6 directly to the lower floor (rows 12-16), Switch 1 @ (1, 16), and Boulder @ (4, 14). Note: Columns 0-4 are blocked north of row 6 by the Row 4 rock wall.

## Puzzle Reset Triggers
- Map reload events (such as ascending/descending floor ladders, leaving through cave entrances, or using Dig/Escape Rope) completely reload the floor's map state and reset all pushable boulders back to their default starting positions.
- Switch activations and shutter gates on a given floor are temporary for the active visit; they persist while remaining on that floor, but reset to closed when the floor is reloaded.
- **Shutter 2 @ (15, 15)**: Connects eastern corridor (15, 14) directly to Row 16 southern highway at (15, 16).
- **Row 16 Highway**: Row 16 is completely open dark checkerboard floor across columns 9 to 27, connecting Central Chamber (cols 9-11) directly to East Sector (cols 21-27).

## Eastern Sector & Corridor Boundaries
- Lower purple floor runs along rows 12-14 from column 13 to column 22.
- Rock wall at (22, 12..15) and obstacle at (23, 14) separate western lower floor from eastern room.
- Column 15 rock wall at (15, 8..11) divides western upper plateau from eastern upper plateau (Moltres at (19, 8)).
- Shutter 1 at (5, 10) and Shutter 3 at (21, 15) connect through the southern Row 16 highway.
## 2F Pit Drop & Exit Investigation (Turn 35671)
- Pit Boulder dropped from 3F lands on 2F at (23, 16).
- Empirical test: Pushing boulder East into (29, 16) dead-ends against (30, 16) rock wall and does NOT open Exit Shutter at (27, 10). Shutter at (27, 10) confirmed closed on Turn 35669.
## Observed Landmarks
- Shutter at (28, 10): Observed blocking Column 28 passage into Ladder NE Room (rows 7-9, cols 26-29).
- Ladder NE at (27, 7): Wall ladder in enclosed NE room on 2F (cols 26-29, rows 7-9), isolated from main Row 8 corridor by rock wall at cols 24-25.
## Verified Southern Highway & Exit Corridor (Turns 36693-36713)
- **Row 16 Highway**: Spans continuously from Switch 2 at (9, 16) all the way east to (28, 16).
- **Column 28 Avenue**: Spans rows 11 through 16 along column 28, connecting Row 16 at (28, 16) north to (28, 11) directly facing the Exit Shutter at (28, 10).
- **Exit Shutter & NE Ladder**: Exit Shutter at (28, 10) blocks entrance into the NE Room (cols 26-29, rows 7-9) containing Ladder NE at (27, 7) which ascends to 3F Exit Room towards Indigo Plateau.
- **Switch 2 @ (9, 16)**: Sits at the western terminus of Row 16 highway, connecting directly north via Column 9 into the Central Chamber.
## Central Chamber Topology (Verified Turn 36715)
- **Central Corridor (cols 9-11, rows 11-16)**: Connects Switch 2 at (9, 16) north along column 9 to (9, 11).
- **Row 10 Rock Divider (cols 6-12, row 10)**: Solid horizontal rock barrier dividing Central Chamber (row 11) from northern purple corridor (row 8).
- **Passage to Western Sector**: Row 11 dark checkerboard floor spans across (5..7, 11), connecting directly to lowered Shutter 1 at (5, 10).