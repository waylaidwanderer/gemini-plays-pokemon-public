# Safari Zone West Exploration - Run 38 Planning & Execution (Turn 65654+)
- **Current Status**: Standing at (20, 7) in Safari Zone East (Map 0_217) on Turn 65725. Remaining steps: 404 (Run 38 active).
- **Inventory Status**: 15/20 items.

## Run 38 Core Hypothesis & Testing Plan (Warden's Gold Teeth & HM03 Surf)
- **The Core Hypothesis**: Column 14 Row 12 and Row 13 on the plateau level (z=1) contain an unblocked, passable West-facing jump-down ledge. Socratic Answer Turn 65204 proved that all prior records of bumps on these rows were hallucinated, and they have never actually been tested on foot.
- **Strategic Impact**: If Row 12 or Row 13 is a valid jump-left ledge, we can jump West to land on ground level Column 13 (z=0) in the Northwest quadrant. From Column 13, we have direct flat ground-level access to both the Warden's Gold Teeth at (19, 7) and Secret House at (3, 3). This completely bypasses the Southwest isolated pocket, allowing us to easily retrieve both items in under 191 steps (leaving a huge 309-step surplus safety margin!).
- **Testing Protocol**:
  1. Start a fresh Safari game (Run 38) and navigate to (21, 16) [z=1] on the Eastern Plateau.
  2. Walk Left 5 steps along Row 16 to (16, 16) [z=1].
  3. Walk Up 4 steps along Column 16 to stand at (16, 12) [z=1].
  4. Walk Left 1 step to stand at (15, 12) [z=1].
  5. Press `Left` to test walking onto (14, 12).
     - If we successfully jump West, we land on ground level at (13, 12) [z=0], proving Row 12 is a valid jump-down ledge!
  6. If we bump, walk Down 1 step along Column 15 to stand at (15, 13) [z=1].
  7. Press `Left` to test walking onto (14, 13).
     - If we successfully jump West, we land on ground level at (13, 13) [z=0], proving Row 13 is a valid jump-down ledge!

## Run 38 Step-by-Step Backtracking Exit Math (If Bumps Occur)
- If both Row 12 and Row 13 are solid, the Western plateau is a dead end. We will immediately backtrack to the western descent stairs at (6, 19), descend to (6, 20) [z=0], and use DIG to exit, preserving our steps.

## Run 38 Gatehouse Entrance Route (Fuchsia City Map 0_7)
- Stand at (19, 28) [outside Pokémon Center].
- Walk Left 1 step to (18, 28), and Up 8 steps to (18, 20) [9 steps].
- Face the first cuttable bush at (18, 19) and use CUT.
- Walk Up 8 steps along Column 18 to (18, 12).
- Walk Left 2 steps to (16, 12).
- Walk Up 1 step to face the second cuttable bush at (16, 11) and use CUT.
- Walk Up 5 steps along Column 16 to (16, 6) [north of Gym tree blockages].
- Walk Right 2 steps to (18, 6), and Up 3 steps to (18, 3) to enter the Safari Gatehouse.

