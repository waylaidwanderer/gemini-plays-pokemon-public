# Scratchpad: Victory Road Route & Puzzle States
- Turn 107083: Standing at (28, 0) on Map 0_198 (Victory Road 3F East)

## Goal
Exit Victory Road to Route 23 North!

## Physical Verification of Exit Location:
- **Test 1 (Turn 107010)**: Stepped on (27, 1) and (27, 0) on 2F East. No exit warp triggered. This falsified the assumption that (27, 1) on 2F East is the exit warp tile.
- **Test 2 (Turn 107045)**: Bumped when trying to step Down from (28, 5) to (28, 6) on 2F East. (28, 6) is a solid wall.
- **Test 3 (Turn 107069)**: Stepped on (27, 1) and (27, 0) on 3F East (Map 0_198). No exit warp triggered either! This means neither (27, 1) nor (27, 0) on 3F East is the exit warp.

## New Hypothesis & Verification Plan:
- The northern pocket of 2F East (Rows 0-5) is a completely closed dead-end pocket.
- The actual exit of Victory Road is in the *southern pocket* of 2F East (Row 7 and below, on Column 29).
- To reach the southern pocket of 2F East, we must take the ladder at (26, 8) on 3F East DOWN to 2F East (which lands at (27, 7) on 2F East).
- From (27, 7) on 2F East, we walk Right to Column 29 and Down to exit!

## Step-by-Step Path on 3F East:
1. Walk from (28, 0) to (26, 8) on 3F East:
   - Down 3 to (28, 3)
   - Left 1 to (27, 3)
   - Down 5 to (27, 8)
   - Left 1 to (26, 8) (this is the ladder!)
2. Take the ladder DOWN to 2F East at (27, 7).
3. From (27, 7) on 2F East, walk Right to Column 29 and Down to exit.