# Victory Road 3F - Layout & Topology

## Ladders & Exits
- NW Ladder (from 2F NW (1, 1)): Located at (2, 0) in isolated NW room
- Ladder A (from 2F (23, 7)): Arrival tile at (23, 7) on upper plateau from 2F (23, 7). (Note: Descent from 3F (23, 7) is not bidirectional; use Ladder NE at (27, 7) or Ladder B at (25, 14) to descend).
- Ladder NE (to 2F): Located at (27, 7) in an isolated northeastern corridor (rows 7-9, cols 25-29) bounded by solid rock walls at row 6 and row 10.
- Ladder B (to 2F SE): Located at (25, 14) in SE Lower Purple Room
- The Pit / Hole: Located at (23, 14) in SE Lower Purple Room.

## Physical Features & Topography
- Northern Highway (Rows 0-1): Continuously open from Column 27 west through Column 13 and beyond! Row 1 connects directly across all northern columns, while Row 2 (Purple Chamber) is separated from Row 1 by a solid cliff/wall.
- NW Room Access: Connected to Central Bridge (Columns 6-7) via Row 2 ((6, 2) -> (2, 2)) and to 2F NW Ladder (1, 1) <-> 3F (2, 0). Note: (6, 7) at the south base of Central Bridge is an impassable wall.
- Upper Dark Plateau (rows 0-11, cols 15-28): Contains Ladder A (23, 7), Ladder NE (27, 7), and connects via southern corridor (row 11) to column 28/29.
- Central Bridge (Columns 6-7): Spans rows 0-6 connecting Northern Highway (Row 1) south to NW Room and Row 6 cross-corridor.
- Central Corridor (Columns 9-10): Vertical corridor spanning rows 2-10 (terminates at (10, 10)).
- Purple Chamber (rows 2-4, cols 14-18): Connected west to central corridor via row 2 (cols 9-18). Separated from Northern Highway by solid north wall at row 2, and blocked to the south by rock walls and Shutter at (17, 5).
- SE Lower Purple Floor (rows 12-14, cols 10-26): Accessible via 2F Ladder B at (25, 14). Contains Boulder 3 at (13, 12), the Pit at (23, 14), and Ladder B at (25, 14).

## Discovered Points of Interest & Topology
- [ ] Item Ball at (11, 0) in northern corridor of western sector.

- Shutter at (17, 5): Horizontal purple bars blocking passage south from row 4 purple room to row 6.

## Northern Highway Branch Corridors & Scout Checklist
- Column 17: Open 1-tile gap at row 4 connecting rows 1-3 to rows 6-11 (Upper Dark Plateau & Ladder A arrival).
- Columns 9-10: North wall at row 2 separates row 1 Northern Highway from Purple Chamber.
- Columns 6-7 (Central Bridge): Spans rows 0-6 connecting Northern Highway (Row 1) south to NW Room and Row 6 cross-corridor.
- Columns 0-5 (Far West Room): Contains Switch Plate at (3, 5) and Ladder to 2F NW at (2, 0).

## NW Room & Switch Plate
- Empirically Verified (Turns 30576, 30680, 30756, 30818): NW Room contains Switch Plate at (3, 5), but NO pushable boulder exists inside the room.
- Row 6 Boundary (Turn 30818): Stepping South from (2, 5) onto (2, 6) confirmed that Row 6 ((2..5, 6)) is an IMPASSABLE SOLID WALL (not a hop-able ledge). The NW room does not connect to the southern sector.

## 3F Pit Area & Boulder Observations
- Column 13 / Row 11: Pushing boulder at (13, 12) down to (13, 13) dead-ends against rock obstacle at (13, 14).


## 3F Default Boulder & Switch Layout
- Note: Warping out via Dig / Escape Rope resets all dungeon entities to default spawn positions.
- Boulder 1 default position: (22, 3) on Upper Dark Plateau.
- Row 11/12 Elevation Cliff (Empirically Verified Turn 29996): Row 11 is an impassable south-facing cliff wall separating the Upper Dark Plateau from the Lower Purple Floor (rows 12-14). Access from Row 11 to the Lower Highway (Row 16) requires walking east to Eastern Outer Corridor (cols 28-29) and south to row 16.
- Row 16 Lower Highway: Spans east-west along rows 16-17, connecting Eastern Outer Corridor (cols 28-29) westward beneath the rock obstacles.
## Obstacles & Blockages (Verified Turn 30600)
- Column 11 Wall: Column 11 (x=11, y=5..10) is a solid vertical rock barrier blocking Row 6 westward passage at (11, 6). Boulders pushed west past (17, 6) stop at (12, 6) and cannot be pushed further west or south.
- Row 7 Ledge / Wall: Impassable from (13, 6) south to (13, 7). Bypass east via Row 6 to (17, 6).

## Master Boulder 1 to Switch (3, 5) Solution (VERIFIED & SOLVED Turn 30921)
1. Strength activated by ATLAS on 3F Upper Dark Plateau.
2. Initial State: Boulder 1 at (22, 3).
3. Position at (22, 4) -> Push North 2 times to (22, 1) on Row 1 (Northern Highway).
4. Reposition via (22, 3) -> (23, 3) -> (23, 1).
5. Push West along Row 1: (22, 1) -> (21, 1) -> (20, 1) -> (19, 1) -> (18, 1) -> ... -> (6, 1).
6. At (6, 1), stand at (6, 0) and push South 1 time to (6, 2) on Central Bridge.
7. Stand at (7, 2) and push West into NW Room at (5, 2) -> (4, 2) -> (3, 2).
8. Note: Tile (3, 3) is a rock obstacle! Bypass to (2, 2):
   - From (4, 2), push Left to (2, 2) [Boulder at (2, 2)].
   - Reposition to (2, 1) via (3, 2) -> (3, 1) -> (2, 1).
   - Push South down Column 2: (2, 2) -> (2, 3) -> (2, 4) -> (2, 5) [Boulder at (2, 5), Player at (2, 4)].
   - Reposition to (1, 5) via (2, 4) -> Left to (1, 4) -> Down to (1, 5).
   - Stand at (1, 5) facing East -> Push Right 1 time onto Switch Plate (3, 5)!
9. Outcome: Switch (3, 5) ACTIVATED! Shutter at (17, 5) OPENED!