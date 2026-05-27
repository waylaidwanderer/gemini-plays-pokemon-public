# Vermilion Gym Trash Can Lock Puzzle Strategy

## Puzzle Mechanics:
- There are 15 trash cans inside the Vermilion Gym.
- A lock blocks the path to Lt. Surge.
- To open the lock:
  1. We must search the trash cans to find the 1st switch.
  2. Once the 1st switch is found, the 2nd switch is ALWAYS located in a trash can directly adjacent (North, South, East, or West) to the 1st switch.
  3. If we search any non-adjacent can, or an adjacent can that does not contain the 2nd switch, the lock resets and we must find the 1st switch again!
  4. Once both switches are found in succession, the laser gate opens, allowing us to battle Lt. Surge.
- CRITICAL ACTIVE-STATE PUZZLE RULE:
  - Checking a trash can *before* the 1st switch is found does NOT disqualify it from being the 2nd switch.
  - This is because the 2nd switch's active state is ONLY generated *at the moment the 1st switch is toggled*.
  - Any prior empty checks are completely irrelevant to the 2nd switch's state. Always check all valid adjacent cans after finding the 1st switch, regardless of whether you checked them earlier in the same trial.

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
We will search the 15 trash cans in the following exact serpentine sequence to systematically find the 1st switch with zero redundant turns. Once the 1st switch is found, we will systematically test only its cardinally adjacent trash cans (using the offset formula) to locate the 2nd switch.

### Serpentine Restart/Resume Protocol:
- **CRITICAL RULE**: Every time the electric lock resets (i.e., when a 2nd switch check fails), the game's script selects a **COMPLETELY NEW, RE-RANDOMIZED** 1st switch location from all 15 cans.
- **Therefore**: We **MUST** restart the serpentine search at **Index 1 (1, 11)** at the beginning of every new Trial.
- **Why Resuming is a Flaw**: Resuming the serpentine search from where we left off (e.g., starting Trial 2 at Index 10 instead of Index 1) is mathematically incorrect because the new 1st switch could have spawned at any of the previously checked cans (Indices 1-7). Skipping them means we are ignoring valid spawn locations for the new active layout.
- **Status**: We are strictly restarting at Index 1 for Trial 3, Trial 4, and all future trials.

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
  - **Mathematical Deduction**: Since West (5, 9) was empty, if the 1st switch is found at (7, 9) again, the remaining valid 2nd switch candidates are: East (9, 9), North (7, 7), South (7, 11).

### Trial 2 (Turn 18624 - 18668):
- 1st Switch: Found at (9, 7) on Turn 18664!
- 2nd Switch Candidates (Cardinally Adjacent):
  - West: (7, 7)
  - South: (9, 9)
- Adjacent Checks:
  - Checked West at (7, 7) on Turn 18668 -> Result: Empty ("Nope! There's only trash here.").
- Outcome: Lock completely reset! Trial 2 failed.
- **Mathematical Deduction**: Since West (7, 7) was empty, if the 1st switch is found at (9, 7) again, the remaining valid 2nd switch candidate is: South (9, 9).

### Trial 3 (Turn 18668 - 18688):
- 1st Switch: Found at (9, 11) on Turn 18684!
- 2nd Switch Candidates (Cardinally Adjacent):
  - West: (7, 11)
  - North: (9, 9)
- Adjacent Checks:
  - Checked West at (7, 11) on Turn 18688 -> Result: Empty ("Nope! There's only trash here.").
- Outcome: Lock completely reset! Trial 3 failed.
- **Mathematical Deduction**: Since West (7, 11) was empty, if the 1st switch is found at (9, 11) again, the remaining valid 2nd switch candidate is: North (9, 9).

## The Lt. Surge Gym Puzzle Out-of-Bounds Bug (Proven Turn 18759):
- **Glitch Mechanic**: In Gen 1, when the 1st switch is found, the game randomly selects a cardinal direction (North, South, East, West) for the 2nd switch. If the selected direction points out of bounds of the 3x5 trash can grid (e.g. North or East of (9, 7)), the 2nd switch is placed out of bounds and cannot be reached.
- **Flawed Elimination Assumption**: Due to this glitch, if we check one adjacent can and it is empty, the other adjacent can is **NOT** guaranteed to be the 2nd switch (as the 2nd switch could have glitched out of bounds).
- **Corrected Strategy**: If the 1st switch is on a corner/edge, we must systematically check *both* valid adjacent cans. If both are empty, it was an out-of-bounds glitched layout.
- **Corner Probability Proof & Optimal Policy (Turn 19059)**:
  - Corner cans (such as (9, 7)) have only 2 valid adjacent neighbors. Since directions are selected with equal (25%) probability:
    - 50% probability the 2nd switch glitches out of bounds (unreachable).
    - 50% probability the 2nd switch is in one of the 2 valid adjacent cans.
  - Policy: Since finding the 1st switch is costly (~20-30 turns), but checking adjacent cans is cheap (1-2 turns), we should ALWAYS check both valid adjacent cans. Only if BOTH are empty do we exit the Gym to reset.

