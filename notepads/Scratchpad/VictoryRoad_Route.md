# Scratchpad: Victory Road Route & Puzzle States
- Turn 107076: Standing at (27, 0) on Map 0_198 (Victory Road 3F East)

## Goal
Exit Victory Road to Route 23 North!

## Physical Verification of Exit Location:
- **Test 1 (Turn 107010)**: Stepped on (27, 1) and (27, 0) on 2F East. No exit warp triggered. This falsified the assumption that (27, 1) on 2F East is the exit warp tile.
- **Test 2 (Turn 107045)**: Bumped when trying to step Down from (28, 5) to (28, 6) on 2F East. (28, 6) is a solid wall.
- **Test 3 (Turn 107069)**: Stepped on (27, 1) and (27, 0) on 3F East (Map 0_198). No exit warp triggered either! This means neither (27, 1) nor (27, 0) on 3F East is the exit warp.

## New Hypothesis & Verification Plan:
The exit of Victory Road MUST be in the northeast corner of 2F East, but we must have the warp located at either (28, 5) or some other Column 28 coordinate, or we need to look closer.
Wait, let's look at (28, 0) on 3F East. Walking onto (28, 0) on 3F East warps us to (28, 1) on 2F East.
Let's warp down to 2F East, and systematically test Column 28 and Column 27 on 2F East to find the exit warp.
- To do this:
  1. Walk Right from (27, 0) on 3F East to (28, 0). This triggers the warp to (28, 1) on 2F East.
  2. From (28, 1) on 2F East, walk Left to (27, 1), Up to (27, 0), then Down to (27, 1) to test if direction of entry matters for (27, 1).
  3. If that fails, test (28, 5) by walking Down Column 28 and testing if (28, 5) is indeed an exit warp from a different angle or if there's any other exit.