# Safari Zone West Exploration Scratchpad (Run 30 Planning & Execution)
- **Current Status**: Standing at (8, 5) in Safari Zone East (Map 0_217) on Turn 59334, with exactly 254 steps remaining.
- **Inventory Status**: 15/20 items. (COMPLETED)
- **Main Objectives**: Retrieve Warden's Gold Teeth at (19, 7) and HM03 Surf at (3, 3) in Safari Zone West.

## Fresh Run 30 Optimal Multi-Map Route Plan (500 Step Budget):
1. **Segment 1: Safari Zone Center (Map 0_220)**
   - Path: Walk Left 1 step to (14, 25), Up 2 steps to (14, 23), Right 14 steps to (28, 23), Up 12 steps to (28, 11), and Right 2 steps to transition to Safari Zone East at (0, 21).
   - Expected Cost: 31 steps.
2. **Segment 2: Safari Zone East (Map 0_217)**
   - Path: Enter at (0, 23) due to Center-to-East Row 11-to-23 offset transition. Walk Down 1 step to Row 24 at (0, 24), Right 20 steps along Row 24 to Column 20 at (20, 24), and Up 4 steps along Column 20, climbing the stairs at (20, 21) to (20, 20) on the plateau. Walk Left 10 steps along Row 20 to the western plateau stairs at (12, 20). Walk Down 2 steps to descend the western plateau stairs at (12, 21), landing on ground level at (12, 22). Walk Left 3 steps along Row 22 to Column 9, and walk North along Column 9 to Row 8. Walk East 3 steps along Row 8 to (12, 8). Climb the northern stairs at (12, 7) to (12, 6) on the high plateau. Walk Right 5 steps to (17, 6) and Down 2 steps to descend the eastern plateau stairs at (17, 7), landing on ground level at (17, 8). Walk East 4 steps to Column 21 on Row 8, and North along Column 21 to Row 3, landing at (21, 3). Walk Left to (0, 5) to transition to Safari Zone North at (39, 31).
   - Expected Cost: 25 steps to plateau + 12 steps to western stairs + 22 steps to northern stairs + 9 steps to eastern stairs + 9 steps to Column 21/Row 3 + 21 steps to transition = ~98 steps.
3. **Segment 3: Safari Zone North (Map 0_218)**
   - Path: Enter at (39, 31). Walk Left 11 steps along Row 31 to (28, 31). Climb plateau stairs UP at (28, 27) onto plateau at (28, 26). Walk across plateau to (34, 16) stairs, descend stairs to (34, 16). Walk around the southern corridor to Column 8/9 on Row 33, then walk Down to transition to Safari Zone West at (27, 0).
   - Expected Cost: ~48 steps.
4. **Segment 4: Safari Zone West (Map 0_219) - The Double Retrieval**
   - Path: Enter at (27, 0). Walk Down 18 steps along Column 27 to (27, 18), Left 6 steps to (21, 18), and Up 2 steps to climb Eastern stairs UP to (21, 16) on the plateau. Walk across plateau to northern descent ramp at (18, 9). Descend/jump down ramp to ground level at (19, 9). Walk Up 2 steps to stand at (19, 7) and press A to retrieve Warden's Gold Teeth. Walk Left 16 steps along Row 7 to Column 3 at (3, 7) and Up 4 steps to (3, 3) to enter the Secret House. Talk to the NPC to receive HM03 Surf. Use BLASTOISE's DIG to escape back to Fuchsia City outside the Pokémon Center.
   - Expected Cost: ~40 steps.

