# Scratchpad - Rock Tunnel Routing & Verified Dungeon Topology

## Verified Ladder Network & Dungeon Structure
- Entrance: Route 10 North -> Rock Tunnel 1F at (15, 3).
- Ladder 1: 1F (37, 3) <-> B1F (33, 25) [Verified Turn 3460, 3766]
- Ladder 2: 1F (5, 3) <-> B1F (27, 3) [Verified Turn 3640, 3788, 3978, 4023]
- Ladder 3: B1F (23, 11) -> leads to southern sector of 1F (NPC at 22, 24 and exit to Route 10 South / Lavender Town).

## Verified Collision Bounds on 1F
1. North Entrance Chamber (cols 14-17, rows 2-7):
   - East connects to col 18-23 (rows 2-5).
   - West is BLOCKED by solid rock wall at cols 12-13 (rows 2-7). No direct row 3 connection to Ladder 2.
   - South connects via col 17 (rows 4-14) directly down to Middle Highway at row 14.
2. Middle Highway (row 14, cols 5-17):
   - Continuous horizontal passage connecting col 17 all the way west to col 5.
3. Western Upper Corridor (col 5, rows 3-14):
   - Continuous vertical passage connecting Middle Highway at (5, 14) north to Ladder 2 at (5, 3).

## Active Navigation Route to Ladder 2 (5, 3) -> B1F (23, 11)
1. Flee wild Zubat at (17, 3).
2. Move South 11 steps down col 17: (17, 3) -> (17, 14).
3. Move West 12 steps along row 14: (17, 14) -> (5, 14).
4. Move North 11 steps up col 5: (5, 14) -> (5, 3) [Ladder 2].
5. On B1F from (27, 3), navigate to Ladder 3 at (23, 11) and ascend to the 1F southern sector.