## Run 38 Chronological Movement Log:
- Turn 65529: Arrived outside Fuchsia Pokémon Center at (19, 28) via GEMMY's DIG field move. All party members at 100% full health. Preparing to route to the Safari Zone Gatehouse to begin Run 38.
- Turn 65534: Attempted to walk Up from (18, 28) and bumped against the Pokémon Center wall, remaining at (18, 28).
- Turn 65542: Walked Right 4 steps to (22, 28), Up 2 steps to (22, 26), and Right 1 step to jump East over the ledge at (23, 26), landing at (24, 26) on Turn 65543.
- Turn 65543 - 65554: Standing at (24, 26) verifying navigation route and preparing to walk to (18, 20).
- Turn 65558: Walked Up 6 steps to Row 20 at (24, 20) and Left 6 steps to Column 18 at (18, 20).
- Turn 65559: Pressed Up to face the first cuttable bush at (18, 19).
- Turn 65568 - 65571: Opened menu, went to POKéMON, selected PETAL, and used CUT to chop down the first bush at (18, 19).
- Turn 65574: Walked Up 8 steps along Column 18 to stand at (18, 12).
- Turn 65575: Walked Left 2 steps along Row 12 to (16, 12) and pressed Up to face the second cuttable bush at (16, 11) on Turn 65576.
- Turn 65594: Walked Up 6 steps, Right 2 steps, and Up 3 steps to enter the Safari Zone Gatehouse (Map 0_156), landing at (3, 5) on Turn 65595.
- Turn 65606: Walked Up 2 steps to (3, 3) on Turn 65607.
- Turn 65607: Walked Up 1 step to (3, 2) to trigger check-in dialogue on Turn 65608.
- Turn 65601: Advanced dialogue.
- Turn 65603: Selected YES to join the hunt, paid ¥500, and entered Safari Zone Center (Map 0_220) at (15, 25) on Turn 65604 (500 steps remaining).
- Turn 65604: Ran 'safari_navigator_agent' to synchronize coordinates (Map transition consumes 1 step, leaving 499 remaining).
- Turn 65607: Executed 'safari_pathfinder' which generated an invalid right-first path through solid gatehouse structures. Walked Up 9 steps along Column 15 to stand at (15, 16) on Turn 65608 (9 steps used, 490 remaining).
- Turn 65627: Walked Right 5 steps and Up 2 steps along Column 20 through the fence gap at (20, 15) to stand at (20, 14) on Turn 65628 (7 steps used, 483 remaining).
- Turn 65629: Walked Right 4 steps along Row 14 to stand at (24, 14) and triggered a wild battle against Nidoran♀ on Turn 65630 (4 steps used, 479 remaining).
- Turn 65630: Selected RUN and successfully escaped from the wild Nidoran♀ on Turn 65631 (0 steps used, 479 remaining).
- Turn 65633: Ran 'safari_navigator_agent' to synchronize coordinates and steps (479 remaining).
- Turn 65636: Walked Up 3 steps along Column 24 to Row 11, and Right 5 steps directly along Row 11 to stand at (29, 11) on Turn 65637 (8 steps used, 471 remaining).
- Turn 65637: Ran 'safari_navigator_agent' to synchronize coordinates and steps (471 remaining).
- Turn 65639: Pressed Right 1 step to transition East to Safari Zone East, landing at (0, 23) on Turn 65641 (1 step used, 470 remaining).
- Turn 65641: Standing at (0, 23) in Safari Zone East syncing coordinates and preparing to route to the Southern Plateau stairs at (20, 21).
- Turn 65652: Walked Left 1, Down 3, and Right 6 steps to stand at (10, 24) on Turn 65653 (10 steps used, 459 remaining).
- Turn 65653: Ran 'safari_navigator_agent' to synchronize steps and coordinates.
- Turn 65655: Walked Right 10 steps along Row 24 to stand at (20, 24) on Turn 65656 (10 steps used, 449 remaining).
- Turn 65656: Ran 'safari_navigator_agent' to synchronize steps and coordinates.
- Turn 65657: Standing at (20, 24) facing UP directly at the wooden stairs at (20, 21). Ready to walk Up 3 steps to climb onto the Southern Plateau at (20, 20).
- Turn 65657 - 65665: Walked Up 3 steps to stand on stairs at (20, 21) [z=1/0], Up 1 step to (20, 20) [z=1], Left 8 steps along Row 20 to (12, 20) [z=1], and Down 1 step to western stairs at (12, 21) [z=1] on Turn 65665 (23 actual steps used, 436 remaining).
- Turn 65666 - 65674: Ran 'safari_navigator_agent' to synchronize coordinates and steps. Standing at (12, 21) on the western plateau stairs.
- Turn 65675: Walked Down 1 step to descend western plateau stairs onto ground level at (12, 22) [z=0], and Left 3 steps along Row 22 to stand at (9, 22) [z=0] on Turn 65675 (4 actual steps used, 432 remaining). Ran 'safari_navigator_agent' to synchronize coordinates and steps.
- Turn 65676 - 65677: Walked Up 7 steps along Column 9 to (9, 15) [z=0] and stepped Up 1 step onto (9, 14) on Turn 65677 (8 actual steps used, 424 remaining), triggering a wild battle against Level 24 Nidoran♀.
- Turn 65681: Walked Up 4 steps along Column 9 to (9, 10) [z=0] on Turn 65682 (4 actual steps used, 420 remaining). Ran 'safari_navigator_agent' to synchronize coordinates and steps on Turn 65683.
- Turn 65687: Walked Right 1 to (10, 10) [z=0], Up 2 to (10, 8) [z=0], Right 2 to (12, 8) [z=0], and Up 1 onto the northern stairs at (12, 7) [z=1/0] on Turn 65688 (6 actual steps used, 414 remaining). Ran 'safari_navigator_agent' on Turn 65690.
- Turn 65691 - 65694: Standing at (12, 7) [z=1] preparing to cross the Northern Plateau East.
- Turn 65694: Walked Up 1 to stand fully on the plateau at (12, 6) [z=1], Right 5 to (17, 6) [z=1], and Down 1 onto the eastern stairs at (17, 7) [z=1] on Turn 65695 (7 actual steps used, 409 remaining). Ran 'safari_navigator_agent' to synchronize coordinates and steps. Pressed 'Right' and bumped against (18, 7), remaining at (17, 7).
- Turn 65701: Walked Down 1 step to descend eastern plateau stairs onto ground level at (17, 8) [z=0] on Turn 65702 (1 actual step used, 408 remaining). Ran 'safari_navigator_agent' to synchronize coordinates and steps on Turn 65707.
- Turn 65702 - 65707: Standing at (17, 8) [z=0] preparing to navigate the eastern bypass detour corridor.
- Turn 65723: Walked Right 3 steps along Row 8 to (20, 8) [z=0], and Up 1 step along Column 20 to stand at (20, 7) [z=0] on Turn 65724 (4 actual steps used, 404 remaining). Ran 'safari_navigator_agent' to synchronize coordinates and steps on Turn 65725.