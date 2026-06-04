# Safari Zone West Exploration Scratchpad (Run 20 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Current Turn**: Turn 53603.
- **Currently standing at**: (9, 13) on Map 0_217 (Safari Zone East).
- **Steps Taken in Run 20**: 86 overworld steps (measured as 32 steps in Center and 54 steps in East).
- **Steps Remaining**: 414 steps remaining.

## Answers to Socratic Questions (Turn 53381)
### Socratic Question 1: Tracking Drift & Turn-by-Turn Verification
- **Why tracking drift occurred**: We failed to recognize that transitions between maps and other non-movement overworld events (like wild battles and escape mechanics) take steps, and we were not performing a strict step budget synchronization with the overwatch system.
- **Verification routine**: For Run 20, we will check our coordinate changes after every movement chunk, verify our step count on every single turn, and update our scratchpad with the exact step budget to stay 100% in sync.

### Socratic Question 2: Circular Backtracking Loops
- **Why we backtracked**: We fell into a confirmation bias trap where we assumed we could horizontally walk onto the checkered plateau ramp of Column 17 from Column 16 on Row 9, ignoring our verified notes from Turn 52789 that checkered slopes are horizontal barriers. When that failed, we walked all the way back around to test Column 24 again, which was also already proven solid.
- **The Lesson**: Always consult verified permanent notepads before repeating any movement that resulted in a bump or block in previous runs, and do not repeat tests of already proven solid barriers.

### Socratic Question 3: Fresh Run 20 Strategy & Step-Budget Allocation
- **Why DIG was critical**: With only 17 steps remaining, reaching either item on foot was mathematically impossible. DIG instantly teleported us outside Fuchsia Pokémon Center with 0 step cost, allowing us to restart the Safari Zone.
- **Double-Retrieval Route for Run 20 (500 steps fresh)**:
  1. **Safari Zone Center (29 steps)**: Enter at (15, 25) -> Walk to (29, 10). Path: Up x9, Right x6, Up x2, Right x1, Up x4, Right x7.
  2. **Safari Zone East (29 steps)**: Enter at (0, 22) -> Walk to (0, 5). Path: Up x1, Right x6, Up x16, Left x6.
  3. **Safari Zone North (50 steps)**: Enter at (39, 31) -> Walk to (9, 35). Path: Walk Left along Row 31/33 to climb the western plateau at (22, 23), traverse West, descend at (16, 27) to ground, bypass lake to (9, 35). (Approx 50 steps).
  4. **Safari Zone West (162 steps)**:
     - Enter at (27, 0) -> Walk Down 20 to (27, 20) -> Left 6, Up 3 to stairs UP at (21, 17) [30 steps].
     - Climb stairs to (21, 16) [1 step].
     - Traverse plateau West to (6, 19) [approx 18 steps].
     - Descend stairs to ground level at (6, 20) [1 step].
     - Walk from southwest ground level to northwest: Walk Left 3 to Column 3, Walk Up 6 along Column 3 to (3, 14), Walk Right 7 to (10, 14), Walk Up along Column 10 to (10, 12), Walk Right to Column 18, Walk Up to Row 5, Walk Left to (3, 5), Walk Up to Secret House at (3, 3) [approx 62 steps].
     - Enter Secret House, get HM03 Surf, exit [2 steps].
     - Walk from Secret House (3, 3) to Gold Teeth (19, 7): Walk Down 2 to (3, 5), Walk Right 15 along Row 5 to (18, 5), Walk Down 3 to (18, 8), Walk Right 1 to (19, 8) facing Up, press A [21 steps].
     - **Cumulative Steps**: 29 + 29 + 50 + 30 + 1 + 18 + 1 + 62 + 2 + 21 = 243 steps total!
     - This leaves over 250 steps of safety margin, guaranteeing we can easily complete both on foot in Run 20!

### Socratic Question 4: Chronological Logs & Burden of Proof
- We successfully tested Column 24 on Rows 9-13 on foot and verified they are all blocked. To preserve this, we are documenting it permanently in "Locations/SafariZone_West" and keeping our scratchpad clean.

## Run 20 Chronological Overworld Logs
- Turn 53381: Standing at (19, 28) in Fuchsia City outside Pokémon Center. We must walk to the Safari Zone Gatehouse.
- Turn 53381: Standing at (19, 28) outside Pokémon Center. Starting Run 20 with fresh 500-step budget.
- Turn 53386: Walked Down 2, Right 5 steps to reach (25, 30) to bypass the Pokémon Center and fence.
- Turn 53388: Walked Left 1, Up 10 steps to reach (24, 20).
- Turn 53389: Walked Left 6 steps to reach (18, 20) (directly below the first cuttable bush).
- Turn 53402: Currently standing at (18, 20) in Fuchsia City, preparing to CUT the bush at (18, 19).
- Turn 53408: Successfully CUT the first bush at (18, 19). Row 19 is now clear!
- Turn 53418: Walked Down 1 from (18, 11) to (18, 12), walked Left 2 to (16, 12), and turned North to face the second bush at (16, 11).
- Turn 53422: Successfully CUT the second bush at (16, 11). Row 11 is now clear!

## Step-by-Step Path from (16, 12) to Safari Zone Gatehouse (18, 3)
- We are standing at (16, 12) facing North in Fuchsia City.
- Walk Up 9 steps along Column 16 to (16, 3).
- Walk Right 2 steps to (18, 3) to enter the Safari Zone Gatehouse.
- Total steps: 11 steps.
- Start turn for Safari budget tracking: Turn 53422 (currently on Map 0_7). Fresh budget of 500 steps starts upon entering Safari Zone Center (Map 0_220).
- Turn 53425: Walked Up 6 along Column 16 to (16, 6) (bumped into fence at 16, 5), then walked Right 2 steps to (18, 6). Currently standing at (18, 6) in Fuchsia City. We are in line with the Gatehouse door.
- Turn 53444: Successfully walked past the gatekeeper and signpost to (15, 22).
- Turn 53448: Walked Up 6, Right 6 to (21, 16) in Safari Zone Center. No encounters. Steps taken: 17. Steps remaining: 483.
- Turn 53452: Walked from (21, 16) in Safari Center to (29, 10), then transitioned to Safari Zone East at (0, 22). No encounters. Steps taken: 29. Steps remaining: 454.
- Turn 53455: Walked from (0, 22) in Safari Zone East to (5, 21). No encounters. Steps taken: 6. Steps remaining: 448.
- Turn 53463: Walked from (5, 21) to (16, 24). No encounters. Steps taken: 14. Steps remaining: 434.
- Turn 53469: Walked from (16, 24) to (20, 24). No encounters. Steps taken: 4. Steps remaining: 430.
- Turn 53472: Walked from (20, 24) to (20, 21), then climbed wooden stairs to (20, 20) on the plateau. No encounters. Steps taken: 4. Steps remaining: 426.
- Turn 53492: Synced steps remaining to 438 to align with overwatch step budget tracking (accounting for actual overworld steps and map boundary transitions).
- Turn 53514: Currently standing at (20, 20) on the plateau, preparing to walk West to (12, 21).
- Turn 53546: Walked Down 1 step from (12, 21) to (12, 22) on the ground level. No encounters. Steps taken: 1. Steps remaining: 428.
- Turn 53561: Walked Up 4 steps from (9, 22) to (9, 18) on the ground level. No encounters. Steps taken: 4. Steps remaining: 421.