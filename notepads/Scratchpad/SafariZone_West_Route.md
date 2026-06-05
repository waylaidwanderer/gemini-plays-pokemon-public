# Safari Zone West Exploration Scratchpad (Run 30 Planning & Execution)
- **Current Status**: Standing at (24, 14) in Safari Zone East (Map 0_217) on Turn 59192, with exactly 389 steps remaining.
- **Inventory Status**: 15/20 items. (COMPLETED)
- **Main Objectives**: Retrieve Warden's Gold Teeth at (19, 7) and HM03 Surf at (3, 3) in Safari Zone West.

## Fresh Run 30 Optimal Multi-Map Route Plan (500 Step Budget):
1. **Segment 1: Safari Zone Center (Map 0_220)**
   - Path: Walk Left 1 step to (14, 25), Up 2 steps to (14, 23), Right 14 steps to (28, 23), Up 12 steps to (28, 11), and Right 2 steps to transition to Safari Zone East at (0, 21).
   - Expected Cost: 31 steps.
2. **Segment 2: Safari Zone East (Map 0_217)**
   - Path: Enter at (0, 23) due to Center-to-East Row 11-to-23 offset transition. Walk Down 1 step to Row 24 at (0, 24), Right 20 steps along Row 24 to Column 20 at (20, 24) to bypass Rest House 1 on Row 23, and Up 3 steps to climb the stairs at (20, 21) to (20, 20) on the plateau. Walk Right 2 steps to Column 22 on the plateau and Up 10 steps along Column 22 to (22, 10). Descend the eastern plateau stairs at (24, 15) to ground level at (24, 16). Walk East to Column 21 and North to Row 3, landing at (21, 3). Walk Left to (0, 5) to transition to Safari Zone North at (39, 31).
   - Expected Cost: 25 steps to plateau + ~35 steps to transition = ~60 steps.
3. **Segment 3: Safari Zone North (Map 0_218)**
   - Path: Enter at (39, 31). Walk Left 11 steps along Row 31 to (28, 31). Climb plateau stairs UP at (28, 27) onto plateau at (28, 26). Walk across plateau to (34, 16) stairs, descend stairs to (34, 16). Walk around the southern corridor to Column 8/9 on Row 33, then walk Down to transition to Safari Zone West at (27, 0).
   - Expected Cost: ~48 steps.
4. **Segment 4: Safari Zone West (Map 0_219) - The Double Retrieval**
   - Path: Enter at (27, 0). Walk Down 18 steps along Column 27 to (27, 18), Left 6 steps to (21, 18), and Up 2 steps to climb Eastern stairs UP to (21, 16) on the plateau.
   - Walk across plateau to northern descent ramp at (18, 9). Descend/jump down ramp to ground level at (19, 9).
   - Walk Up 2 steps to stand at (19, 7) and press A to retrieve Warden's Gold Teeth.
   - Walk Left 16 steps along Row 7 to Column 3 at (3, 7) and Up 4 steps to (3, 3) to enter the Secret House. Talk to the NPC to receive HM03 Surf.
   - Use BLASTOISE's DIG to escape back to Fuchsia City outside the Pokémon Center.
   - Expected Cost: ~40 steps.

## Run 30 Chronological Movement Log:
- Turn 59053: Dialogue cleared, Safari Game Run 29 ended.
- Turn 59060: Stepped Up from (4, 3) in Gatehouse to (4, 2), triggering registration dialogue.
- Turn 59063: Paid ¥500 and started Safari Zone Run 30.
- Turn 59064: Entered Safari Zone Center (Map 0_220) at (15, 25) with exactly 500 steps remaining.
- Turn 59073: Walked to (14, 23).
- Turn 59076: Walked to (19, 23).
- Turn 59079: Walked to (23, 23).
- Turn 59083: Checked position (23, 23) via navigator agent [490 steps remaining].
- Turn 59088: Walked 5 steps Right to (28, 23) [485 steps remaining].
- Turn 59091: Walked 6 steps Up to (28, 17) [479 steps remaining].
- Turn 59115: Walked 6 steps Up to (28, 11) [473 steps remaining].
- Turn 59121: Walked 1 step Right to (29, 11) [472 steps remaining].
- Turn 59125: Walked 1 step Right to transition to Safari Zone East (Map 0_217) at (0, 23) [430 steps remaining].
- Turn 59137: Walked 1 step Down to (0, 24) [429 steps remaining].
- Turn 59139: Walked 5 steps Right to (5, 24) [424 steps remaining].
- Turn 59141: Walked 5 steps Right to (10, 24) [419 steps remaining].
- Turn 59145: Walked 5 steps Right to (15, 24) [414 steps remaining].
- Turn 59149: Walked 5 steps Right to (20, 24) [409 steps remaining].
- Turn 59154: Walked 4 steps Up to (20, 20) [405 steps remaining].
- Turn 59158: Walked 2 steps Right and 4 steps Up to (22, 16) [399 steps remaining].

## Strategic Answers to Turn 59130 Socratic Questions:
### Socratic Question 1 (Tracking Latency):
- **Tracking Latency**: The tracking latency accumulates when we perform multi-step movement segments without updating the log after each intermediate segment. To enforce a strict turn-by-turn routine, we will systematically run 'safari_navigator_agent' as the VERY FIRST action after any movement sequence or transition, and immediately perform a 'notepad_edit' to update both the Current Status block and chronological log in the same turn before pressing any more overworld buttons.

### Socratic Question 2 (Coordinate Discrepancy & East Route Adjustments):
- **Discrepancy Explanation**: The Center-to-East transition has a vertical coordinate shift of +12. Since we transitioned from Center (29, 11), we spawn in East at (0, 23).
- **Path Adjustments**: Since we spawn at (0, 23), we are already at Y=23 and do not need to walk on Row 21. We can bypass the Rest House at (5, 23) by simply going Down to Row 24 and walking East.
- **Tile-by-Tile Path to Southeastern Stairs at (20, 21)**:
  1. From (0, 23), walk Down 1 step to (0, 24). [Cost: 1 step].
  2. Walk Right 20 steps along Row 24 to (20, 24). [Cost: 20 steps].
  3. Walk Up 3 steps along Column 20 to the stairs at (20, 21). [Cost: 3 steps].
  4. Walk Up 1 step to climb onto the plateau at (20, 20). [Cost: 1 step].
  - **Total Cost**: 25 steps to reach (20, 20) on the plateau, which is highly efficient.

### Socratic Question 3 (Systematic Testing of Column 3 Row 13 Blockage):
- **Blockage Testing Plan**: Once we enter Safari Zone West (Map 0_219) on Run 30 with our healthy step budget, we will descend the Western Plateau stairs to (6, 20) and walk to Column 3 Row 13 on foot. We will attempt to step Up into Row 13 and log the resulting collision (bump) to provide an indisputable, Turn-numbered, empirical proof that the western corridor is blocked at Row 13. After logging, we will backtrack up the Western Plateau stairs to (6, 18) to resume the correct route. This detour will cost exactly 4 steps extra, which is completely safe for our budget.