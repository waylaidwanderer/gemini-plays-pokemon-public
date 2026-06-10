# 3F West-East Southern Balcony Crossover Passability Tests
- **Objective**: Systematically test and document whether the southern balcony on Rows 16 and 17 provides a continuous, walkable horizontal crossover that connects 3F West to 3F East on foot.

## Test Log (Started Turn 77524)
- *TBD*
- **Turn 77569**: Systematic visual check of Rows 16 and 17 on 3F West confirms that Columns 6 to 10 are completely blocked by solid wall/rubble of TYPE_2889. Row 17 on Columns 1 to 10 is also blocked by solid wall/rubble or railing of TYPE_2889. This mathematically disproves the southern balcony crossover hypothesis. There is no walkable horizontal connection between 3F West and 3F East under State B.
- **Routing Decision**: We must backtrack down to 1F East under State B. We will check if the staircase at (25, 14) on 1F East (which we previously documented as a normal floor tile with no stairs) actually warps us up to the isolated 2F Southeast room, which contains the stairs up to 3F East.

## Socratic Question Response & Test Protocol (Turn 77665)
- **The Visual Check Danger**: Visually checking (25, 14) from across closed Gate 1 on Turn 76295 was a massive pitfall. In Gen 1, warp tiles can look identical to normal floor tiles, meaning visual observation is NOT proof of absence.
- **The Burden of Proof Principle**: Only physical foot-testing (standing on the exact tile and verifying if a map transition occurs) satisfies the Burden of Proof.
- **Physical Foot-Test Protocol for (25, 14)**:
  1. Walk to (26, 3) via Row 3.
  2. Walk South down Column 26 to Row 13: (26, 3) -> (26, 13).
  3. Walk Left to (25, 13) (Gate 1, open under State B).
  4. Walk Down 1 step onto (25, 14).
  5. Observe:
     - **Result A**: If we warp to 2F East South at (25, 14), then the staircase is bidirectionally active and verified. We will immediately update `Locations/CinnabarMansion` to reflect this.
     - **Result B**: If we stand on (25, 14) on 1F and nothing happens, we will attempt to interact facing in all directions. If still nothing, then (25, 14) is indeed a one-way warp from 2F or not a warp at all, proving the hypothesis false.
- **Turns 77748-77749**: Bypassed the wandering Burglar NPC using Row 10, then successfully walked down Column 4 to Row 15, and stepped Right to (5, 15).
- **Turns 77752-77753**: Stood at (5, 15) and pressed Down to reach (5, 16) (passable floor TYPE_3fe2). From (5, 16), pressed Down again and collided/bumped against (5, 17) (solid balcony railing TYPE_2889). Visually confirmed that Columns 1 to 5 on Row 17 are solid black/white railings of TYPE_2889, and Columns 6 to 10 on Row 16 and 17 are solid rubble of TYPE_2889.
- **Definitive Conclusion**: The southern balcony crossover hypothesis is mathematically and physically DISPROVEN. There is no horizontal walkthrough or drop-down crossover between 3F West and 3F East on Rows 16 and 17. The southwest quadrant is completely dead-ended.
- **Turn 78113-78114 State A Gate 2 physical test**:
  - Stand at (8, 9) facing Up. Press Up.
  - Result: Collision, stayed at (8, 9).
  - Conclusion: Gate 2 on 3F at (8, 8)-(11, 8) is CLOSED/impassable under State A as well.
  - **Turn 78144-78145 Row 7/6/5 physical and visual verification under State A**:
  - Stood at (7, 8). Directly above us at (7, 7) is TYPE_2889 (solid wall/rubble).
  - Visually confirmed on the screen that Rows 6 and 7 are blocked by TYPE_2889 rubble from Column 3 all the way to Column 9.
- **No Remaining Hypotheses**: All possible physical on-foot crossover paths on 3F between West and East have been systematically tested and are confirmed 100% blocked under both State A and State B. There is no walkthrough connection on 3F.

