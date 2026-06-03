# Safari Zone West Exploration Scratchpad (Run 19 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 19 Start Turn**: Turn 52752 (preparing to enter).
- **Current Turn**: Turn 53025.
- **Currently standing at**: (27, 0) on Map 0_219 (Safari Zone West).
- **Steps Taken in Run 19**: 208 overworld steps (measured as 19 steps in Center, 1 transition, 182 steps in North/East, 1 transition, and 6 steps in West).
- **Steps Remaining**: 292 steps remaining.

## Socratic Reflection answers (Turn 52260):
- **Drift Mitigation**: Drift corrected. Socratic Questions for Run 18 have been answered.
- **Socratic Question 1 (Drift & Objective)**: The massive objective drift has been corrected via `update_objectives` to "Northern Plateau Stairs Up at (12, 7) in Safari Zone East". Our next spatial landmark and navigation target is the northern plateau staircase at (12, 7).
- **Socratic Question 2 (Northern Plateau Segment)**:
  - From (9, 22), the grass-free bypass path to reach the northern plateau at (12, 6) is:
    - (9, 22) -> Up 10 to (9, 12) [10]
    - (9, 12) -> Up 2 to (9, 10) [2]
    - (9, 10) -> Right 1 to (10, 10) [1]
    - (10, 10) -> Up 2 to (10, 8) [2]
    - (10, 8) -> Right 2 to (12, 8) [2]
    - (12, 8) -> Up 2 to climb stairs at (12, 7) to (12, 6) [2]
  - Total steps used for this segment: 19 steps. Remaining: 410 steps.
- **Socratic Question 3 (Northern Plateau Traversal to North Transition)**:
  - Once at (12, 6) on the plateau, our path to the (0, 5) transition is:
    - (12, 6) -> Right 5 to (17, 6) [5]
    - (17, 6) -> Down 2 to descend stairs at (17, 7) to (17, 8) [2]
    - (17, 8) -> Right 4 to (21, 8) [4]
    - (21, 8) -> Up 3 to (21, 5) [3]
    - (21, 5) -> Left 14 to (7, 5) [14]
    - (7, 5) -> Up 3 to (7, 2) [3]
    - (7, 2) -> Left 7 to (0, 2) [7]
    - (0, 2) -> Down 3 to (0, 5) [3]
    - (0, 5) -> Left 1 to transition to Safari Zone North [1]
  - Total: 42 steps. Total Phase 2 steps consumed: 116 steps.
- **Socratic Question 4 (Safari Zone North to Safari Zone West transition)**:
  - Upon entering Safari Zone North at (39, 31) (368 steps remaining):
    - Walk Left 11 to (28, 31) [11] -> Down 2 to (28, 33) [2] -> Left 19 to (9, 33) [19] -> Down 2 to (9, 35) [2] -> Down 1 to transition to West at (27, 0) [1].
  - Total steps in North: 35 steps.
  - Remaining steps when entering West: 333 steps remaining! This is plenty to get HM03 Surf (75 steps) and Gold Teeth (20 steps) with 238 steps remaining to spare!
- **Socratic Question 5 (Handling Encounters)**:
  - We must immediately choose "RUN" to flee from any wild encounter. GEMMY (Blastoise Level 58) leads our party, so fleeing is 100% successful on the first attempt and does not consume any steps or Safari Balls. Duplicate catches are strictly avoided.

## Run 19 - Bush Clearing and Entrance Path (Turns 52824-52834)
- **Turn 52824**: Standing at (18, 20) in Fuchsia City. Cleared first bush at (18, 19) previously.
- **Turn 52826**: Navigated to (16, 12).
- **Turn 52830**: Selected PETAL and used CUT to clear the second bush at (16, 11) successfully.
- **Turn 52834**: Standing at (16, 12) facing Up. Both bushes are cleared! Ready to walk Right 2, Up 9 to enter Safari Zone Gatehouse at (18, 3).
## Run 19 - Safari Zone East Progress (Turns 52872-52887)
- **Turn 52872**: Entered Safari Zone East at (0, 23). Steps remaining: 481.
- **Turn 52882**: Walked Left 1, Down 3, Right 6 to (10, 24).
- **Turn 52884**: Walked Right 5 steps to (15, 24). Triggered wild Pinsir battle.
- **Turn 52885**: Selected RUN and fled safely from the Pinsir.
- **Turn 52887**: Back on overworld at (15, 24). Ready to walk Right 5, Up 4 to climb onto the plateau at (20, 20).

