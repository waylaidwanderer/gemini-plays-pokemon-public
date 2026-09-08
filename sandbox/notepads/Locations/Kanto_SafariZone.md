# Safari Zone - Kanto

## Safari Zone Rules & Mechanics
- Admission: ¥500 for 30 Safari Balls and 500 overworld steps.
- Step Counter: Only movement in the overworld consumes steps. Wild battles, menus, and turning in place do NOT consume steps.
- When steps expire, PA chime rings and player is automatically warped to the gatehouse.
- Key Objectives:
  - Secret House in Area 3: Obtain HM03 (Surf).
  - Area 3 Item: Retrieve Gold Teeth for the Fuchsia Warden (rewards HM04 Strength).
  - Rest Houses: Located in each area for shelter/hints.

## Center Area
- Row 9 Bush Collision at (22, 9): Tested Turn 7767; solid impassable collision.
- Map Size: 30x30.
- South Exit: Gatehouse to Fuchsia City at (14..15, 25). Player spawns at (15, 24).
- Rest House 1: Located at cols 16..19 rows 18..19, door at (17, 19).
- Central Pond: Cols 17..20 rows 10..13. Shoreline at col 21.
- East Exit (to Area 1): Open corridor at rows 10..11 cols 28..30. Tree wall blocks col 29 rows 12..19.
- Route Progression: Clockwise traversal (Center Area -> Area 1 -> Area 2 -> Area 3).

## Area 1 (East)
- West Exit: Center Area at (0, 22..23). Player enters at (0, 23). (Tile 0, 24 is impassable collision verified Turn 7761).
- Signpost: Located at (5, 23) ("CENTER AREA / NORTH: AREA 2").
- Geography: Row 23 hedge extends along cols 8..16, opens to lawn at cols 17..18, and resumes at cols 19..21+. Row 24 corridor has lawn (cols 0..13) then tall grass (cols 14..21+). Southern boundary has hedge (cols 0..13) and stumps (cols 14..21+).
- Rock Plateau: Located north of row 22 with south-facing staircases at (12, 21) and (20, 21). Eastern cliff edge ends at col 23.
- Eastern Bypass: Eastern corridor spans cols 24..28, bounded by col 29 tree wall. Clear lawn at rows 16..19 across cols 24..28 leads north to a wooden staircase at (24, 15).
- Northern Plateau Staircase: At (24, 15), a south-facing wooden staircase ascends to the northern plateau (row 14+ across cols 20..26). Cliff face (cols 25..27) and trees (cols 28..29) block the ground path.
## Area 1 Features & Landmarks
- Row 6 Bush Collision at (4, 6): Tested Turn 7698; solid impassable collision.
- Row 6 Bush Cut Test at (6, 6): Tested Turn 7720 with Farfetch'd (DUX); returned 'There isn't anything to CUT!'.
- Signpost at (26, 10): 'REST HOUSE' [Read Turn 7733].
- Rest House 2 Eastern Boundary: Columns 27..28 lawn dead-ends at row 4..5 tree line.
- Plateau North Cliff Edge at (17, 4): Impassable solid cliff edge verified Turn 7728; rock plateau cannot be exited northward directly onto row 3 lawn.
- Signpost: Located at (6, 4) in northern corridor.
- Plateau Western Cliff Corner at (10, 4): Impassable solid cliff edge verified Turn 7702; rock plateau cannot be exited westward directly onto row 4 lawn.
- Item Ball: Located at (3, 7) on western lawn - MAX POTION [Collected Turn 7695].
- Northern Lawn: Extends along rows 10..11 cols 20..25.
- Item Ball: Located at (21, 10) on the northern lawn - FULL RESTORE [Collected Turn 7647].
- Rest House 2: Located at cols 24..26 rows 8..9 with entrance door at (25, 9) and signpost at (26, 10).
- Water Pond: Located west of the plateau along cols 16..19 rows 11..17.
- Empirical Verification (Turn 7540): Row 12 is an impassable cliff face to the north; cannot walk off plateau onto northern lawn (rows 10-11). Plateau acts as an elevated bridge between south stairs at (20, 21) and east stairs at (24, 15). Walkable ridge is along cols 21-22. Empirical Collision (Turn 7570): Columns 0..5 north of row 21 are blocked by trees, statues, and bushes; open northern passage in Area 1 lies through cols 7..9.
## Center Area Topological Barriers & Routing (Verified Turns 7600-7609)
- Southern Barrier (Rows 15-16): Continuous barrier of trees (cols 0-1), bush hedge (cols 2-5 on row 16, cols 6-9 on row 15), and wooden fence with statues (cols 10-19 on row 15) blocks northern passage across the entire western and central sectors.
- Pond Underpass Barrier (Row 14): Stone statues at (19, 14) and (16, 14) block westward passage under the pond.
- Area 2 Route: As indicated by official signpost at (5, 23) ('CENTER AREA / NORTH: AREA 2'), route to Area 2 proceeds north through Area 1. Center Area northern passage is blocked by stone statues at row 14.
## Step Budget & Timer (Verified Mechanics)
- Display Format: In-game menu box displays `[STEPS REMAINING] / 500`.
- Empirical Benchmarks:
  - Turn 7671: 223 / 500 remaining.
  - Turn 7716: 183 / 500 remaining (verified via Start menu).
  - Turn 7741: ~139 steps remaining.
  - Turn 7774: Exactly 60 / 500 steps remaining (verified via in-game Start menu display).
