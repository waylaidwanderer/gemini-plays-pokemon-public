# Safari Zone West Exploration - Run 38 Planning & Execution (Turn 65641+)
- **Current Status**: Standing at (0, 23) in Safari Zone East (Map 0_217) on Turn 65641. Remaining steps: 470 (Run 38 active).
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
- Turn 65596: Walked Up 2 steps to (3, 3) on Turn 65597.
- Turn 65597: Walked Up 1 step to (3, 2) to trigger check-in dialogue on Turn 65598.
- Turn 65601: Advanced dialogue.
- Turn 65603: Selected YES to join the hunt, paid ¥500, and entered Safari Zone Center (Map 0_220) at (15, 25) on Turn 65604 (500 steps remaining).
- Turn 65604: Ran 'safari_navigator_agent' to synchronize coordinates (Map transition consumes 1 step, leaving 499 remaining).
- Turn 65607: Executed 'safari_pathfinder' which generated an invalid right-first path through solid gatehouse structures. Walked Up 9 steps along Column 15 to stand at (15, 16) on Turn 65608 (9 steps used, 490 remaining).
- Turn 65608 - 65619: Standing at (15, 16) in Safari Zone Center syncing coordinates and preparing to route around the central partition fence.