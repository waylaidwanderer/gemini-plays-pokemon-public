# Safari Zone West - Run 43 Route and Logs Archive

## Active Campaign Plan (Run 43 Victory Route)
We are executing a fully optimized Run 43 ground-to-plateau dual retrieval.
1. **Walk to Gatehouse**: From (19, 28), walk to the first cuttable bush at (18, 19). Standing at (18, 20), use CUT to clear the bush.
2. **First Corridor Traversal**: Walk Up to (16, 11). Standing at (16, 12), use CUT to clear the second bush.
3. **Safari Entrance**: Walk to (18, 3) and enter the Safari Zone Gatehouse.
4. **Register**: Pay ¥500, enter Safari Zone Center (Map 0_220) at (15, 25) with a full 500-step budget.
5. **Center to East Transition**: Walk to the East transition at (29, 11) in Safari Zone Center -> **28 steps**.
6. **East Corridor Traversal**: Transition to East (Map 0_217) at (0, 23). Walk and climb Southern stairs at (20, 21), cross plateau, descend Western stairs at (12, 22), bypass tall grass (9, 9) via Column 9 corridor, climb northern stairs at (12, 7) onto high plateau at (12, 6), cross to East (21, 6), descend to ground, walk along Row 3 to the West, and transition to Safari Zone North at (39, 31) -> **40 steps**.
7. **North Corridor Traversal**: Transition to North (Map 0_218) at (39, 31). Walk along Row 31 to (28, 31), climb Eastern stairs at (28, 27) [climbing from (28, 28)] onto plateau, descend Western stairs at (16, 27) [descending to (16, 28)], walk to Column 9 Row 30, and walk Down along Column 9 to transition to Safari Zone West at (26, 0) / (27, 0) -> **40 steps**.
8. **West Quad Double-Retrieval**: 
   - Transition to West (Map 0_219) at (27, 0) [z=0].
   - Walk Down to (27, 18), Left 6 to (21, 18), and climb Eastern stairs UP to (21, 16) [z=1].
   - Walk Left 5 to (16, 16) [z=1], Up 7 to (16, 9) [z=1].
   - Walk Down 7 to (16, 16) [z=1], Right 1 to (17, 16) [z=1] on Koga's bridge.
   - Walk Up 2 to (17, 14), Right 1 to (18, 14) [z=1].
   - Walk Up 5 along Column 18 to (18, 9) [z=1], and Right 1 to jump down onto (19, 9) [z=0] on the ground.
   - Walk Up 2 steps to stand adjacent to the Warden's Gold Teeth at (19, 7) [z=0], and pick them up!
   - Walk West 16 steps along the Row 5 ground-level corridor, and walk Up to enter the Secret House at (3, 3) to get HM03 Surf!
   - Total steps used in West: ~35 steps. Total steps used across entire run: ~143 steps (out of 500), leaving a massive surplus of ~357 steps inside the Secret House!
9. **Warp Home**: Use DIG to warp back to Fuchsia City!

