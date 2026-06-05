# Safari Zone West Exploration Scratchpad (Run 27 Planning & Execution)
- **Current Status**: Standing at (12, 20) on ground level of Safari Zone West (Map 0_219) on Turn 58030 with exactly 158 steps remaining.
- **Inventory Status**: 15/20 items. (COMPLETED)
- **Next Step**: Walk Left 6 steps to (6, 20) and Up 2 steps to climb the Western Plateau stairs at (6, 19) to reach (6, 18).

## Run 27 Optimal Double-Retrieval Route Plan (500 Step Budget)
1. **Prepare**: Deposit items in PC to have at least 2 free slots (15/20 items). (COMPLETED)
2. **Travel to Gatehouse**: Exit Pokémon Center, walk to (18, 3) in Fuchsia City, and enter the Safari Zone Gatehouse. (COMPLETED)
3. **Start Run 27**: Pay Yen500 and enter Safari Zone Center (Area 0) at (15, 25). (COMPLETED)
4. **Transition to Safari Zone West (Area 3)**:
   - Walk from Center (15, 25) to East at (0, 22) [~28 steps used]. (COMPLETED)
   - Walk from East (0, 22) to North at (39, 31) [~53 steps used]. (COMPLETED)
   - Walk from North (39, 31) to West at (27, 0) [~48 steps used]. (COMPLETED)
5. **Traverse Plateau to Western Ground Level**:
   - Climb UP the southeastern stairs: (21, 18) -> (21, 17) -> (21, 16) [2 steps]. (COMPLETED)
   - Walk across the plateau to the western stairs: Left 10 to (11, 16) [10 steps], Down 2 to (11, 18) [2 steps], Left 5 to (6, 18) [5 steps]. (COMPLETED)
   - Descend the western stairs to the ground: (6, 18) -> (6, 19) -> (6, 20) [2 steps]. (COMPLETED)
6. **Bypassing Obstacles & Backtracking**:
   - Walked Right 6 steps to (12, 20) along Row 20 to test ground bypass. Bumped at (12, 19), confirming Row 19 is a solid tree/cliff wall (TYPE_2889) and the southwest ground quadrant is indeed a completely closed pocket.
   - Walk Left 6 steps to (6, 20), climb back UP the stairs to (6, 18), traverse back across the plateaus to (21, 16), descend to (21, 18), walk to (27, 18), and walk Up to (27, 0) to transition back to Safari Zone North at (9, 35).
7. **Retrieve Warden's Gold Teeth and Surf**:
   - Retrying pathing on the north of the Western/Eastern Plateau or ground level after returning to Safari Zone North.

