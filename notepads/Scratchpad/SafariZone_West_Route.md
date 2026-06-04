# Safari Zone West Exploration Scratchpad (Run 23 Planning & Execution)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Current Status**: Standing at (22, 22) inside Safari Zone North (Map 0_218) on Turn 55805.
- **Step Budget Remaining**: 207 steps.
- **Next Step**: Walk Left 6 steps along Row 22 to (16, 22) to begin traversing the plateau.

## Socratic Question Answers (Turn 55805 Update)

### Socratic Question 1: Persisting Tracking Latency and Enforced Routing to Western Plateau Stairs
- **Why tracking latency persisted**: Latency occurred because our overworld movement sequence (Left 17 steps from 26, 33) collided with a building wall/roof at (19, 33) on Turn 55755, which aborted our movement early at (20, 33). When movements are blocked or interrupted, our physical position and step budget change, and our records become temporarily out of sync until we call our bookkeeping tool and edit our notepad using official harness tools.
- **Enforced Protocol**:
  1. Immediately after any overworld movement sequence or battle, call `safari_navigator_agent` to compute coordinates and step budget deltas (Completed on Turn 55801!).
  2. Call `notepad_edit` using the official harness tool to update the top status block and append exact movement logs (Completed on Turn 55805!).
  3. Call `update_objectives` to synchronize navigation goals (Completed on Turn 55752!).
  4. Only proceed with further movement after the files and objectives are fully synchronized.
- **Route to Western Plateau stairs at (22, 23) minimizing tall grass**:
  - Current position is (22, 22) on the plateau.
  - We successfully took:
    - 3 steps Up along Column 21 from (21, 31) to (21, 28) on Turn 55773.
    - 3 steps Up along Column 21 from (21, 28) to (21, 25) on Turn 55780.
    - 1 step Up to (21, 24) and 1 step Right to (22, 24) on Turn 55785 (interrupted by wild Nidorino battle, fled on Turn 55788).
    - 1 step Up to climb the stairs at (22, 23) on Turn 55794.
    - 1 step Up to land on the plateau at (22, 22) on Turn 55799.
  - This path touched exactly 7 grass tiles and successfully climbed the stairs with minimum grass exposure.