## Chronological Movement Log (Run 42)
- Turn 68118: Entered Safari Zone Center (Map 0_220) at (15, 25) with a starting budget of 500 steps.
- Turn 68134: Transitioned to Safari Zone East (Map 0_217) at (0, 23).
- Turn 68236: Transitioned to Safari Zone North (Map 0_218) at (39, 31).
- Turn 68338: Transitioned to Safari Zone West (Map 0_219) at (26, 0).
- Turn 68364: Climbed Eastern Plateau stairs at (21, 17) [climbing from (21, 18)].
- Turn 68388: Traversed Koga's Eastern Plateau and descended Western Plateau stairs at (6, 19) to (6, 20).
- Turn 68425: Escaped a wild battle at (6, 20).
- Turn 68430: Run safari_navigator_agent to synchronize steps to 339 remaining.
- Turn 68458: Walked Left 4 steps from (6, 20) to (2, 20) (remaining: 335).
- Turn 68469: Walked Up 6 steps along Column 2 to (2, 14) (remaining: 329).
- Turn 68472: Empirically verified water blockage at Column 2 Row 13 (TYPE_4e8c).
- Turn 68479: Backtracked Down 6 steps along Column 2 to (2, 20) (remaining: 323).
- Turn 68487: Walked Right 4 steps to (6, 20) (remaining: 319).
- Turn 68490: Overwatch step reconciliation: confirmed exactly 247 actual physical steps remaining in RAM on Turn 68490.
- Turn 68497: Climbed stairs Up 2 steps from (6, 20) to (6, 18) [z=1] (remaining: 245).
- Turn 68500: Walked Up 2 steps to (6, 16) [z=1] (remaining: 243).
- Turn 68502: Walked Right 5 steps to (11, 16) [z=1] (remaining: 238).
- Turn 68505: Walked Right 5 steps to (16, 16) [z=1] (remaining: 233).
- Turn 68507: Walked Right 5 steps to (21, 16) [z=1] (remaining: 228).
- Turn 68511: Descended stairs Down 2 steps to (21, 18) [z=0] (remaining: 226).
- Turn 68516: Walked Right 4 steps to (25, 18) [z=0] (remaining: 222).
- Turn 68519: Walked Up 6 steps along Column 25 to (25, 12) [z=0] (remaining: 216).
- Turn 68531: Walked Up 6 steps along Column 25 to (25, 6) [z=0] (remaining: 210).
- Turn 68533: Walked Up 4 steps along Column 25 to (25, 2) [z=0], bumping twice against the solid tree wall at (25, 1) (remaining: 206).
- Turn 68540: Walked Right 1 step to (26, 2), Up 2 steps along Column 26 to (26, 0) [z=0] (remaining: 203).
- Turn 68542: Walked Up 1 step to transition to Safari Zone North, landing at (8, 35) [z=0] (remaining: 202).
- Turn 68557: Walked Up 4 steps along Column 8 to (8, 31) [z=0] (remaining: 198).

## 50-Turn Reflection (Turn 68614)
1. **Current Position & Map ID**: Standing at (8, 31) [z=0] on Map 0_218 (Safari Zone North).
2. **Custom Tool Usage**: Redefined safari_pathfinder on Turn 68590 to incorporate Map 0_218 correct water lake and tree walls, fixing the database gap.
3. **Notepads & Objectives Update**: Updated Scratchpad/SafariZone_West_Route and Mechanics/Socratic_West_Answers to reflect 198 steps remaining and corrected the chronological steps-taken math.
4. **50-Turn Plan**: Walk across the North Corridor using the verified ground-level path ['Up', 'Left', 'Up', 'Up', 'Up', 'Up', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left'] to reach the Northwest transition to Safari Zone West ground level Northwest plains (where the Secret House and teeth are located). Walk to the Secret House and obtain HM03 Surf!

## 50-Turn Reflection (Turn 69228)
1. **Immediate Execution**: I analyzed our position and confirmed that the Southwest ground pocket is physically closed on foot, making a backtrack over Koga's bridge mandatory.
2. **Notepad Hygiene**: Recorded the closure of the Southwest ground pocket on foot in Locations/SafariZone_West and added a clean transition backtrack log.
3. **Map Hygiene**: Map markers are accurate and up to date. I will use the established markers for routing.
4. **Custom Tools**: safari_pathfinder was extremely useful for determining the multi-map route.
5. **Tool Maintenance**: Kept the pathfinder updated to model the correct 3D elevation transitions.
6. **Goal Clarity**: Our primary goal remains retrieving the Gold Teeth and Surf from Safari Zone West, and the method is traversing back over Koga's bridge to Safari Zone North, then descending into the Northwest quadrant of Safari Zone West.
7. **Error Analysis**: By verifying our assumptions about the Southwest ground pocket, we avoided spending more steps trying to force a route through a closed area.