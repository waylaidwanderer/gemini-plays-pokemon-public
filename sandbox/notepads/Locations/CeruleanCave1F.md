# Cerulean Cave (Unknown Dungeon) 1F - Layout & Notes

## Connected Component Graph (1F)
- **Entrance / Exit**: (24..25, 17) connects to Route 24 northern waterway.
- **Ladder B (East Landing)**: (23, 7) <-> 2F (22, 6).
- **Ladder C (Central Platform)**: (18, 9) <-> 2F (19, 7).
- **Ladder D (NE High Plateau)**: (27, 1) <-> 2F (29, 1).
- **Ladder E (NW Upper Shelf)**: (7, 1) <-> 2F (9, 1).
- **Ladder A (NW Lower Basin)**: Located at (1, 3) in the isolated NW lower basin. Note: Tile (5, 3) was empirically verified to be a solid rock wall (Turns 42824-42826), not a ledge. The NW Lower Basin is physically separated on 1F from the NW Upper Plateau (cols 5..16, rows 0..2) and the Western Ridge (cols 1..6, rows 8..12).

## Verified Topography & Transit (1F)
- **Central Platform**: Spans cols 11-18, rows 8-14.
  - Accessed from water via West Ramp at (11, 13) -> (11, 12).
  - Accessed from South Ground Highway via South Ramp at (17, 15) -> (17, 14).
  - Contains Ladder C at (18, 9).
- **South Ground Highway (Row 17)**: Continuous walkable ground spanning (1..16, 17).
  - West end connects via (2, 17) -> (2, 14) -> (1, 13) [Western Ridge South Ramp].
  - East end connects via (15, 17) -> (17, 15) [South Ramp onto Central Platform].
- **Western Ridge (South Sector)**: Cols 0-8, rows 8-13. Elevated plateau accessed via South Ramp at (1, 13). Visually confirmed on Turn 43751:
  - **Ladder at (3, 11)**: A clear ladder graphic is present at (3, 11) on this elevated plateau.
  - **Northern Boundary (Row 7-8)**: Lower ground visible north across rows 4-7 with a ladder visible at (0, 6) in the lower basin. Currently testing transition from (1, 8) to (1, 7).
- **Waterways**:
  - Northern Water Highway: Rows 4-5 (cols 14-20), Row 6-7 bypass (cols 10-15).
  - Western Water Channel: Cols 8-9 (rows 6-14).
  - Rock island at (10..13, 4..5) separates Northern Highway from Central canal.
- **East Landing Access (Verified Turn 42699)**: The East Landing (cols 21..25, rows 6..10 containing Ladder B at (23, 7)) cannot be boarded from the north (row 5); it is boarded from the south via the ramp at (25, 9) from the East Water Channel at (25, 10).
- **High NE Plateau (Verified Turn 42728)**: Spans cols 23..28, rows 0..2. Accessed via Ramp at (23, 3) from Northern Water Highway at (23, 4). Contains Ladder D at (27, 1) <-> 2F (29, 1). Blocked to west by solid rock wall at (19..22, 0..3).
- **NW Upper Shelf Topology & Probes (Turns 42733, 43519)**:
  - Accessed via Ramp at 1F (15, 3) from Northern Water Highway at 1F (15, 4).
  - Contains Ladder E at (7, 1) <-> 2F (9, 1).
  - Floor verified spanning (5..15, 0..2). Southern boundary at Row 3 is a cliff wall overlooking the NW Lower Basin.
  - Collision test on Turn 43519 confirmed Tile (4, 0) is a solid rock wall (blocked moving Left from (5, 0)).
  - Rows 1 and 2 at Column 4 are visually solid rock, while the shelf connects east to the water ramp at (15, 3). No confirmed ground path exists from this shelf to the NW basin.
- **East Landing to South Floor Connectivity (Verified Turns 42934, 43647)**:
  - Ramp at (21, 11) connects East Landing (cols 21..25, rows 6..10) down to an isolated lower pocket (cols 21..25, rows 12..15), bounded to the west by continuous Column 20 rock wall.
  - To traverse 1F to Central Platform, NE Plateau, or NW Shelf: Board water at East Landing Ramp (25, 9) -> Surf into East Water Channel at (25, 10).
  - Cave entrance/exit mat at (24..25, 17) connects to Route 24 waterway.

- **Central Platform Internal Topography (Turn 43466)**:
  - Row 12 is an open horizontal corridor spanning (11..15, 12) and (16..18, 12).
  - Column 15 connects (15, 12) south to (15, 14).
  - West Ramp at (11, 13) is accessed from (11, 12) by stepping Down.