### Trial 4 (Turn 18688 - 18759):
- 1st Switch: Found at (9, 7) on Turn 18754!
- 2nd Switch Candidates (Cardinally Adjacent):
  - West: (7, 7)
  - South: (9, 9)
- Adjacent Checks:
  - Checked South at (9, 9) on Turn 18758 -> Result: Empty ("Nope! There's only trash here. The electric locks were reset!").
- Outcome: Lock completely reset! Trial 4 failed. (Confirmed the out-of-bounds bug: either the 2nd switch was at (7, 7) or it glitched out of bounds).
- **Mathematical Deduction**: Since South (9, 9) was empty, if the 1st switch is found at (9, 7) again, the remaining valid 2nd switch candidate is: West (7, 7).

### Trial 5 (Turn 18759 - 18773):
- 1st Switch: Found at (3, 11) on Turn 18768! (Deducted because checking (5, 11) on Turn 18773 triggered the lock reset message).
- 2nd Switch Candidates (Cardinally Adjacent to (3, 11)):
  - West: (1, 11)
  - East: (5, 11)
  - North: (3, 9)
- Adjacent Checks:
  - Checked East at (5, 11) on Turn 18773 -> Result: Empty ("Nope! There's only trash here. Hey! The electric locks were reset!").
- Outcome: Lock completely reset! Trial 5 failed.
- **Mathematical Deduction**: Since East (5, 11) was empty, if the 1st switch is found at (3, 11) again, the remaining valid 2nd switch candidates are: West (1, 11), North (3, 9).

### Trial 6 (Turn 18774 - 18781):
- Serpentine Search Index: 1 (Can at (1, 11))
- Status: Found 1st switch at (1, 11) on Turn 18777!
- 2nd Switch Candidates (Cardinally Adjacent to (1, 11)):
  - East: (3, 11)
  - North: (1, 9)
- Adjacent Checks:
  - Checked East at (3, 11) on Turn 18779 -> Result: Empty ("Nope! There's only trash here. Hey! The electric locks were reset!").
- Outcome: Lock completely reset! Trial 6 failed.
- **Mathematical Deduction**: Since East (3, 11) was empty, if the 1st switch is found at (1, 11) again, the remaining valid 2nd switch candidate is: North (1, 9).

### Trial 7 (Turn 18782 - 18830):
- Serpentine Search Index: 13 (Can at (5, 7))
- Status: Found 1st switch at (5, 7) on Turn 18827!
- 2nd Switch Candidates (Cardinally Adjacent to (5, 7)):
  - West: (3, 7)
  - East: (7, 7)
  - South: (5, 9)
- Adjacent Checks:
  - Checked West at (3, 7) on Turn 18829 -> Result: Empty ("Nope! There's only trash here. Hey! The electric locks were reset!").
- Outcome: Lock completely reset! Trial 7 failed.
- **Mathematical Deduction**: Since West (3, 7) was empty, if the 1st switch is found at (5, 7) again, the remaining valid 2nd switch candidates are: East (7, 7), South (5, 9).

### Trial 8 (Turn 18831 - 18890):
- Serpentine Search Index: 15 (Can at (9, 7))
- Status: Found 1st switch at (9, 7) on Turn 18887!
- 2nd Switch Candidates (Cardinally Adjacent to (9, 7)):
  - West: (7, 7)
  - South: (9, 9)
- Adjacent Checks:
  - Checked West at (7, 7) on Turn 18890 -> Result: Empty ("Nope! There's only trash here. Hey! The electric locks were reset!").
- Outcome: Lock completely reset! Trial 8 failed.
- **Mathematical Deduction**: Since West (7, 7) was empty, if the 1st switch is found at (9, 7) again, the remaining valid 2nd switch candidate is: South (9, 9).