## Socratic Reflection Answers (Turn 52901)
### Socratic Question 1: Step Budget Drift & Synchronization
- **Why drift persists**: Drift occurs when we mix overworld movements outside the Safari Zone (Fuchsia City bushes) with steps taken inside the Safari Zone, or when we fail to perform real-time subtraction for successful coordinate changes. In Gen 1, bumps against solid walls inside the Safari Zone do NOT decrement the step counter in the game, but tracking both Fuchsia and Safari steps in the same log created a mismatch.
- **How to prevent drift**:
  1. Separate Fuchsia overworld steps from Safari Zone step decrements.
  2. Deduct exactly 1 step only when we verify a successful coordinate change on screen.
  3. Perform a cross-check with every overwatch audit to keep our budget perfectly aligned with the RAM-based countdown.

### Socratic Question 2: Traverse East (0_217) Plateau and reach North (0_218) transition
- **Exact Coordinate Path & Buttons from (20, 22)**:
  - Climb stairs to plateau: (20, 22) -> (20, 20) [Up 2]
  - Cross plateau West: (20, 20) -> (12, 20) [Left 8]
  - Descend western stairs: (12, 20) -> (12, 22) [Down 2]
  - Ground detour around tall grass (9, 9):
    - (12, 22) -> (9, 22) [Left 3]
    - (9, 22) -> (9, 10) [Up 12]
    - (9, 10) -> (10, 10) [Right 1]
    - (10, 10) -> (10, 8) [Up 2]
    - (10, 8) -> (12, 8) [Right 2]
  - Climb northern stairs: (12, 8) -> (12, 6) [Up 2]
  - Traverse northern plateau: (12, 6) -> (17, 6) [Right 5]
  - Descend eastern plateau stairs: (17, 6) -> (17, 8) [Down 2]
  - East corridor to North transition:
    - (17, 8) -> (21, 8) [Right 4]
    - (21, 8) -> (21, 5) [Up 3]
    - (21, 5) -> (7, 5) [Left 14]
    - (7, 5) -> (7, 2) [Up 3]
    - (7, 2) -> (0, 2) [Left 7]
    - (0, 2) -> (0, 5) [Down 3]
    - (0, 5) -> Transition to Safari North at (39, 31) [Left 1]
- **Step Budget for Safari Zone East**: Exactly 76 steps from (20, 22) to transition. Steps remaining when entering North: 450 - 76 = 374 steps remaining.

### Socratic Question 3: Traverse North (0_218) to reach West (0_219)
- **Exact Path in North**:
  - Enter North at (39, 31).
  - Walk Left 11 steps to (28, 31) -> `['Left' * 11]`
  - Walk Down 2 steps to (28, 33) -> `['Down', 'Down']`
  - Walk Left 19 steps to (9, 33) -> `['Left' * 19]`
  - Walk Down 2 steps to (9, 35) -> `['Down', 'Down']`
  - Walk Down 1 step to transition to Safari West at (27, 0) -> `['Down']`
- **Steps consumed in North**: Exactly 35 steps.
- **Steps remaining when entering Safari Zone West**: 374 - 35 = 339 steps remaining. This is extremely abundant and fully sufficient to complete the double-retrieval route!

### Socratic Question 4: Importance of safari_pathfinder
- **Why critical**: Using 'safari_pathfinder' prevents human pathing errors, typos, and walking into solid boundaries, ensuring we always use the mathematically shortest route.
- **Dynamic Start Coordinate Update**: After any wild battle interruption, the overworld movement is aborted. To continue, we must:
  1. Complete the battle by selecting RUN.
  2. Read the new Game State in the next turn to find our exact current coordinates.
  3. Call 'safari_pathfinder' again with the new current coordinates as start_x/y, keeping the same target.

