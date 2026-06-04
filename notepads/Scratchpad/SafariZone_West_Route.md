# Safari Zone West Exploration Scratchpad (Run 20 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Current Turn**: Turn 53834.
- **Currently standing at**: (25, 5) on Map 0_219 (Safari Zone West).
- **Steps Taken in Run 20**: 281 overworld steps (measured as 32 steps in Center, 199 steps in East/North, 50 steps in West).
- **Steps Remaining**: 219 steps remaining.

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
- Turn 53585: Walked from (9, 18) to (10, 15) on the ground level. No encounters.
- Turn 53590: Walked from (10, 15) to (10, 14) on the ground level. No encounters.
- Turn 53592: Walked from (10, 14) to (9, 14) on the ground level. No encounters.
- Turn 53601: Walked from (9, 14) to (9, 13) on the ground level. No encounters.
- Turn 53608: Walked from (9, 13) to (10, 10) on the ground level. No encounters.
- Turn 53610: Walked from (10, 10) to (12, 7) on the stairs. No encounters.
- Turn 53615: Climbed onto the plateau, walked east to (17, 6), and descended the stairs to (17, 8). No encounters.
- Turn 53632: Walked from (17, 8) to (20, 7) on the ground level. No encounters.
- Turn 53635: Walked from (20, 7) to (17, 3) on the ground level, crossing exactly one grass tile at (20, 6). No encounters.
- Turn 53645: Walked from (17, 3) to (14, 3) on the ground level, crossing 3 grass tiles. Triggered wild Kangaskhan battle. Kangaskhan ran away.
- Turn 53651: Walked from (14, 3) to (10, 3) on the ground level, crossing 4 grass tiles. Triggered wild Exeggcute battle. (Note: Total steps taken in Run 20: 121 overworld steps, 32 in Center and 89 in East).
- Turn 53656: Walked Left 4 steps from (10, 3) to (6, 3) on the ground level. No encounters.
- Turn 53657: Walked Right 1, Down 2, Left 2 steps from (6, 3) to (5, 5). No encounters.
- Turn 53659: Walked Left 5 steps from (5, 5) to (0, 5). No encounters.
- Turn 53664: Walked Left 1 step from (0, 5) to transition to Safari Zone North (Map 0_218) at (39, 31). No encounters.
- Turn 53673: Walked Left 6 steps from (39, 31) to (33, 31). No encounters.
- Turn 53674: Walked Left 6 steps from (33, 31) to (27, 31). No encounters.
- Turn 53675: Walked Left 5 steps from (27, 31) to (22, 31). Triggered wild Nidoran♀ battle at (22, 31). Escaped.
- Turn 53681: Walked Up 4 steps from (22, 31) to (22, 27). No encounters.
- Turn 53685: Walked Up 5 steps from (22, 27) to (22, 22) on the plateau. No encounters.
- Turn 53689: Walked Left 6 steps from (22, 22) to (16, 22) on the plateau. No encounters. (Note: Total steps taken in Run 20: 169 overworld steps).
- Turn 53692: Walked Down 6 steps from (16, 22) to (16, 28) on the ground level, descending the stairs. No encounters.
- Turn 53695: Walked Left 4 steps from (16, 32) to (12, 32) on clear ground. No encounters. (Note: Total steps taken in Run 20: 179 overworld steps).
- Turn 53697: Walked Left 3 steps to (9, 32), then Down 3 steps to (9, 35) on clear ground. No encounters.
- Turn 53697: Walked Down 1 step from (9, 35) to transition to Safari Zone West (Map 0_219) at (27, 0). No encounters. (Note: Total steps taken in Run 20: 186 overworld steps).
- Turn 53703: Walked Down 10 steps from (27, 0) to (27, 10) on clear ground. No encounters.
- Turn 53706: Walked Down 10 steps from (27, 10) to (27, 20) on clear ground. No encounters.
- Turn 53709: Walked Left 6 steps from (27, 20) to (21, 20) on clear ground. No encounters.
- Turn 53712: Walked Up 4 steps from (21, 20) to (21, 16) on the East Plateau, climbing the stairs. No encounters.
- Turn 53716: Walked Left 4 steps from (21, 16) to (17, 16) on the plateau. No encounters.
- Turn 53720: Walked Left 6 steps from (17, 16) to (11, 16) on the plateau. No encounters.
- Turn 53722: Walked Left 5 steps from (11, 16) to (6, 16) on the plateau. No encounters.
- Turn 53725: Walked Down 4 steps from (6, 16) to (6, 20) on the ground level, descending the stairs. No encounters.
- Turn 53727: Walked Left 2 steps from (6, 20) to (4, 20) in the tall grass. Triggered wild Doduo battle. Escaped. (Note: Total steps taken in Run 20: 237 overworld steps).
- Turn 53742: Walked Right 2 steps to (6, 20) and Up 1 step to (6, 19) to climb the West stairs. No encounters. Steps taken: 3. Steps remaining: 260.
- Turn 53747: Walked Up 3 steps from (6, 19) to (6, 16) onto the plateau surface. No encounters. Steps taken: 3. Steps remaining: 257.
- Turn 53756: Walked Right 5 steps from (6, 16) to (11, 16) along Row 16 of the plateau. No encounters. Steps taken: 5. Steps remaining: 252.

