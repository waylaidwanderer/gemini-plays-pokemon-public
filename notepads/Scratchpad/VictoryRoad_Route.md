# Scratchpad: Victory Road Route & Puzzle States
- Turn 106892: Standing at (27, 3) on Map 0_194 (Victory Road 2F East)
- Real-World Timestamp: Friday, June 19, 2026 at 10:20 AM PDT

## Goal
Exit Victory Road via 3F East to Route 23 North!

## Correct Routing to Victory Road Exit:
1. Currently in the northeastern pocket of 2F East.
2. Collect the item at (27, 5) by standing at (27, 4) and pressing 'A'. This clears the vertical path down Column 27.
3. Walk Down Column 27 to the ladder at (27, 7).
4. Take the ladder at (27, 7) UP to 3F East (lands at (26, 8) on 3F East).
5. On 3F East, walk to the cave exit located in the northeast corner of 3F East to transition to Route 23 North.
6. This route is fully open and avoids all remaining boulder puzzles on 2F/3F.

## Verification of Alternate Paths (Falsified):
- Tried to exit from (28, 1) / (28, 0) on 2F East. Result: Solid collision bumps (bumps at (28, 0) on Turn 106859 and Turn 106863), confirming no exit warp exists on 2F East.
- Confirmed that the northeastern corner of 2F East (Rows 7-9, Columns 25-28) is a closed pocket separated from the southern Row 11 ground level by the solid wall at Row 10.
- Re-verified that the ladder at (27, 7) on 2F East goes UP to 3F East. Since the final cave exit doorway to Route 23 North is located on 3F East, climbing this ladder is the mandatory path to exit the cave!

## League Preparation Protocol:
- Once we successfully emerge onto Route 23 North and enter the Indigo Plateau Pokémon Center, we must immediately:
  1. Call the custom agent `league_readiness_coordinator` to conduct a comprehensive final audit of our party levels, movesets, item inventories, and remaining PP counts before challenging the Elite Four.
  2. Create and load a new permanent regional notepad named `Locations/IndigoPlateau_PointsOfInterest` to systematically catalog the final exit transitions, Poké Mart inventories, and Pokémon Center coordinates to prevent context loss.