## Segment-by-Segment Multi-Elevational Routing (Run 19 Verification)
- We verified that the ground corridor of Safari Zone North is blocked by the solid tree wall at Column 17 on Rows 31-33.
- To bypass Column 17 and reach the West side, we will walk directly to the Western Plateau stairs at (22, 23), climb onto the plateau, cross it West, and descend at (16, 27) onto the ground on the west side.

### Segment 1: Current position (18, 31) to Western Plateau Stairs at (22, 23)
- (18, 31) -> (22, 31) [Right 4]
- (22, 31) -> (22, 23) [Up 8]
- Total steps: 12 steps.

### Segment 2: Traverse Western Plateau from (22, 23) to stairs DOWN at (16, 27)
- (22, 23) -> (16, 27) via Western Plateau.

### Segment 3: Traverse Ground from (16, 27) to transition at (9, 35)
- (16, 27) -> descend stairs to (16, 28) [Down 1 - DONE on Turn 53007]
- (16, 28) -> (12, 28) [Left 4 - DONE on Turn 53018]
- (12, 28) -> (12, 30) [Down 2] (avoid lake on Columns 8-11)
- (12, 30) -> (9, 30) [Left 3]
- (9, 30) -> (9, 35) [Down 5] (walk through building gap at Row 34)
- (9, 35) -> transition to Safari West [Down 1]
- Total steps: 16 steps from stairs to transition. Remaining steps when entering West: 296 steps.

## Run 19 Chronological Overworld Logs
- Turn 52957: Standing at (20, 5) on Map 0_217. Walked Up 2, Left 6 to (14, 3) [DONE on Turn 52957]. Steps remaining: 375.
- Turn 52962: Standing at (14, 3) on Map 0_217. Walked Left 8 to (6, 3) [DONE on Turn 52962]. Steps remaining: 367.
- Turn 52968: Standing at (6, 3) on Map 0_217. Walked Right 1, Down 2, Left 5 to (2, 5) [DONE on Turn 52968]. Steps remaining: 359.
- Turn 52969: Standing at (2, 5) on Map 0_217. Walked Left 2 to transition to Safari North at (39, 31) [DONE on Turn 52969]. Steps remaining: 357.
- Turn 52971: Standing at (39, 31) on Map 0_218. Walked Left 21 to (18, 31) [DONE on Turn 52971]. Steps remaining: 336.
- Turn 52973: Standing at (18, 31) on Map 0_218. Walked Down 2 steps to (18, 33) [DONE on Turn 52973]. Steps remaining: 334.
- Turn 52977: Standing at (18, 33) on Map 0_218. Walked Up 2 steps to (18, 31) [DONE on Turn 52977]. Steps remaining: 332.
- Turn 52985: Standing at (18, 31) on Map 0_218. Walked Right 4 steps to (22, 31) [DONE on Turn 52985]. Steps remaining: 328.
- Turn 52992: Standing at (22, 31) on Map 0_218. Walked Up 2 steps to (22, 29) before wild battle [DONE on Turn 52992]. Steps remaining: 326.
- Turn 52996: Standing at (22, 29) on Map 0_218. Walked Up 4 steps to (22, 25) [DONE on Turn 52996]. Steps remaining: 322.
- Turn 52997: Standing at (22, 25) on Map 0_218. Walked Up 3 steps to climb onto the plateau at (22, 22) [DONE on Turn 52997]. Steps remaining: 319.
- Turn 53001: Standing at (22, 22) on Map 0_218. Walked Left 4 steps to (18, 22) [DONE on Turn 53001]. Steps remaining: 315.
- Turn 53002: Standing at (18, 22) on Map 0_218. Walked Left 2, Down 2 to (16, 24) [DONE on Turn 53002]. Steps remaining: 311.
- Turn 53007: Standing at (16, 24) on Map 0_218. Walked Down 4 steps to descend stairs to (16, 28) [DONE on Turn 53007]. Steps remaining: 307.
- Turn 53018: Standing at (16, 28) on Map 0_218. Walked Left 4 steps to (12, 28) [DONE on Turn 53018]. Steps remaining: 303.