### Socratic Question 2: Completed Chronological Logs (Run 23)
- Turn 54981: Cut the first bush at (18, 19) in Fuchsia City.
- Turn 54996: Cut the second bush at (16, 11) in Fuchsia City.
- Turn 54999: Took the warp to Safari Zone Gatehouse.
- Turn 55007: Paid ¥500 and started Safari Run 23, spawning at (15, 25) in Safari Zone Center.
- Turn 55585: Attempted to walk Down to (15, 26) but triggered 'Leaving early?' prompt; selected NO and returned to (15, 25).
- Turn 55588: Walked 9 steps to reach (21, 22) (1 Left, 2 Up, 1 Right, 1 Up, 6 Right). New steps remaining: 455 steps.
- Turn 55591: Standing at (21, 22) planning our route to (29, 10).
- Turn 55595: Attempted to walk Right to (22, 14), triggered a wild Nidorina battle; selected RUN and escaped.
- Turn 55598: Walked 12 steps (4 Up, 8 Right) to transition to Safari Zone East at (0, 22). New steps remaining: 415 steps.
- Turn 55604: Walked 5 steps to reach (5, 22) (Right x5). New steps remaining: 410 steps.
- Turn 55607: Walked 9 steps to reach (10, 24) (Left x1, Down x2, Right x6). New steps remaining: 403 steps.
- Turn 55609: Walked 11 steps to reach (21, 24) (Right x11). New steps remaining: 392 steps. (Correction: Live navigator tracked Manhattan distance 403 - 11 = 392, but manually verified as 3 steps to (24, 24) and 3 steps to (24, 21), resulting in 397 steps remaining on Turn 55621).
- Turn 55612: Walked 3 steps to reach (24, 24) (Right x3). New steps remaining: 400 steps.
- Turn 55616: Walked 3 steps to reach (24, 21) (Up x3), triggered a wild Exeggcute battle; selected RUN and escaped on Turn 55619. New steps remaining: 397 steps.
- Turn 55625: Walked 9 steps Up along Column 24 to reach (24, 12) on the plateau. New steps remaining: 388 steps.
- Turn 55634: Walked 5 steps Left along Row 12 of the plateau to reach (19, 12). New steps remaining: 383 steps.
- Turn 55642: Walked 10 steps (Right x2, Down x8) to bypass the lake and reach (21, 20) on the plateau. New steps remaining: 373 steps.
- Turn 55644: Walked 9 steps Left along Row 20 of the plateau to reach (12, 20). New steps remaining: 364 steps.
- Turn 55645: Walked 2 steps Down to descend the western plateau stairs to (12, 22) on the ground level. New steps remaining: 362 steps.
- Turn 55652: Walked 3 steps Left from (12, 22) to reach (9, 22) on the ground level. New steps remaining: 359 steps.
- Turn 55656: Walked 6 steps Up along Column 9 to reach (9, 16). New steps remaining: 353 steps.
- Turn 55665: Walked 6 steps Up along Column 9 to reach (9, 10). New steps remaining: 353 steps. (Note: No steps taken since Turn 55657 until Turn 55665).
- Turn 55668: Walked 2 steps (Right x1, Up x2, Left x1) to reach (9, 8), bypassing the (9, 9) tall grass. New steps remaining: 351 steps.
- Turn 55674: Walked 5 steps (Right x3, Up x2) to climb the northern stairs at (12, 7) onto the northern plateau at (12, 6). New steps remaining: 346 steps.
- Turn 55678: Walked 7 steps (Right x5, Down x2) to descend the eastern plateau stairs from (12, 6) to (17, 8) on the ground level. New steps remaining: 339 steps.
- Turn 55684: Walked 4 steps Right to (21, 8) and Turn 55686: Walked 5 steps Up to (21, 3) along Column 21 on the ground level. New steps remaining: 330 steps.
- Turn 55691: Attempted to walk Left to (17, 3), triggered a wild Nidorina battle at (21, 3); selected RUN and escaped on Turn 55694. New steps remaining: 330 steps.
- Turn 55705: Attempted to walk Left 9 steps along Row 3 to (8, 3); triggered a wild Exeggcute battle at (16, 3) on the first step.
- Turn 55708: Selected RUN from the battle menu and successfully escaped the wild Exeggcute. New steps remaining: 325 steps.
- Turn 55715: Walked 8 steps Left along Row 3 from (16, 3) to (8, 3). No encounters. New steps remaining: 317 steps.
- Turn 55721: Walked 2 steps Down to (8, 5) and 8 steps Left along Row 5 to reach (0, 5). No encounters. New steps remaining: 307 steps.
- Turn 55723: Walked Left 1 step from (0, 5) to transition into Safari Zone North (Map 0_218) at (39, 31). New steps remaining: 241 steps.
- Turn 55727: Walked 11 steps Left along Row 31 from (39, 31) to reach (28, 31). No encounters. New steps remaining: 230 steps.
- Turn 55731: Walked 2 steps Down along Column 28 from (28, 31) to reach (28, 33). No encounters. New steps remaining: 228 steps.
- Turn 55735: Attempted to walk Left 19 steps to (9, 33); triggered a wild Venomoth battle at (26, 33) on the second step.
- Turn 55737: Selected RUN from the battle menu and successfully escaped the wild Venomoth on Turn 55738. New steps remaining: 226 steps.
- Turn 55755: Attempted to walk Left 17 steps along Row 33 to reach (9, 33); collided with a solid building roof/wall of TYPE_2889 at (19, 33) on the 6th step. Left us standing at (20, 33) facing Left. No encounters. New steps remaining: 220 steps.
- Turn 55765: Walked 1 step Right to (21, 33) and 2 steps Up to (21, 31) along Column 21 on the ground level. No encounters. New steps remaining: 217 steps.
- Turn 55773: Walked 3 steps Up along Column 21 from (21, 31) to (21, 28). No encounters. New steps remaining: 214 steps.
- Turn 55780: Walked 3 steps Up along Column 21 from (21, 28) to (21, 25). No encounters. New steps remaining: 211 steps.
- Turn 55785: Walked 1 step Up to (21, 24) and 1 step Right to (22, 24); triggered wild Nidorino battle at (22, 24). Selected RUN and escaped on Turn 55788. New steps remaining: 209 steps.
- Turn 55794: Walked 1 step Up from (22, 24) onto the stairs at (22, 23). No encounters. New steps remaining: 208 steps.
- Turn 55799: Walked 1 step Up from (22, 23) to land on (22, 22) on the plateau. No encounters. New steps remaining: 207 steps.

