# Route 10 - Map Layout, Ledges & Landmarks

## Overworld Layout & Structure
- **Dimensions:** Height = 36 blocks (144 tiles), Width = 10 blocks (40 tiles).
- **Global Alignment:** Route 10 starts at Column 50 of the global coordinate system.
- **Top Connection:** Connects West to Route 9 at the top-west (Block Rows 0 to 8).

## Verified Landmarks
- **Pokémon Center:** Located at tile coordinates x=58-61, y=68-71. 
  - Block 0x0d is the roof/building.
  - Block 0x7f is the door/window.
- **Rock Tunnel South Exit / Lavender Town Connection:** Located at the bottom of Route 10.

## Terrain & Ledges
- **Eastern River:** Columns 54-58 are water/river (specifically Column 54 is the shore, Columns 55-58 are water with animated wave sparkles).
- **Ledge on Row 13:** A horizontal ledge facing DOWN runs across Row 13 (Block Row 3, tiles y=12-15) from Columns 50 to 53.
  - Standing below the ledge (Row 14/15), you CANNOT walk UP to Row 12/13.
  - Thus, the pocket at (50, 14) to (53, 15) is a dead end from the south-west, but you can escape by walking Left back to Route 9.
- **Upper Level (Row 12/13):** Block Row 3 (tiles y=12-15) is completely walkable pavement from Column 52 to 58. This upper level allows players to walk east and go south to reach the Pokémon Center.

## Navigational Strategy
- To reach the Pokémon Center from Route 9:
  1. Walk UP through the gap at Columns 29/30 on Route 9 to Row 12 (middle lane).
  2. Walk EAST on Row 12/13 of Route 9 to Route 10, past Column 50, to Column 58 (upper pavement).
  3. From the upper level of Route 10, walk SOUTH directly to the Pokémon Center on Row 17 (y=68).
## Verified Obstacles & Navigation Limits (Turn 8878)
- **Row 16 Rock Wall:** Completely solid and continuous across Columns 50 to 57, making Route 10's lower pocket (Columns 50-53, Rows 14-15) a strict dead end going south.
- **Row 13 Ledge:** Continuous across Columns 50 to 53, blocking all upward (northward) movement to the upper level of Route 10.


## ROM Tile Map 2x Coordinate Scaling (Critical)
- **Scale Factor:** The raw tile map file `route10_tile_map.txt` is exactly **2x scaled** relative to the in-game global coordinate grid reported by the harness.
- **Mapping Formula:** To map from in-game global coordinates `(x_game, y_game)` to the raw file indices `(x_file, y_file)`:
  - `x_file = (x_game - 50) * 2`  (maps to file columns `2 * (x_game - 50)` and `2 * (x_game - 50) + 1` since Route 10 starts at global `x_game = 50`)
  - `y_file = y_game * 2`        (maps to file rows `2 * y_game` and `2 * y_game + 1`)
- **Strict Spatial Consistency:** Each 1x1 in-game overworld tile corresponds to a 2x2 block of raw tiles in `route10_tile_map.txt`. All pathfinding and navigation scripts MUST apply this 2x multiplier before reading from or writing to the file representation.
