# Scratchpad - Rock Tunnel Routing & Verified Bipartite Traversal

## Verified Multi-Floor Ladder Bipartite Graph
- Ladder 1: 1F (37, 3) <---> B1F (33, 25) [Entrance sector <-> SE B1F]
- Ladder 2: 1F (5, 3) <---> B1F (27, 3) [NW 1F <-> N B1F]
- Ladder 3: 1F (23, 11) <---> B1F (17, 11) [Central 1F <-> Central B1F]
- Ladder 4: 1F (27, 3) <---> B1F (5, 3) [North-Central 1F <-> NW B1F]

## Outdoor Warps (Floor 1F Only)
- North Entrance: 1F (15, 3) <---> Route 10 North (Outside)
- South Exit: 1F (15, 33) <---> Route 10 South (Outside -> Lavender Town)

## Full Traversal Route (Entrance -> Exit)
1. 1F (37, 3): Descend Ladder 1 -> B1F (33, 25).
2. B1F (33, 25): Walk South to row 31, West along row 31 to col 15, North to (27, 3). Ascend Ladder 2 -> 1F (5, 3).
3. 1F (5, 3): Walk South down cols 4-5 to row 14, East along row 14/21 to (23, 11). Descend Ladder 3 -> B1F (17, 11).
4. B1F (17, 11): Walk South down cols 14-17 to row 19, West along row 19 to col 3, North to (5, 3). Ascend Ladder 4 -> 1F (27, 3).
5. 1F (27, 3): Walk South (cols 26-29) -> East to col 32 -> South down Eastern Thoroughfare to row 18 -> West to col 23 -> South to row 27 -> West to col 17 -> South to row 33 -> West to (15, 33) -> Step Down to exit to Route 10 South! (DO NOT step on Ladder 1 at 33, 25).