## Socratic Reflection (Turn 53825 - Final Verified Edition)
### Socratic Question 1: Tracking Drift & Turn-by-Turn Verification
- **Why tracking drift occurred**: We relied too heavily on the game state's raw 'Steps Taken' reporting without realizing that map transitions, battle screens, and other non-movement overworld events can introduce a step counting delta from true overworld movement. This led to a cumulative 17-step tracking drift on Turn 53760.
- **Verification routine**: We have defined the 'safari_navigator_agent' to automatically parse our starting and ending coordinates, perform strict Manhattan distance delta calculations, and subtract exact overworld steps. We will run this agent and verify our position and budget turn-by-turn.

### Socratic Question 2: Planned Route to Surf at (3, 3) & Southwest Pocket Isolation
- **Why southwest pocket is isolated**: The southwestern ground level (where Column 6 Row 20 lies) is completely blocked to the North by water (TYPE_4e8c) on Column 9, the Rest House 3 building (TYPE_2889) on Column 10-13, and the plateau cliff walls (TYPE_2889) on Column 14. Therefore, any attempt to reach the northwestern quadrant (Secret House) from the southwest ground level directly is impossible. If we descend the western stairs to (6, 20), we are trapped in a dead end pocket and MUST climb back onto the plateau at (6, 19).
- **Exact Planned Coordinate Path to Surf at (3, 3) from (25, 13)**:
  1. Walk Up 8 steps along Column 25 to Row 5 at (25, 5). [Buttons: 'Up' * 8, Step Cost: 8]
  2. Walk Left 22 steps along Row 5 to Column 3 at (3, 5). [Buttons: 'Left' * 22, Step Cost: 22]
  3. Walk Up 2 steps to (3, 3) and enter the Secret House. [Buttons: 'Up' * 2, Step Cost: 2]
  - **Total Steps from (25, 13) to Surf**: 8 + 22 + 2 = 32 steps.
  - **Remaining Steps inside Secret House**: 227 - 32 = 195 steps remaining.

### Socratic Question 3: Planned Route from Surf (3, 3) to Gold Teeth (19, 7)
- **Planned Route**:
  1. Exit Secret House at (3, 3) -> Walk Down 2 steps to Row 5 at (3, 5). [Buttons: 'Down' * 2, Step Cost: 2]
  2. Walk Right 15 steps along Row 5 to (18, 5). [Buttons: 'Right' * 15, Step Cost: 15]
  3. Walk Down 3 steps to (18, 8). [Buttons: 'Down' * 3, Step Cost: 3]
  4. Walk Right 1 step to (19, 8) facing Up. [Buttons: 'Right', Step Cost: 1]
  5. Press 'A' to retrieve the Gold Teeth at (19, 7). [Buttons: 'A', Step Cost: 0]
  - **Total Steps from Surf to Gold Teeth**: 2 + 15 + 3 + 1 = 21 steps.
  - **Remaining Steps after Gold Teeth**: 195 - 21 = 174 steps remaining.
- **Why Row 5 northern corridor is required**: The eastern ground corridor is completely blocked on Columns 23-24 by continuous solid tree walls (TYPE_2889) across Rows 1-12, making vertical ground-level transitions impassable. Walking along the open, grass-free Row 5 corridor is the only viable path.

## Corrected Run 20 Chronological Overworld Logs (Turn 53774 to 53814)
- Turn 53774: Walked Right 5 steps from (11, 16) to (16, 16) on the plateau. No encounters. Steps remaining: 247.
- Turn 53781: Walked Right 5 steps from (16, 16) to (21, 16) on the plateau. No encounters. Steps remaining: 242.
- Turn 53783: Walked Down 4 steps from (21, 16) to (21, 20) on ground level, descending the East stairs. No encounters. Steps remaining: 238.
- Turn 53805: Walked Right 4 steps from (21, 20) to (25, 20) to enter the eastern corridor. No encounters. Steps remaining: 234.
- Turn 53814: Walked Up 7 steps from (25, 20) to (25, 13) in the eastern corridor. No encounters. Steps remaining: 227.
- Turn 53835: Verified that Column 24 Row 5 is indeed blocked by solid tree walls (TYPE_2889). Ground passage west is completely closed. Backtracking: walking Down 15 steps along Column 25 to (25, 20). No encounters. Steps remaining: 219.