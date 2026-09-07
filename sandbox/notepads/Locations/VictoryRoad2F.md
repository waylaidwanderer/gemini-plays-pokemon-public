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
- **Switch 1 @ (1, 16)**: Activated by pushing Boulder (4, 14) onto (1, 16). Lowers Shutter 1 at (5, 10) and Shutter 3 at (21, 15).
- **Central-South Boulder & Switch**: Boulder at (9, 11) with switch at (9, 16) and shutter at (15, 15).
- **Pit Drop Landing**: Falling through 3F Pit drops player to 2F around (22, 16) / (23, 16).

## Verified NW Sector & Lower Floor Access (Verified Turn 34008)
- NW Ladder @ (1, 1) connects to 3F (2, 0).
- Row 1 Highway: (1..10, 1) connects NW Ladder to central corridors.
- Boulder at (5, 5): Pushed down/east to (6, 6) to open the passage between northern plateau and southern rows 6-7.
- Columns 2-3 Highway: Columns 2 and 3 (y=7..10+) form an unobstructed 2-tile wide vertical highway connecting Row 7 down into the lower western floor (rows 8-16, Switch 1 @ (1, 16) and Boulder @ (4, 14)).

## Verified Puzzle Reset Triggers (Verified Turn 34061)
- Map reload events (such as ascending/descending floor ladders, leaving through cave entrances, or using Dig/Escape Rope) completely reload the floor's map state and reset all pushable boulders back to their default starting positions.
- Switch activations and shutter gates on a given floor are temporary for the active visit; they persist while remaining on that floor, but reset to closed when the floor is reloaded.