### Trial 9 (Turn 18891 - Turn 18925):
- Serpentine Search Index: 4 (Can at (7, 11))
- Status: Failed (locks reset).
  - Checked (1, 11) on Turn 18894 (Empty).
  - Checked (3, 11) on Turn 18898 (Empty).
  - Checked (5, 11) on Turn 18903 (Empty).
  - Checked (7, 11) on Turn 18912 (Empty).
  - Checked (9, 11) on Turn 18917 (Empty).
  - Checked (9, 9) on Turn 18921 (Empty).
  - Found 1st switch at (7, 9) on Turn 18923!
  - Checked adjacent East (9, 9) on Turn 18925 (Empty, locks reset).
- Mathematical Deduction for (7, 9):
  - Since East (9, 9) was empty, if the 1st switch is found at (7, 9) in any future trial, the remaining valid 2nd switch candidates are: West (5, 9), North (7, 7), South (7, 11).

### Trial 10 (Turn 18926 - Present):
- Serpentine Search Index: 15 (Can at (9, 7))
- Status: 1st switch found!
  - Checked (1, 11) on Turn 18934 (Empty).
  - Checked (3, 11) on Turn 18940 (Empty).
  - Checked (5, 11) on Turn 18944 (Empty).
  - Checked (7, 11) on Turn 18947 (Empty).
  - Checked (9, 11) on Turn 18952 (Empty).
  - Checked (9, 9) on Turn 18957 (Empty).
  - Checked (7, 9) on Turn 18964 (Empty).
  - Checked (5, 9) on Turn 18968 (Empty).
  - Checked (3, 9) on Turn 18972 (Empty).
  - Checked (1, 9) on Turn 18975 (Empty).
  - Checked (1, 7) on Turn 18981 (Empty).
  - Checked (3, 7) on Turn 18985 (Empty).
  - Checked (5, 7) on Turn 18988 (Empty).
  - Checked (7, 7) on Turn 18994 (Empty).
  - Found 1st switch at (9, 7) on Turn 18998!
  - Checked adjacent West (7, 7) on Turn 19003 (Empty, lock reset).

### Trial 11 (Turn 19004 - Turn 19014):
- Serpentine Search Index: 1 (Can at (1, 11))
- Status: Failed (locks reset).
  - Found 1st switch at (1, 11) on Turn 19009!
  - Checked adjacent East (3, 11) on Turn 19013 (Empty, locks reset).
- Mathematical Deduction for (1, 11):
  - Since East (3, 11) was empty, if the 1st switch is found at (1, 11) in any future trial, the remaining valid 2nd switch candidate is: North (1, 9).

### Trial 12 (Turn 19015 - Turn 19037):
- Serpentine Search Index: 3 (Can at (5, 11))
- Status: Failed (locks reset).
  - Checked (1, 11) on Turn 19023 (Empty).
  - Checked (3, 11) on Turn 19028 (Empty).
  - Found 1st switch at (5, 11) on Turn 19031! (Proven by Turn 19037 reset message).
  - Checked adjacent East (7, 11) on Turn 19037 (Empty, locks reset).
- Mathematical Deduction for (5, 11):
  - Since East (7, 11) was empty, if the 1st switch is found at (5, 11) in any future trial, the remaining valid 2nd switch candidates are: West (3, 11), North (5, 9).

### Trial 13 (Turn 19038 - Turn 19069):
- Serpentine Search Index: 5 (Can at (9, 11))
- Status: Failed (locks reset).
  - Checked (1, 11) on Turn 19044 (Empty).
  - Checked (3, 11) on Turn 19048 (Empty).
  - Checked (5, 11) on Turn 19056 (Empty).
  - Checked (7, 11) on Turn 19062 (Empty).
  - Found 1st switch at (9, 11) on Turn 19066!
  - Checked adjacent West (7, 11) on Turn 19068 (Empty, locks reset).
- Mathematical Deduction for (9, 11):
  - Since West (7, 11) was empty, if the 1st switch is found at (9, 11) in any future trial, the remaining valid 2nd switch candidate is: North (9, 9).

