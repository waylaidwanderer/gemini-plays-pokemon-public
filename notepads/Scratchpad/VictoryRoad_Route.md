# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (26, 5) on Victory Road 3F East (Map 0_198)

## Analysis of 3F East Path to Exit
- **Observed Constraints on 3F East (Map 0_198)**:
  - Row 6 is completely impassable on the Right Channel (Columns 24-29) due to solid rock walls (TYPE_2889) at (26, 6), (27, 6), (28, 6), blocking vertical movement to the (26, 8) ladder.
  - Column 24 is a solid vertical rock wall on Rows 4-8, separating the Left and Right channels south of Row 3.
  - Row 9 is completely blocked on Columns 22, 23, and 24 by solid rock walls (TYPE_2889) at (22, 9), (23, 9), and (24, 9).
  - Therefore, the northern area (Rows 0-8 of Left Channel, Rows 0-5 of Right Channel) is completely cut off on foot from the southern area (Row 10+).
- **The True Descent Pathway**:
  - Since the Right Channel's Row 6 blocks access to (26, 8) on 3F East from the north, we must take the **(23, 7) ladder** DOWN instead.
  - The ladder at (23, 7) on 3F East is on the Left Channel, which is accessible from (26, 5) via the Row 2 crossover.
  - Symmetrically, the (23, 7) ladder DOWN to 2F East lands at (23, 7) on 2F East.
  - On 2F East, (23, 7) and (27, 7) both reside within the northern ground pocket (Columns 19-27, Rows 7-11) and connect directly to the exit at (28, 1). Thus, taking the (23, 7) ladder DOWN is the correct, unblocked way to reach the exit on 2F East.

## Path from (26, 5) to (23, 7) Ladder:
1. Stand at (26, 5). Walk Right to (27, 5) [1 step]
2. Walk Up 3 steps along Column 27 to Row 2 at (27, 2) [3 steps]
3. Walk Left 4 steps along Row 2 to Column 23 at (23, 2) [4 steps]
4. Walk Down 5 steps along Column 23 to reach the (23, 7) ladder [5 steps]
5. Interact with the ladder to descend to 2F East.