## Run 27 Chronological Movement Log:
- Turn 57710: Paid Yen500 and entered Safari Zone Center (Map 0_220) at (15, 25) with 500 steps remaining (Start of Run 27).
- Turn 57712: safari_pathfinder moved us to (28, 16) [22 steps used, 478 remaining].
- Turn 57713: Walked Up 5 steps along Column 28 to Y=11, and Right 1 step to (29, 11) [6 steps used, 472 remaining].
- Turn 57714: Walked Right 1 step to transition from Safari Zone Center to Safari Zone East (Map 0_217) at (0, 23) [1 step used, 471 remaining].
- Turn 57718: Walked Up 2 steps to (0, 21) [2 steps used, 469 remaining].
- Turn 57722: Walked Right 5 steps along Row 21 to (5, 21) [5 steps used, 464 remaining].
- Turn 57728: Walked Left 1 step and Down 3 steps to reach (4, 24) on ground level [4 steps used, 460 remaining].
- Turn 57733: Walked Right 16 steps along Row 24 to Column 20, then Up 3 steps to reach the stairs at (20, 21) [19 steps used, 441 remaining].
- Turn 57735: Walked Up 1 step to climb onto the Eastern Plateau at (20, 20) [1 step used, 440 remaining].
- Turn 57738: Walked Right 2 steps to Column 22 and Up 10 steps along Column 22 on the plateau. A wild encounter occurred on Row 12, aborting movement and leaving us at (22, 12) facing Down [10 steps used, 430 remaining].
- Turn 57744: Walked Right 2 steps to Column 24 and Down 4 steps to descend the plateau stairs at (24, 15), landing on ground level at (24, 16) [6 steps used, 424 remaining].
- Turn 57746: Walked Up 2 steps to climb back onto the Eastern Plateau at (24, 14) [2 steps used, 422 remaining].
- Turn 57748: Synchronized step budget using the safari navigator agent, confirming exactly 469 steps remaining [tracking budget recalibrated].
- Turn 57800: Walked East on plateau to (17, 6), descended stairs at (17, 7) to ground level (17, 8). Then walked East to Column 21 and North to Row 3, landing at (21, 3) facing Up. Exactly 9 steps used.
- Turn 57802: Standing at (21, 3) on the northern ground corridor. Planning to walk West along Row 3 to Column 1 (20 steps), then Down to Row 5 (2 steps), and West to Column 0 (1 step) to trigger transition to Safari Zone North at (0, 5).
- Turn 57804: Walked Left 10 steps along Row 3 to (11, 3) [10 steps used, 459 remaining].
- Turn 57806: Walked Left 5 steps along Row 3 to (6, 3), where movement was blocked by a solid tree wall at (5, 3). The subsequent 5 Left presses, 2 Down presses, and 1 Left press resulted in wall collisions (bumps) [5 steps used, 454 remaining].
- Turn 57812: Synchronized step budget using the safari navigator agent, confirming exactly 440 steps remaining [tracking budget recalibrated].
- Turn 57817: Attempted to walk to Column 1 Row 3 but found it blocked by a tree wall. Arrived at (1, 2) facing Left.
- Turn 57819: Detoured around the tree wall by walking Right 6 steps, Down 3 steps, and Left 7 steps, arriving at (0, 5) facing Left. [16 steps used, 424 remaining].
- Turn 57821: Synchronized step budget using the safari navigator agent, confirming exactly 432 steps remaining at (0, 5) [tracking budget recalibrated].
- Turn 57823: Pressed Left once to exit Safari Zone East at (0, 5) and transition to Safari Zone North (Map 0_218) at (39, 31). [1 step used, 431 remaining].
- Turn 57825: Synchronized step budget using the safari navigator agent after map transition, confirming exactly 366 steps remaining at (39, 31) [tracking budget recalibrated].
- Turn 57831: Walked Left 11 steps along Row 31 from (39, 31) to (28, 31) [11 steps used, 355 remaining].
- Turn 57834: Synchronized step budget using the safari navigator agent, confirming exactly 355 steps remaining at (28, 31) [tracking budget recalibrated].
- Turn 57836: Walked Up 5 steps to climb onto the Eastern Plateau at (28, 26) [5 steps used, 350 remaining].
- Turn 57839: Walked Right 5 steps across the plateau to (33, 26) [5 steps used, 345 remaining].
- Turn 57841: Synchronized step budget using the safari navigator agent, confirming exactly 345 steps remaining at (33, 26) [tracking budget recalibrated].
- Turn 57848: Walked Right 4 steps to Column 37, and Up 2 steps to (37, 24) to bypass the plateau cliff wall gap. [6 steps used, 339 remaining].
- Turn 57849: Synchronized step budget using the safari navigator agent, confirming exactly 339 steps remaining at (37, 24) [tracking budget recalibrated].
- Turn 57852: Walked Up 9 steps along Column 37 to (37, 15) [9 steps used, 330 remaining].
- Turn 57855: Synchronized step budget using the safari navigator agent, confirming exactly 330 steps remaining at (37, 15) [tracking budget recalibrated].
- Turn 57856: Walked Up 1 step to Row 14, Left 3 steps along Row 14 to Column 34, and Down 2 steps to descend the plateau stairs to (34, 16) [6 steps used, 324 remaining].
- Turn 57857: Synchronized step budget using the safari navigator agent, confirming exactly 326 steps remaining at (34, 16) [tracking budget recalibrated].
- Turn 57866: Walked Down 4 steps along Column 34 to (34, 20) [4 steps used, 322 remaining].
- Turn 57869: Synchronized step budget using the safari navigator agent, confirming exactly 322 steps remaining at (34, 20) [tracking budget recalibrated].
- Turn 57874: Walked Down 3 steps along Column 34 to (34, 23) [3 steps used, 319 remaining].
- Turn 57880: Walked Left 8 steps along Row 23 from (34, 23) to (26, 23) [8 steps used, 311 remaining].
- Turn 57882: Synchronized step budget using the safari navigator agent, confirming exactly 311 steps remaining at (26, 23) [tracking budget recalibrated].
- Turn 57890: Attempted to walk Down from (26, 23) to (26, 24) but bumped against a solid cliff face, confirming (26, 24) is impassable [0 steps used, 311 remaining].
- Turn 57895: Walked Up 4 steps to reach (26, 19) [4 steps used, 307 remaining].
- Turn 57897: Synchronized step budget using the safari navigator agent, confirming exactly 307 steps remaining at (26, 19) [tracking budget recalibrated].
- Turn 57903: Walked Left 9 steps along Row 19 to (17, 19) [9 steps used, 298 remaining].
- Turn 57907: Synchronized step budget using the safari navigator agent, confirming exactly 298 steps remaining at (17, 19) [tracking budget recalibrated].
- Turn 57927: Walked Right 17 steps along Row 19 from (17, 19) to (34, 19) [17 steps used, 281 remaining].
- Turn 57930: Walked Up 5 steps along Column 34 to climb the Eastern Plateau stairs at (34, 15) to land at (34, 14) [5 steps used, 276 remaining].
- Turn 57931: Synchronized step budget using the safari navigator agent, confirming exactly 276 steps remaining at (34, 14) [tracking budget recalibrated].
- Turn 57947: Walked Down 2 steps and Left 9 steps along Row 26 on the Eastern Plateau to reach (28, 26) [11 steps used, 265 remaining].
- Turn 57948: Synchronized step budget using the safari navigator agent, confirming exactly 265 steps remaining at (28, 26) [tracking budget recalibrated]. (Wait, actually 252 steps after correcting formula)
- Turn 57950: Walked Down 3 steps to descend Eastern Plateau stairs at (28, 27) onto ground level at (28, 29) [3 steps used, 249 remaining].
- Turn 57952: Synchronized step budget using the safari navigator agent, confirming exactly 249 steps remaining at (28, 29) [tracking budget recalibrated].
- Turn 57963: Walked Left 6 steps on ground level of Safari Zone North from (28, 29) to (22, 29) [6 steps used, 243 remaining].
- Turn 57964: Synchronized step budget using the safari navigator agent, confirming exactly 243 steps remaining at (22, 29) [tracking budget recalibrated].
- Turn 57968: Walked Up 7 steps on Column 22 to climb the Western Plateau stairs at (22, 23), landing on the plateau at (22, 22) [7 steps used, 236 remaining].
- Turn 57969: Synchronized step budget using the safari navigator agent, confirming exactly 236 steps remaining at (22, 22) [tracking budget recalibrated].
- Turn 57974: Walked Left 6 steps and Down 5 steps on the Western Plateau to reach the West Descent Stairs at (16, 27) [11 steps used, 225 remaining].
- Turn 57975: Synchronized step budget using the safari navigator agent, confirming exactly 225 steps remaining at (16, 27) [tracking budget recalibrated].
- Turn 57981: Walked Down 1 step and Left 7 steps on Row 28. Encountered water collision at Column 11, resulting in landing at (12, 28) [5 steps used, 220 remaining].
- Turn 57982: Synchronized step budget using the safari navigator agent, confirming exactly 220 steps remaining at (12, 28) [tracking budget recalibrated].
- Turn 57985: Walked Down 2 steps to (12, 30), Left 3 steps along Row 30 to Column 9, and Down 6 steps along Column 9 to transition to Safari Zone West (Map 0_219) at (27, 0) [11 steps used, 209 remaining].
- Turn 57987: Recalibrated step budget after transition using safari navigator agent, confirming exactly 209 steps remaining at (27, 0) [tracking budget recalibrated].
- Turn 57992: Walked Down 18 steps along Column 27 from (27, 0) to (27, 18) [18 steps used, 191 remaining].
- Turn 57993: Synchronized step budget using the safari navigator agent, confirming exactly 191 steps remaining at (27, 18) [tracking budget recalibrated].
- Turn 57996: Walked Left 6 steps to (21, 18) and Up 2 steps to climb the Eastern Plateau stairs at (21, 17) to reach (21, 16) [8 steps used, 183 remaining].
- Turn 57997: Synchronized step budget using the safari navigator agent, confirming exactly 183 steps remaining at (21, 16) [tracking budget recalibrated].
- Turn 58002: Walked Left 10 steps to (11, 16), Down 2 steps to (11, 18), Left 5 steps to (6, 18), and Down 2 steps to descend the Western Plateau stairs to ground level at (6, 20) [19 steps used, 164 remaining].
- Turn 58008: Synchronized step budget using the safari navigator agent, confirming exactly 164 steps remaining at (6, 20) [tracking budget recalibrated].
- Turn 58012: Walked Right 6 steps along Row 20 to (12, 20) and Up 1 step (bump/collision at Row 19), landing at (12, 20) [6 steps used, 158 remaining].
- Turn 58024: Recalibrated step budget after collision using safari navigator agent, confirming exactly 158 steps remaining at (12, 20) [tracking budget recalibrated].