### Trial 14 (Turn 19070 - Turn 19151):
- Serpentine Search Index: 15 (Can at (9, 7))
- Status: Failed (locks reset).
  - Checked (1, 11) on Turn 19075 (Empty).
  - Checked (3, 11) on Turn 19077 (Empty).
  - Checked (5, 11) on Turn 19086 (Empty).
  - Checked (7, 11) on Turn 19090 (Empty).
  - Checked (9, 11) on Turn 19094 (Empty).
  - Checked (9, 9) on Turn 19099 (Empty).
  - Checked (7, 9) on Turn 19102 (Empty).
  - Checked (5, 9) on Turn 19106 (Empty).
  - Checked (3, 9) on Turn 19111 (Empty).
  - Checked (1, 9) on Turn 19119 (Empty).
  - Checked (1, 7) on Turn 19123 (Empty).
  - Checked (3, 7) on Turn 19127 (Empty).
  - Checked (5, 7) on Turn 19132 (Empty).
  - Checked (7, 7) on Turn 19141 (Empty).
  - Found 1st switch at (9, 7) on Turn 19147!
  - Checked adjacent West (7, 7) on Turn 19151 (Empty, locks reset).
- Mathematical Deduction for (9, 7):
  - Since West (7, 7) was empty, if the 1st switch is found at (9, 7) in any future trial, the remaining valid 2nd switch candidate is: South (9, 9).

  - Trial 15 (Turn 19151 - Turn 19220): Failed. Checked (1, 11) on Turn 19164 (Empty), (3, 11) on Turn 19169 (Empty), (5, 11) on Turn 19182 (Empty), (7, 11) on Turn 19189 (Empty), (9, 11) on Turn 19194 (Empty), (9, 9) on Turn 19208 (Empty). Found 1st Switch at (7, 9) on Turn 19215! Checked adjacent South (7, 11) on Turn 19220 (Empty, locks reset).
  - Mathematical Deduction for (7, 9): Since West (5, 9) (Trial 1), East (9, 9) (Trial 9), and South (7, 11) (Trial 15) were empty, if the 1st switch is found at (7, 9) in any future trial, the 2nd switch is 100% GUARANTEED to be at North (7, 7)!!!

  - Trial 16 (Turn 19221 - Present): Serpentine search in progress.
  - Checked (1, 11) on Turn 19227 (Empty).
  - Checked (3, 11) on Turn 19238 (Empty).
  - Checked (5, 11) on Turn 19247 (Empty).
  - Checked (7, 11) on Turn 19256 (Empty).
  - Checked (9, 11) on Turn 19267 (Empty).
  - Checked (9, 9) on Turn 19276 (Empty).
  - Checked (7, 9) on Turn 19286 (Empty).
  - Next target: (5, 9).
  - Movement plan: Close textbox with B. Walk Left to (6, 10), Left to (5, 10). Stand at (5, 10) facing Up to check (5, 9).

## Contingency Plan: No Switch Found (Turn 18721)
- **Problem**: If we search all 15 cans in our serpentine sequence and the 1st switch is still not found:
- **Potential Variables**:
  1. *Interaction/Pathing Error*: We might have pressed 'A' without properly facing a can or when we were blocked, causing a "no-op" that skipped checking.
  2. *Coordinate Typo*: One or more coordinates in our list might be off by a tile.
  3. *Accidental Reset*: An accidental interaction with a non-adjacent can after finding the first switch could have silently reset the state without us realizing.
- **Empirical Testing Protocol**:
  1. We will verify every trash can coordinate against the on-screen magenta coordinates to ensure absolute precision.
  2. If the entire grid is empty, we will exit the Gym entirely (which guarantees a full map/script reset) and restart the serpentine search from Index 1 with extreme step-by-step validation.

## Socratic Verification & Mechanics Alignment (Turn 19294):
- **Overworld Turning and Movement Mechanics Proof**:
  - In Gen 1, pressing a direction that you are not currently facing automatically turns you and takes a step forward in a single motion (unless physically blocked). There is no "turn-in-place" penalty.
  - Thus, when moving from (7, 10) facing DOWN to (5, 10), pressing 'Left' immediately turns us Left and steps to (6, 10) on Step 1, and 'Left' again steps to (5, 10) on Step 2. Total is exactly 2 movement presses: `['Left', 'Left']`.
- **First-Switch/Second-Switch Active State Proof**:
  - Under the Critical Active-State Puzzle Rule: empty checks made *before* finding the 1st switch are completely irrelevant.
  - If we find the first switch at (5, 9), even though we already checked (3, 9), (7, 9), and (5, 11) and found them empty earlier in Trial 16, their prior empty status does **NOT** disqualify them from being the active second switch.
  - The second switch's active state is *only* generated at the moment the first switch is toggled. Therefore, we must systematically test all cardinally adjacent candidates—including prior empty checks—after finding the first switch.