## 3F Row 8 Gate (Gate 2) Test under State B (Turn 79282)
- **Hypothesis**: Under State B, the horizontal gate on Row 8 at (8, 8)-(11, 8) is CLOSED and impassable.
- **Methodology**: Walk Up from (9, 11) to (9, 9), then attempt to step Up onto (9, 8) to see if we bump.
- **Turn 79282 Test**: Walked Up 3 times from (9, 11) to test (9, 8).
- **Turn 79310 State A Gate 2 Test Preparation**: Backtracked to 2F West at (2, 12) facing Up to toggle Statue 2 back to State A. After toggling, we will climb the stairs at (7, 10) back to 3F, stand at (9, 9) facing Up, and attempt to walk Up onto (9, 8) to see if Gate 2 is open under State A.
- **Turn 79330 State A Gate 2 Test**: Walked Up from (9, 9) and bumped against (9, 8) on Turn 79330. This physically proves that Gate 2 is CLOSED under State A. Since it was also verified CLOSED under State B, 3F West has no on-foot crossover to 3F East under any state.
- **New Path Plan (Column 22 State B Corridor Test)**: We are backtracking to 2F West to toggle Statue 2 back to State B. Then we will walk to 2F East South and test the passability of Column 22 under State B to see if it opens access to the isolated Southeast room (and thus the stairs up to 3F East).

## 2F East Column 22 State B Passability Test Protocol
- **Objective**: Systematically test the passability of Column 22 on Rows 9-15 under State B on 2F East to find an open gate/passage.
- **Route to Test Zone**:
  1. Warp back up to 2F West at (5, 10).
  2. Walk Up Column 5 to Row 4: (5, 10) -> (5, 4) [6 steps].
  3. Walk Right through Gate 6 (open under State B) to (14, 4): (5, 4) -> (14, 4) [9 steps].
  4. Walk Down 2 steps to Row 6: (14, 4) -> (14, 6) [2 steps] (to bypass the Column 15 solid wall on Rows 1-5).
  5. Walk Right through Column 15 to Column 21 on Row 6: (14, 6) -> (21, 6) [7 steps].
  6. Walk Down Column 21 to the test starting position at (21, 9): (21, 6) -> (21, 9) [3 steps].
- **Systematic Test Protocol for Column 22**:
  - For each Row Y from 9 to 15:
    1. Stand at (21, Y) facing Right.
    2. Press Right.
    3. If we step onto (22, Y), Column 22 is OPEN on Row Y under State B! We will immediately document this open gate, walk into the Southeast room (Columns 23-28), and climb the stairs at (25, 14) up to 3F East.
    4. If we bump, Column 22 is CLOSED on Row Y under State B. We will log the bump (including Turn number), walk Down to (21, Y+1), and repeat.
- **Turn 79398 Systematic Test Row 9**: From (21, 9) facing Right, pressed Right against (22, 9) (`TYPE_2889`). Result was a BUMP, physically proving Column 22 is CLOSED/solid on Row 9 under State B.
- **Turn 79404 Systematic Test Row 10**: From (21, 10) facing Right, pressed Right against (22, 10) (`TYPE_2889`). Result was a BUMP, physically proving Column 22 is CLOSED/solid on Row 10 under State B.
- **Turn 79410 Systematic Test Row 11**: From (21, 11) facing Right, pressed Right against (22, 11) (`TYPE_2889`). Result was a BUMP, physically proving Column 22 is CLOSED/solid on Row 11 under State B.
- **Turn 79416 Systematic Test Row 12**: From (21, 12) facing Right, pressed Right against (22, 12) (`TYPE_2889`). Result was a BUMP, physically proving Column 22 is CLOSED/solid on Row 12 under State B.
- **Turn 79429 Systematic Test Row 13**: From (21, 13) facing Right, pressed Right against (22, 13) (`TYPE_3fe2`). Result was a BUMP, physically proving Column 22 is CLOSED/solid on Row 13 under State B, despite its grid label being `TYPE_3fe2`. This confirms the tile overlay type can be misleading because it represents underlying terrain rather than dynamic blockage sprites or state-dependent collision data.
- **Turn 79438 Systematic Test Row 14**: From (21, 14) facing Right, pressed Right against (22, 14) (`TYPE_2889`). Result was a BUMP, physically proving Column 22 is CLOSED/solid on Row 14 under State B.