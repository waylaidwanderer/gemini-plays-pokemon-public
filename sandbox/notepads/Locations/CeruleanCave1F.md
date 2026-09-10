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
- **Western Ridge (South Sector)**: Cols 1-6, rows 8-12. Elevated plateau accessed via South Ramp at (1, 13). Contains standard floor; bounded to north by Row 7 cliff wall.
- **Waterways**:
  - Northern Water Highway: Rows 4-5 (cols 14-20), Row 6-7 bypass (cols 10-15).
  - Western Water Channel: Cols 8-9 (rows 6-14).
  - Rock island at (10..13, 4..5) separates Northern Highway from Central canal.
- **East Landing Access (Verified Turn 42699)**: The East Landing (cols 21..25, rows 6..10 containing Ladder B at (23, 7)) cannot be boarded from the north (row 5); it is boarded from the south via the ramp at (25, 9) from the East Water Channel at (25, 10).
- **High NE Plateau (Verified Turn 42728)**: Spans cols 23..28, rows 0..2. Accessed via Ramp at (23, 3) from Northern Water Highway at (23, 4). Contains Ladder D at (27, 1) <-> 2F (29, 1). Blocked to west by solid rock wall at (19..22, 0..3).
- **NW Upper Shelf / Plateau (Verified Turn 42733)**: Accessed via Ramp at 1F (15, 3) from Northern Water Highway at 1F (15, 4). Spans cols 0..16, rows 0..2. Contains Ladder E at (7, 1) <-> 2F (9, 1). Continues west towards western boundary.
- **East Landing to South Floor Connectivity (Verified Turns 42934, 42939)**:
  - Ramp at (21, 11) connects East Landing (cols 21..25, rows 6..10) directly down to South Ground Level (cols 20..25, rows 12..15).
  - Cave entrance/exit mat at (24..25, 17) connects to Route 24 waterway.
## NW Sector Topology Ground Truth (Verified Turn 43125 Screen)
- Ladder at (9, 1) on 1F <-> 2F (9, 1).
- Row 1: Floor at (3..8, 1). (1..2, 1) and (10, 1) are solid rock.
- Column 3: Floor at (3, 1..3).
- Row 3: Floor at (3..9, 3).
- Ladder A at (1, 3): Blue ladder icon visible at (1, 3)!
  - (1, 2) is floor above Ladder A.
  - (2, 3) is solid rock between Column 3 and Ladder A.
- Column 9: Connects Row 3 at (9, 3) south via (9, 4..5).
- Row 5: Floor at (1..7, 5) and (9, 5). Tile (8, 5) is solid rock.