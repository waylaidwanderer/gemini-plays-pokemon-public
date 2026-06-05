# Safari Zone West Exploration Scratchpad (Run 28 Planning & Execution)
- **Current Status**: Standing at (34, 14) in Safari Zone North (Map 0_218) on Turn 58263 with exactly 345 steps remaining.
- **Inventory Status**: 15/20 items. (COMPLETED)
- **Next Step**: Walk Down 2 steps to descend plateau stairs to (34, 16) and navigate to Safari Zone West.

## Run 28 Optimal Double-Retrieval Route Plan (500 Step Budget)
1. **Prepare**: Deposit items in PC to have at least 2 free slots (15/20 items). (COMPLETED)
2. **Travel to Gatehouse**: Exit Pokémon Center, walk to (18, 3) in Fuchsia City, and enter the Safari Zone Gatehouse. (COMPLETED)
3. **Start Run 28**: Pay Yen500 and enter Safari Zone Center (Area 0) at (15, 25). (COMPLETED)
4. **Transition to Safari Zone East (Area 1)**:
   - Walk from Center (15, 25) to East at (0, 22) [~18 steps used]. (COMPLETED)
5. **Transition to Safari Zone North (Area 2)**:
   - Walk from East (0, 23) to North at (0, 5) using the central corridor: East 4 to (4, 23), Down 1 to (4, 24), East 17 to (21, 24) [or 10 steps East to (14, 24) due to wild encounter], climb Eastern stairs to plateau at (20, 20), walk Left across plateau to (12, 20), descend western stairs to (12, 22), walk Left 3 and Up 14 along Column 9 to Row 8, walk Right 3 to (12, 8), and climb northern plateau stairs UP to (12, 6) [climbing stairs at (12, 7)].
   - Walk East across the plateau to Column 21, walk Up to Row 2, and walk West along Row 2/3 to the northwest transition at Column 0 to exit into Safari Zone North (Area 2) at (0, 5).
6. **Transition to Safari Zone West (Area 3)**:
   - Walk from North (39, 31) to West at (27, 0) [~48 steps used].
7. **Traverse West Plateau to Northern Ground Level**:
   - Climb UP the southeastern stairs: (21, 18) -> (21, 17) -> (21, 16) [2 steps].
   - Walk across the plateau to the eastern ramp: Left 3 steps to Column 18, Up 7 steps to (18, 9) [10 steps].
   - Descend (jump down) the plateau ramp to the east: (18, 9) -> (19, 9) [1 step].
8. **Retrieve Warden's Gold Teeth and Surf**:
   - Walk Up 2 steps to retrieve Gold Teeth at (19, 7) [2 steps].
   - Walk Up 2 steps to Row 5, Left 16 steps along Row 5 to Column 3, and Up 2 steps to enter the Secret House at (3, 3) [20 steps].
   - Receive HM03 Surf!
   - Use DIG to return to Fuchsia City.

