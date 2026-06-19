# Scratchpad: Victory Road Route & Puzzle States
- Turn 106921: Standing at (23, 7) on Map 0_198 (Victory Road 3F East)
- Real-World Timestamp: Friday, June 19, 2026 at 10:25 AM PDT

## Goal
Exit Victory Road via 3F East to Route 23 North!

## Correct Routing to Victory Road Exit (Bypassing Column 24 wall via Row 10):
1. Currently at (23, 7) on 3F East (Map 0_198).
2. Walk Down 3 steps to (23, 10).
3. Walk Right 2 steps to (25, 10), bypassing the Column 24 vertical wall through the open Row 10 gap (since Boulder C2 was successfully pushed to (22, 10)).
4. Walk Up 2 steps to (25, 8).
5. Walk Right 1 step to the ladder at (26, 8).
6. Take the ladder at (26, 8) DOWN to 2F East (lands at (27, 7) on 2F East).
7. On 2F East, walk north to the exit at (28, 1) to transition to Route 23 North.
8. This route is fully open, safe, and avoids all remaining boulder puzzles on 2F/3F.

## Verification of Alternate Paths (Falsified):
- Tried to exit from (28, 1) / (28, 0) on 2F East. Result: Solid collision bumps (bumps at (28, 0) on Turn 106859 and Turn 106863), confirming no exit warp exists on 2F East.
- Confirmed that Row 8 is blocked on 3F East at Column 24 by a solid rock wall (verified on Turn 105244).
- Re-verified that the ladder at (27, 7) on 2F East goes UP to 3F East. Since the final cave exit doorway to Route 23 North is located on 3F East, climbing this ladder is the mandatory path to exit the cave!

## League Preparation Protocol:
- Once we successfully emerge onto Route 23 North and enter the Indigo Plateau Pokémon Center, we must immediately:
  1. Call the custom agent `league_readiness_coordinator` to conduct a comprehensive final audit of our party levels, movesets, item inventories, and remaining PP counts before challenging the Elite Four.
  2. Create and load a new permanent regional notepad named `Locations/IndigoPlateau_PointsOfInterest` to systematically catalog the final exit transitions, Poké Mart inventories, and Pokémon Center coordinates to prevent context loss.