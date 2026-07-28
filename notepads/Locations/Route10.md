# Route 10 - Map Layout, Ledges & Landmarks

## Overworld Layout & Structure
- **Dimensions:** Height = 36 blocks (144 tiles), Width = 10 blocks (40 tiles).
- **Global Alignment:** Route 10 starts at Column 50 of the global coordinate system.
- **Top Connection:** Connects West to Route 9 at the top-west.
- **River Division & Coordinate Transition:** Crossing East from (59, 8) on the West side of Route 10 transitions the player to the East side of Route 10, where coordinates reset to (0, 8) (verified on Turn 10053).

## Verified Landmarks
- **Pokémon Center:** Located on the east side of Route 10, adjacent to the Rock Tunnel entrance. 
  - **Exterior Location:** Entrance Door is at (11, 19) (verified on Turn 10075).
  - **Interior Location:** Nurse Joy is behind the counter at (3, 2). Exiting from (3, 7) warps the player back to Route 10 East at (11, 20).
- **Rock Tunnel Entrance:** Located on Route 10 East at (14, 11) (verified on Turn 10221). Walking UP from (14, 12) triggers the warp/map transition into Rock Tunnel 1F.

- **Rock Tunnel South Exit / Lavender Town Connection:** Located at the bottom of Route 10.

## Terrain & Ledges
- **Eastern River:** Columns 54-58 are water/river (specifically Column 54 is the shore, Columns 55-58 are water with animated wave sparkles).
- **Ledge on Row 13:** A horizontal ledge facing DOWN runs across Row 13 (tiles y=12-15) from Columns 50 to 53.
  - Standing below the ledge (Row 14/15), you CANNOT walk UP to Row 12/13.
  - Thus, the pocket at (50, 14) to (53, 15) is a dead end from the south-west, but you can escape by walking Left back to Route 9.

## Navigational Strategy
- Row 8/9 is the open pavement path from Route 9 going east to Column 59 on Route 10.
- Column 52 and 53 on Row 9 are the only columns where you can walk down to the lower level of Route 10 (containing the grass lanes).
- Column 54 is mountain wall on rows 10 to 13, which blocks any eastward traversal on those lower rows.
## Verified Obstacles & Navigation Limits (Turn 8878)
- **Row 16 Rock Wall:** Completely solid and continuous across Columns 50 to 57, making Route 10's lower pocket (Columns 50-53, Rows 14-15) a strict dead end going south.
- **Row 13 Ledge:** Continuous across Columns 50 to 53, blocking all upward (northward) movement to the upper level of Route 10.

## ROM Tile Map 2x Coordinate Scaling (Critical)
- **Scale Factor:** The raw tile map file `route10_tile_map.txt` is exactly **2x scaled** relative to the in-game global coordinate grid reported by the harness.
- **Mapping Formula:** To map from in-game global coordinates `(x_game, y_game)` to the raw file indices `(x_file, y_file)`:
  - `x_file = (x_game - 50) * 2`  (maps to file columns `2 * (x_game - 50)` and `2 * (x_game - 50) + 1` since Route 10 starts at global `x_game = 50`)
  - `y_file = y_game * 2`        (maps to file rows `2 * y_game` and `2 * y_game + 1`)
- **Strict Spatial Consistency:** Each 1x1 in-game overworld tile corresponds to a 2x2 block of raw tiles in `route10_tile_map.txt`. All pathfinding and navigation scripts MUST apply this 2x multiplier before reading from or writing to the file representation.