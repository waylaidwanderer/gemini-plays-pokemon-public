# Route 9 - Spatial Coordinates, Landmarks & Trainer Log

## Overworld Layout & Navigation
- **Western Entrance:** Connects to Cerulean City at `(39, 16)`.
- **Cuttable Bush:** Located at `(5, 8)`. This bush must be cut using HM01 (Cut) to unlock access to the eastern path.
- **Escape Gap (from bottom lane):** Standing at `(19, 14)` and walking UP through `(19, 13)` to `(19, 12)` allows players to exit the lower dead-end pocket and return to the main upper lanes.

## Key Items Found
- **TM30 (Teleport):** Retreived from a Poké Ball at `(10, 15)` inside the southern pocket.

## Trainer Roster & Coordinates
| Trainer Name | Location / Coordinates | Trainer Roster | Earnings / Turn | Notes |
|--------------|------------------------|----------------|-----------------|-------|
| JR. TRAINER♀ | (12, 10) / (13, 10)    | Oddish, Bellsprout (Lv 18) | ¥360 / Turn 7197 | Defeated! |
| Hiker Alan   | (45, 15)               | Geodude, Onix              | ¥735 / Turn 7280| Defeated! |
| JR. TRAINER♂ | (24, 7)                | Growlithe (Lv 21), Charmander (Lv 21) | ¥420 / Turn 7479 | Defeated! |
| Bug Catcher Conner | (40, 8)          | Bug Pokémon (unfought)                | ¥320 / Turn 7431 | Defeated! |
| JR. TRAINER♂ | (34, 7)                | Rattata (Lv 19), Diglett (Lv 19), Ekans (Lv 19), Sandshrew (Lv 19) | ¥380 / Turn 7528 | Defeated! |
## Ledge & Pockets Layout
- **Upper Pavement Lanes (Rows 8, 9, 10):** Main path going east/west.
  - Rows 8 & 9: Completely clear pavement going west from Column 20 to Column 0. Bypasses the trainer at (13, 10) by walking on Row 9.
  - Row 10: Blocked at (9, 10) by a mountain wall. Contains JR. TRAINER♀ at (13, 10) (facing down, defeated).
- **Ledge on Row 11 (Columns 10-19):** Blocks going UP from Row 12 (grass lane) to Row 11 (pavement). This ledge ends at Column 20, which is clear pavement. Note: The boundary at Column 45/46 on Row 6-10 is a solid rock cliff/mountain wall and is NOT a jumpable ledge from the west.
- **Grass Lane (Row 12, Columns 10-19):** Bounded by Row 11 ledge on top and Row 13 ledge on bottom. Blocked on the west (Column 9) by a mountain wall. To return to the upper lanes from here, walk east to Column 20, then walk UP to Row 11/10.
- **Row 13 Ledge & Gap (Columns 20-53):** Blocks going UP from Row 14 (lower pavement) to Row 12 (grass). This ledge has an **empirically verified open gap at Columns 29 and 30** (discovered on Turn 7376, verified on Turn 7451), allowing players to walk UP from (29, 14) to (29, 12).
- **Row 9 Ledge & Gap (Columns 20-25):** Blocks going UP from Row 10 to Row 8. This ledge has an **empirically verified open gap at Column 29** (discovered on Turn 7399), allowing players to walk UP from (29, 10) to (29, 8/9).
- **Lower Pavement Lane (Row 14/15, Columns 10-53):** Bounded by Row 13 ledge on top. Blocked on the west (Column 9) by a mountain wall. Contains Hiker Alan at (45, 15) and Hiker at (16, 15) facing right. Escape Gap is at (19, 14), walking UP through (19, 13) to (19, 12) into the grass lane.
## Empirical Navigation Realities
- **Column 42 Blockage on Row 12:** Empirically verified multiple times that Row 12 is completely blocked at Column 42 by a solid diagonal rock cliff face.
- **Ledge & Mountain Layout:** Row 9 is blocked at Column 42 by a solid rock wall. Columns 26-28 are also blocked on Rows 2-7 by a solid rock wall. Row 14/15 is open but Column 24-27 has a rock wall. Route 10 lower pocket is a dead end blocked by Row 16 rock wall.
- **Geographical Strategy:** Backtracking to Cerulean City on foot from Route 9's eastern sections is possible! On Turn 8921, we successfully backtracked by cutting the bush at (5, 8) and walking west on Rows 2-4 (which are completely clear on Columns 13-22 and do not have any one-way ledge blockages on those upper rows).
## Verified Obstacles & Navigation Limits (Turn 8878)
- **Column 41 Vertical Corridor:** Empirically verified to be completely open vertically with absolutely NO ledges or rock walls from Row 6 down to Row 14, providing a crucial north/south crossing corridor.
- **Row 13 Ledge Lip:** Continuous across Columns 40 to 53, blocking all upward (northward) movement from Row 14/15 on the eastern side.
- **Columns 24-27 Rock Wall on Row 14-15:** Blocks eastward movement on the lower lanes.
- **Column 19 Vertical Ledge on Rows 8-11:** Blocks westward (backtracking) movement on the upper lanes.
- **Column 24/25 Vertical Ledge on Rows 5-6:** Blocks westward (leftward) movement on the upper lanes.


## ROM Tile Map 2x Coordinate Scaling (Critical)
- **Scale Factor:** The raw tile map file `route9_tile_map.txt` is exactly **2x scaled** relative to the in-game global coordinate grid reported by the harness.
- **Mapping Formula:** To map from in-game global coordinates `(x_game, y_game)` to the raw file indices `(x_file, y_file)`:
  - `x_file = x_game * 2`  (maps to file columns `2 * x_game` and `2 * x_game + 1`)
  - `y_file = y_game * 2`  (maps to file rows `2 * y_game` and `2 * y_game + 1`)
- **Strict Spatial Consistency:** Each 1x1 in-game overworld tile corresponds to a 2x2 block of raw tiles in `route9_tile_map.txt`. All pathfinding and navigation scripts MUST apply this 2x multiplier before reading from or writing to the file representation.

- **Route 9 East Pocket (Columns 45-46, Rows 6-7):**
  - **Column 44:** Open pavement. Does NOT block westward (leftward) movement.
  - **Column 46 Rock Wall:** Solid rock wall blocks all eastward (rightward) movement across Column 46 on Rows 4-7.
  - **Row 7 Ledge and Row 8 Diagonal Rock Wall Blockage:** Jumping DOWN from (45, 7) onto (45, 8) is blocked because (45, 8) is a diagonal rock corner tile.
  - **Escape Route:** You can simply walk Left (west) back across Column 44 onto Column 41/42 to exit the pocket. No soft-lock or warp is required.