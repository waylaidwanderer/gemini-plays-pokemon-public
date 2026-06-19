# Scratchpad: Victory Road Route & Puzzle States
- Turn 107037: Standing at (27, 0) on Map 0_194 (Victory Road 2F East)

## Goal
Exit Victory Road via 2F East to Route 23 North!

## Physical Verification of Exit Location:
- **Test 1 (Turn 107010)**: Stepped on (27, 1) and (27, 0). No exit warp triggered. This falsifies the previous assumption that (27, 1) is the exit warp tile.
- **Test 2 (Turn 107006)**: Stepped on (28, 1). No warp triggered. This confirms (28, 1) is not an exit warp, but rather the landing tile of the ladder from 3F.
- **New Hypothesis**: The exit warp is located at the bottom of the Column 28 corridor (Row 5 or 6). To exit, we must walk onto Column 28 and head South (Down) as far as possible.

## Exit Plan:
1. Walk Right to (28, 0).
2. Walk Down along Column 28 (Y = 1, 2, 3, 4, 5...) to trigger the exit warp.