## Run 28 Chronological Movement Log:
- Turn 58100: Paid Yen500 and entered Safari Zone Center (Map 0_220) at (15, 25) with 500 steps remaining (Start of Run 28).
- Turn 58103: Used safari_pathfinder to walk across Center to (28, 16) [22 steps used, 478 remaining].
- Turn 58108: Walked Up 5 steps along Column 28 to (28, 11) and Right 1 step to (29, 11) [6 steps used, 472 remaining].
- Turn 58109: Walked Right 1 step to transition from Safari Zone Center to Safari Zone East (Map 0_217) at (0, 23) [1 step used].
- Turn 58111: Synchronized step budget using safari_navigator_agent, confirming exactly 482 steps remaining at (0, 23).
- Turn 58113: Walked East 4 steps to (4, 23) and Down 1 step to (4, 24) [5 steps used, 477 remaining].
- Turn 58117: Walked East 10 steps to (14, 24) [10 steps used, 467 remaining]. Wild Nidoran♀ encounter occurred.
- Turn 58122: Walked East 7 steps to (21, 24) [7 steps used, 460 remaining].
- Turn 58125: Walked Left 1 step to (20, 24) and Up 1 step to (20, 23) [2 steps used, 458 remaining]. Wild Exeggcute encounter occurred.
- Turn 58128: Walked Up 1 step to (20, 23) [1 step used, 457 remaining]. Wild Exeggcute encounter occurred, returned to (20, 24).
- Turn 58131: Walked Up 4 steps along Column 20 to climb onto the plateau at (20, 20) [4 steps used, 453 remaining].
- Turn 58136: Walked Left 8 steps across the plateau to Column 12 at (12, 20) [8 steps used, 445 remaining].
- Turn 58138: Walked Down 2 steps to descend the plateau stairs to ground level at (12, 22) [2 steps used, 443 remaining].
- Turn 58139: Walked Left 3 steps to Column 9 and Up 4 steps along Column 9 to (9, 18) [7 steps used, 436 remaining].
- Turn 58145: Synchronized step budget using safari_navigator_agent, confirming exactly 436 steps remaining at (9, 18).
- Turn 58181: Wild Nidoran♂ encounter at (20, 4) in Safari Zone East.
- Turn 58182: Successfully caught Nidoran♂ (named THORN) and sent to BILL's PC.
- Turn 58194: Synchronized step budget using safari_navigator_agent, confirming exactly 409 steps remaining at (20, 4).
- Turn 58195: Walked Up 1 step and Left 5 steps to (15, 3) [6 steps used].
- Turn 58196: Synchronized step budget using safari_navigator_agent, confirming exactly 403 steps remaining at (15, 3).
- Turn 58198: Walked Left 6 steps to (9, 3) [6 steps used].
- Turn 58199: Synchronized step budget using safari_navigator_agent, confirming exactly 397 steps remaining at (9, 3).
- Turn 58208: Walked Down 2 steps to (9, 5) [2 steps used].
- Turn 58209: Synchronized step budget using safari_navigator_agent, confirming exactly 395 steps remaining at (9, 5).
- Turn 58214: Walked Left 6 steps along Row 5 from (9, 5) to (3, 5) [6 steps used].
- Turn 58215: Synchronized step budget using safari_navigator_agent, confirming exactly 389 steps remaining at (3, 5).
- Turn 58217: Walked Left 3 steps along Row 5 from (3, 5) to (0, 5) [3 steps used].
- Turn 58218: Synchronized step budget using safari_navigator_agent, confirming exactly 386 steps remaining at (0, 5).
- Turn 58220: Walked Left 1 step to transition to Safari Zone North (Map 0_218) at (39, 31) [1 step used].
- Turn 58222: Synchronized step budget, recalibrating coordinate jump warp error to confirm exactly 385 steps remaining at (39, 31).
- Turn 58223: Walked Left 11 steps along Row 31 from (39, 31) to (28, 31) [11 steps used].
- Turn 58224: Synchronized step budget using safari_navigator_agent, confirming recalibrated budget of 374 steps remaining at (28, 31).
- Turn 58228: Walked Up 5 steps along Column 28 to climb the plateau stairs at (28, 27) and land on the plateau at (28, 26) [5 steps used].
- Turn 58231: Synchronized step budget using safari_navigator_agent, confirming exactly 369 steps remaining at (28, 26).
- Turn 58236: Walked Right 5 steps across the Eastern Plateau from (28, 26) to (33, 26) [5 steps used].
- Turn 58238: Synchronized step budget using safari_navigator_agent, confirming exactly 364 steps remaining at (33, 26).
- Turn 58245: Walked Right 4 steps and Up 2 steps to bypass the plateau cliff wall and reach (37, 24) [6 steps used].
- Turn 58248: Synchronized step budget using safari_navigator_agent, confirming exactly 358 steps remaining at (37, 24).
- Turn 58252: Walked Up 9 steps along Column 37 to (37, 15) [9 steps used].
- Turn 58253: Synchronized step budget using safari_navigator_agent, confirming exactly 349 steps remaining at (37, 15).
- Turn 58256: Walked Up 1 step and Left 3 steps along Row 14 to (34, 14) [4 steps used].
- Turn 58258: Synchronized step budget using safari_navigator_agent, confirming exactly 345 steps remaining at (34, 14).