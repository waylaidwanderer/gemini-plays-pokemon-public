# Vermilion Gym Trash Can Lock Puzzle Strategy

## Puzzle Mechanics:
- There are 15 trash cans inside the Vermilion Gym.
- A lock blocks the path to Lt. Surge.
- To open the lock:
  1. We must search the trash cans to find the 1st switch.
  2. Once the 1st switch is found, the 2nd switch is ALWAYS located in a trash can directly adjacent (North, South, East, or West) to the 1st switch.
  3. If we search any non-adjacent can, or an adjacent can that does not contain the 2nd switch, the lock resets and we must find the 1st switch again!
  4. Once both switches are found in succession, the laser gate opens, allowing us to battle Lt. Surge.

## Grid Coordinates of Trash Cans (X, Y) in Vermilion Gym (Map 0_92):
- Columns of trash cans are located at X=1, X=3, X=5, X=7, X=9. There are 3 rows: Y=7, Y=9, and Y=11.
- Total 15 trash cans:
  - Row Y=7: (1, 7), (3, 7), (5, 7), (7, 7), (9, 7) (To be fully verified as we go north)
  - Row Y=9: (1, 9), (3, 9), (5, 9), (7, 9), (9, 9)
  - Row Y=11: (1, 11), (3, 11), (5, 11), (7, 11), (9, 11)
- Distance (d) between adjacent trash cans is indeed 2 tiles (e.g. from Y=11 to Y=9 is d=2, from X=1 to X=3 is d=2).
- Let X_1, Y_1 be the coordinates of the 1st switch.
- Offset Formula: The 2nd switch will be at X_2, Y_2 cardinally adjacent:
  - North: (X_1, Y_1 - 2)
  - South: (X_1, Y_1 + 2)
  - East:  (X_1 + 2, Y_1)
  - West:  (X_1 - 2, Y_1)

## Randomizer Hypothesis & Testing Protocol (Turn 18348):
- **Hypothesis**: The trash can lock puzzle is controlled by the map script (a hardcoded event script for Map 0_92), NOT by overworld item tables. Since standard hidden items are scrambled/empty in this randomized ROM, but map-specific scripts are intact, the Gym puzzle mechanics will remain identical to vanilla. Specifically, the second switch will still be cardinally adjacent to the first switch.
- **Empirical Proof Test**:
  - Upon finding the 1st switch at (X, Y), we will systematically check ONLY the cardinally adjacent trash cans first.
  - If we find the 2nd switch, our hypothesis is proven.
  - If we check all cardinally adjacent trash cans and the lock resets every time without revealing a 2nd switch, the randomizer has scrambled this mechanic, and we must perform a wider serpentine search.

## Systematic Serpentine Search Pattern (15 Trash Cans):
We will search the 15 trash cans in the following exact serpentine sequence to systematically find the 1st switch with zero redundant turns. Once the 1st switch is found, we will systematically test only its cardinally adjacent trash cans (using the offset formula) to locate the 2nd switch:
1. (1, 11) - Bottom-Left
2. (3, 11)
3. (5, 11)
4. (7, 11)
5. (9, 11) - Bottom-Right
6. (9, 9)  - Middle-Right
7. (7, 9)
8. (5, 9)
9. (3, 9)
10. (1, 9) - Middle-Left
11. (1, 7) - Top-Left
12. (3, 7)
13. (5, 7)
14. (7, 7)
15. (9, 7) - Top-Right

## Empirical Trial Log (Starting Turn 18493):
- **Adjacency Adherence**: We will check cardinally adjacent cans first. If a lock resets, we will resume searching the serpentine list from the *next* unchecked can to ensure no wasted trials.
- **Log Format**:
  - `Trial [N] (Turn [Start] - [End])`:
    - 1st Switch Search: [Can Coordinates] -> [Result (Found / Empty)]
    - 2nd Switch Search: [Can Coordinates] -> [Result (Unlocked / Reset / Not Applicable)]
    - Notes: [Any observations]

## Live Puzzle Run (Starting Turn 18580):
- **Starting Turn**: 18580
- **Start Time**: Wednesday, May 27, 2026 at 10:06 AM PDT
- **Status**: Commencing systematic serpentine search to locate the 1st switch. Team is fully healed.

### Trial 1 (Turn 18580 - 18624):
- 1st Switch: Found at (7, 9) on Turn 18621!
- 2nd Switch Candidates (Cardinally Adjacent):
  - West: (5, 9)
  - North: (7, 7)
  - East: (9, 9)
  - South: (7, 11)
- Adjacent Checks Strategy:
  - Checked West at (5, 9) on Turn 18624 -> Result: Empty ("Nope! There's only trash here.").
  - **Outcome**: Lock completely reset! Trial 1 failed.

### Trial 2 (Turn 18624 - 18668):
- 1st Switch: Found at (9, 7) on Turn 18664!
- 2nd Switch Candidates (Cardinally Adjacent):
  - West: (7, 7)
  - South: (9, 9)
- Adjacent Checks:
  - Checked West at (7, 7) on Turn 18668 -> Result: Empty ("Nope! There's only trash here.").
- Outcome: Lock completely reset! Trial 2 failed.
- **Mathematical Deduction**: Since (7, 7) was empty, the 2nd switch for a 1st switch at (9, 7) MUST be at (9, 9).

### Trial 3 (Turn 18668 - 18688):
- 1st Switch: Found at (9, 11) on Turn 18684!
- 2nd Switch Candidates (Cardinally Adjacent):
  - West: (7, 11)
  - North: (9, 9)
- Adjacent Checks:
  - Checked West at (7, 11) on Turn 18688 -> Result: Empty ("Nope! There's only trash here.").
- Outcome: Lock completely reset! Trial 3 failed.
- **Mathematical Deduction**: Since (7, 11) was empty, the 2nd switch for a 1st switch at (9, 11) MUST be at (9, 9).

## Validated 1st/2nd Switch Database (Proven by Elimination):
- If 1st Switch is at **(9, 7)** -> 2nd Switch is definitively at **(9, 9)** (Verified via Trial 2 elimination).
- If 1st Switch is at **(9, 11)** -> 2nd Switch is definitively at **(9, 9)** (Verified via Trial 3 elimination).
- If 1st Switch is at **(7, 9)** -> 2nd Switch is NOT at **(5, 9)** (Verified via Trial 1 check). (Remaining candidates: (7, 7), (9, 9), (7, 11)).

### Trial 4 (Turn 18688):
- Serpentine Search Index: 3 (Can at (5, 11))
- Status: Checked (1, 11) on Turn 18696 (Empty) and (3, 11) on Turn 18699 (Empty). Moving to Index 3 (Can at (5, 11)).
  - Stand at (4, 11) facing RIGHT to check (5, 11).