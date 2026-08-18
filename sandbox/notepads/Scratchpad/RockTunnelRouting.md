# Scratchpad - Rock Tunnel Routing & Verified Forward Progression

## Verified Multi-Floor Ladder Bipartite Graph
- Ladder 1: 1F (37, 3) <---> B1F (33, 25) [Entrance sector <-> SE B1F]
- Ladder 2: 1F (5, 3) <---> B1F (27, 3) [NW 1F <-> N B1F]
- Ladder 3: 1F (23, 11) <---> B1F (17, 11) [Central 1F <-> Central B1F]
- Ladder 4: 1F (27, 3) <---> B1F (5, 3) [North-Central 1F <-> NW B1F]

## Outdoor Warps (Floor 1F Only)
- North Entrance: 1F (15, 3) <---> Route 10 North (Outside) [Verified Turn 3120, 3715, 4206]
- South Exit: 1F South Corridor (rows 33-35) -> Route 10 South (Outside -> Lavender Town) [Target Destination]

## Step-by-Step Forward Progression Plan (Avoiding Macro-Loops)
1. Current State: At 1F (5, 3) on Ladder 2.
2. Step 1 (1F NW -> Ladder 3): Walk South down cols 4-5 to row 14, East along row 14 to col 17, North to (23, 11). Descend Ladder 3 to B1F (17, 11).
3. Step 2 (B1F Central -> Ladder 4): Walk South down cols 14-17 to row 19, West along row 19 to col 3, North to (5, 3). Ascend Ladder 4 to 1F (27, 3).
4. Step 3 (1F North-Central -> South Exit):
   - From 1F (27, 3), walk South (cols 26-29) to row 11.
   - Walk East to col 32, South down Eastern Thoroughfare past row 14 to row 18.
   - Walk West along row 18 to col 23, South down col 23 to row 27.
   - Walk West along row 27 to col 17, South down col 17 to row 33.
   - CRITICAL: DO NOT step on Ladder 1 at (33, 25)!
   - Walk West along row 33 to test the exit doorway at cols 15-2 to exit into Route 10 South!