### Socratic Question 3: Exact Route across Western Plateau of Safari Zone North
- Once we climb onto the Western Plateau of Safari Zone North (Map 0_218) at (22, 22), we will traverse the plateau to reach the western descent stairs at (16, 27) and transition:
  1. Walk Left 6 steps along Row 22 of the plateau from (22, 22) to reach (16, 22). This row is completely open and has no tall grass, meaning 0% chance of wild encounters.
  2. Walk Down 5 steps along Column 16 of the plateau from (16, 22) to reach (16, 27). This path is also completely clear.
  3. Walk Down 1 step from (16, 27) to descend the stairs to the western ground level.

### Socratic Question 4: Route from Safari Zone North to Secret House in Safari Zone West
- Once we transition into Safari Zone West (Map 0_219) at (26, 0) or (27, 0) from Safari Zone North, we will traverse the map to the Secret House at (3, 3) using this 100% collision-free route:
  1. **Ground Corridor Descent**: Walk Down 17 steps along Column 26/27 from (26, 0) to reach (26, 17) or (27, 17) at the south edge.
  2. **Approach Eastern Plateau Stairs**: Walk Left 5 or 6 steps along Row 17 to reach (21, 17).
  3. **Climb Eastern Plateau**: Walk Left 1 step to climb the wooden stairs UP at (21, 17) to land on the plateau at (20, 17).
  4. **Traverse Southern Plateau**: Walk Left 2 steps to (18, 17), Down 3 steps to (18, 20), and Left 6 steps along Row 20 to reach (12, 20) on the plateau.
  5. **Traverse Mid-Plateau Corridor**: Walk Down 1 step to (12, 21), Left 6 steps along Row 21 to (6, 21), and Down 1 step to reach the western plateau descent stairs at (6, 22).
  6. **Descend to Southwest Ground Pocket**: Walk Up 3 steps down the stairs at (6, 19) to land on the southwest ground level at (6, 20).
  7. **Transition to Northwestern Area (Bypassing Lake & Rest House 3)**:
     - Walk Left 3 steps along Row 20 to (3, 20) and Up 4 steps along Column 3 to (3, 16) to safely bypass the central lake on Rows 10-13 (which blocks Columns 2-9 and Columns 4-7 further north).
     - Walk Right 5 steps to (8, 16) and Up 2 steps to (8, 14).
     - Walk Right 5 steps along Row 14 to (13, 14) to completely bypass Rest House 3 (located at 11, 11-12 with solid walls on Column 14 Rows 12-15).
  8. **Climb the Western Plateau at (13, 12) (STRICT VERIFICATION PLAN)**:
     - The Western Plateau ascent stairs are at (13, 12) (facing south).
     - Upon reaching the adjacent tile (13, 13) on the ground level, we will physically test passability by walking Up onto the stairs at (13, 12).
     - We will visually verify the tile type of (13, 12) is `TYPE_4b8d` (wooden stairs) on our `<CurrentScreen>` and that the player character successfully transitions onto the elevated plateau level.
     - If blocked or if any obstacle is present, we will immediately halt, document the collision, and revise our route rather than mashing or assuming a lag/desync.
  9. **Walk across the Western Plateau**: Walk Up 4 steps to (13, 8), Left 10 steps to (3, 8), and Up 5 steps to reach (3, 3) to enter the Secret House and retrieve HM03 Surf!
  10. **Gold Teeth**: Pick up the Warden's Gold Teeth at (19, 7) on the Western Plateau.

## Run 23 Route Plan (Safari Zone East to Secret House)
1. Traverse Safari Zone East to Safari Zone North (Map 0_218) (~35 steps).
2. Traverse Safari Zone North to Safari Zone West (Map 0_219) (~70 steps).
3. Traverse Safari Zone West to the Secret House at (3, 3) (~65 steps) and retrieve HM03 Surf!