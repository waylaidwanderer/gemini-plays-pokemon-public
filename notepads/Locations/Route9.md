# Route 9 - Spatial Coordinates, Landmarks & Trainer Log

## Overworld Layout & Navigation
- **Western Entrance:** Connects to Cerulean City at `(39, 16)`.
- **Cuttable Bush:** Located at `(5, 8)`. This bush must be cut using HM01 (Cut) to unlock access to the eastern path.
- **Escape Gap (from bottom lane):** Standing at `(19, 14)` and walking UP through `(19, 13)` to `(19, 12)` allows players to exit the lower dead-end pocket and return to the main upper lanes.

## Key Items Found
- **TM30 (Teleport):** Retreived from a Poké Ball at `(10, 15)` inside the southern pocket.

## Trainer Roster & Coordinates
| Trainer Name | Location / Coordinates | Trainer Roster | Notes |
|--------------|------------------------|----------------|-------|
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
- **Row 13 Ledge & Gap (Columns 20-53):** Blocks going UP from Row 14 (lower pavement) to Row 12 (grass). This ledge has an **empirically verified open gap at Columns 29 and 30** , allowing players to walk UP from (29, 14) to (29, 12).
- **Row 9 Ledge & Gap (Columns 20-25):** Blocks going UP from Row 10 to Row 8. This ledge has an **empirically verified open gap at Column 29** , allowing players to walk UP from (29, 10) to (29, 8/9).
- **Lower Pavement Lane (Row 14/15, Columns 10-53):** Bounded by Row 13 ledge on top. Blocked on the west (Column 9) by a mountain wall. Contains Hiker Alan at (45, 15) and Hiker at (16, 15) facing right. Escape Gap is at (19, 14), walking UP through (19, 13) to (19, 12) into the grass lane.
## Empirical Navigation Realities
- **Column 42 Blockage on Row 12:** Empirically verified multiple times that Row 12 is completely blocked at Column 42 by a solid diagonal rock cliff face.
- **Ledge & Mountain Layout:** Row 9 is blocked at Column 42 by a solid rock wall. Columns 26-28 are also blocked on Rows 2-7 by a solid rock wall. Row 14/15 is open but Column 24-27 has a rock wall. Route 10 lower pocket is a dead end blocked by Row 16 rock wall.
- **Geographical Strategy:** Backtracking to Cerulean City on foot from Route 9's eastern sections is possible! On Turn 8921, we successfully backtracked by cutting the bush at (5, 8) and walking west on Rows 2-4 (which are completely clear on Columns 13-22 and do not have any one-way ledge blockages on those upper rows).
## Verified Obstacles & Navigation Limits 
- **Column 41 Vertical Corridor:** Empirically verified to be completely open vertically with absolutely NO ledges or rock walls from Row 6 down to Row 14, providing a crucial north/south crossing corridor.
- **Row 13 Ledge Lip:** Continuous across Columns 40 to 53, blocking all upward (northward) movement from Row 14/15 on the eastern side.
- **Columns 24-27 Rock Wall on Row 14-15:** Blocks eastward movement on the lower lanes.
- **Column 19 Vertical Ledge on Rows 8-11:** Blocks westward (backtracking) movement on the upper lanes.
- **Column 24/25 Vertical Ledge on Rows 5-6:** Blocks westward (leftward) movement on the upper lanes.
- **Row 17 Water/River Barrier:** Row 17 on Route 9 contains animated river/water tiles (represented by '8788/9392' and '50f8/948d' under dx=0) which completely block foot traversal eastward across Columns 20 to 50.


## ROM Tile Map 2x Coordinate Scaling (Critical)
- **Vertical Scale Factor:** The raw tile map file `route9_tile_map.txt` is exactly **2x scaled** vertically relative to the in-game global coordinate grid reported by the harness.
  - `y_file = y_game * 2`  (maps to file rows `2 * y_game` and `2 * y_game + 1`)
- **Horizontal Scale Alignment:**
  - The horizontal alignment has no offset (dx = 0).
  - `x_file = x_game * 2` (maps to file columns `2 * x_game` and `2 * x_game + 1` since the file represents a 120-column grid, i.e., 60-tile wide map).

- **Route 9 East Pocket (Columns 45-46, Rows 6-7):**
  - **Column 44:** Open pavement. Does NOT block westward (leftward) movement.
  - **Column 46 Rock Wall:** Solid rock wall blocks all eastward (rightward) movement across Column 46 on Rows 4-7.
  - **Row 7 Ledge and Row 8 Diagonal Rock Wall Blockage:** Jumping DOWN from (45, 7) onto (45, 8) is blocked because (45, 8) is a diagonal rock corner tile.
  - **Escape Route:** You can simply walk Left (west) back across Column 44 onto Column 41/42 to exit the pocket. No soft-lock or warp is required.
## Verified Overworld Realities & Escape Routing 
- **Continuous Ledge on Row 13:** Row 13 is a continuous downward-facing ledge from Column 10 all the way to Column 23, blocking all upward movement on the west/middle sections. Column 29 and Column 30 are the only open gaps in the Row 13 ledge.
- **Continuous Ledge on Row 11:** Row 11 contains a continuous downward-facing ledge from Column 10 to Column 19, blocking all upward movement on these columns.
- **Solid Wall on Column 24:** Column 24 contains a solid rock wall blocking all horizontal movement on Rows 11 to 15. Thus, the lower pocket of Route 9 (Columns 10-23, Rows 12-15) is completely dead-ended going east.
- **Solid Wall on Column 9:** Column 9 contains a solid rock wall blocking all horizontal movement on Rows 10 to 17.

- **Verified Row 9 Escape Corridor:** Row 9 is completely open pavement and grass from Column 29 all the way west to Column 0, providing a clear escape route back to Cerulean City.
- **True Escape Path from Lower Pocket:** To escape the lower pocket, walk to Column 19 on Row 14, walk UP Column 19 (which has no ledge lip on Row 13) to Row 12, walk Right to Column 29 Row 12, walk UP Column 29 through the gap to Row 9, and walk Left on Row 9 all the way to Cerulean City!