## Run 30 Chronological Movement Log:
- Turn 59053: Dialogue cleared, Safari Game Run 29 ended.
- Turn 59064: Entered Safari Zone Center (Map 0_220) at (15, 25) with exactly 500 steps remaining.
- Turn 59121: Reached (29, 11) in Safari Zone Center [472 steps remaining].
- Turn 59125: Transitioned to Safari Zone East (Map 0_217) at (0, 23) [430 steps remaining].
- Turn 59137: Walked to (0, 24) [429 steps remaining].
- Turn 59149: Walked to (20, 24) [409 steps remaining].
- Turn 59154: Climbed stairs to (20, 20) on plateau [405 steps remaining].
- Turn 59169: Walked to (22, 13) [396 steps remaining].
- Turn 59172: Walked to (24, 13) [394 steps remaining].
- Turn 59177: Descended stairs to (24, 16) [391 steps remaining].
- Turn 59187: Climbed stairs back to (24, 14) [389 steps remaining].
- Turn 59198: Walked to (20, 13) on plateau [384 steps remaining].
- Turn 59228: Descended stairs to (24, 16) [377 steps remaining].
- Turn 59234: Walked to (28, 20) [369 steps remaining].
- Turn 59242: Walked to (28, 24) [365 steps remaining].
- Turn 59247: Backtracked to (28, 16) [357 steps remaining].
- Turn 59254: Walked back down to (28, 24) [349 steps remaining].
- Turn 59256: Walked Left to (24, 24) [345 steps remaining].
- Turn 59262: Walked Left to (20, 24) [341 steps remaining].
- Turn 59264: Climbed stairs to (20, 20) on plateau [337 steps remaining].
- Turn 59266: Walked to (22, 12) on plateau [327 steps remaining].
- Turn 59276: Walked Down to (22, 20) on plateau [319 steps remaining].
- Turn 59287: Walked Left to (12, 20) on plateau [309 steps remaining].
- Turn 59290: Descended stairs to (12, 22) on ground level [307 steps remaining].

## Answers to Socratic Questions:
### Socratic Question 1 (Tracking Latency):
- **Why tracking latency accumulates**: Coordinate and step budget tracking latency accumulates because after executing large overworld movement sequences, we prioritize immediate route planning and forget to systematically execute our tracking tools. This delay allows desyncs to build up in our context.
- **Strict Turn-by-Turn Routine**:
  1. Immediately following any overworld movement sequence, warp, or map transition, the VERY FIRST action on the next turn MUST be calling 'safari_navigator_agent' to calibrate the step budget.
  2. We must then immediately perform a 'notepad_edit' to update both the top status block and chronological log in 'Scratchpad/SafariZone_West_Route' during the same turn before taking any more overworld steps.

### Socratic Question 2 (Cognitive Dissonance & Eastern Ground Passage Blockage):
- **Cognitive Dissonance Explanation**: The cognitive dissonance arose because we held a historical, generalized assumption that the ground corridor along Columns 20-22 was open from South to North. However, our empirical foot-testing on Turn 59257 proved that Columns 21 and 22 are completely blocked at Row 21 by solid cliff walls of TYPE_2889. Since this corridor is impassable from South to North, walking North from the southern ground level to Row 3 is physically impossible.
- **Correct Plateau-Traversal Route**:
  1. From our current position (12, 22) on ground level, walk Left 3 steps along Row 22 to (9, 22), and North along Column 9 to Row 8.
  2. Walk East 3 steps along Row 8 to (12, 8), and climb the northern stairs at (12, 7) to (12, 6) on the high plateau.
  3. Walk Right 5 steps across the plateau to (17, 6) and Down 2 steps to descend the eastern plateau stairs at (17, 7) to ground level at (17, 8).
  4. From (17, 8), walk East 4 steps to Column 21 and North along Column 21 to Row 3, landing at (21, 3).
  5. Walk Left to (0, 5) to transition to Safari Zone North (Map 0_218) at (39, 31).

### Socratic Question 3 (Systematic SW Quadrant Blockage Test in West):
- **Systematic SW Quadrant Blockage Test Plan**: Once we transition to Safari Zone West (Map 0_219), we will descend the Western Plateau stairs to (6, 20) and walk to Column 3 Row 13 on foot. We will attempt to step Up into Row 13 and log the resulting collision (bump) to provide an indisputable, Turn-numbered, empirical proof that the western corridor is blocked at Row 13. After logging, we will backtrack up the Western Plateau stairs to (6, 18) to resume the correct route. This detour will cost exactly 4 steps extra, which is completely safe for our budget.
- **Logs to Record**: We will record the exact turn numbers, coordinates, and visual output/collisions of this test inside `Locations/SafariZone_West` to satisfy the Burden of Proof.