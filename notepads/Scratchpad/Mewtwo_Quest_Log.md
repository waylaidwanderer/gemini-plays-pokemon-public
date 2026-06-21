# Mewtwo Quest Log (Post-Game)
- Started: Turn 111394
- Goal: Enter Cerulean Cave and catch Mewtwo.

## Current status & Progression
- Exploring the southwest 1F elevated plateau on foot.

## 2F Exploration Discoveries & Pathing Notes
- Turn 112555: Tested passability of (8, 5) on 2F West. Stood at (9, 5) and pressed Left. Result: Did not change coordinates, received "pressed 1 movement buttons, but visited 0 tiles" system warning. Conclusion: (8, 5) is definitively an impassable rock wall, proving that the Lower Band (Rows 5-7) on the west cannot be accessed from Column 9 on Row 5 on foot.
- Turn 112601: Empirically tested Column 19 passability on foot from the east on 1F. Stood at (20, 15) facing Left, pressed Left to walk onto (19, 15). Result: Coordinate remained (20, 15), received bump warning. This definitively proves that Column 19 is impassable on foot at Row 15. Combined with visual confirmation of solid rock walls (TYPE_2889) on Column 19 from Row 11 down to Row 18, the eastern entrance platform of 1F is indeed completely physically isolated on foot from the western/southern portion of 1F.

- Turn 112986: Discovered that Row 5 contains water across Columns 21-25, blocking on-foot horizontal crossover from Water Ramp 3 at (25, 9) to Ladder 2 at (27, 1) directly. To access Ladder 2 (which sits on the northern landmass at Rows 0-2), we must use Water Ramp 1 at (23, 3) because it lands directly on Row 3/2, which connects horizontally to Column 27 on Rows 0-2!
- Turn 113013: Discovered that on 2F East, we are completely blocked on the small island around (22, 6) and cannot reach Ladder 3 at (19, 7) because of solid rock walls (TYPE_2889) at (23, 6) and (21, 6). The only passable direction from (22, 6) is Down to (22, 7) then Right to (23, 7) (which is the ladder we came from). So we must backtrack down the ladder at (22, 6) / (23, 7) back to 1F.
- Turn 113076: Discovered that (7, 13) is a 1x1 on-foot pocket, and (8, 13) is a water tile, meaning we can use Surf to enter the water. We must turn to face Right (towards the water) to execute Surf.
- Turn 113127: Discovered a staircase descent at (17, 15) connecting the central-western land platform (X=11..17, Y=9..14, z=1) to the lower cavern floor (Y=16..17, z=0). We descended onto the lower cavern floor at (17, 16) and walked to (16, 17) to begin exploring the southwest on-foot corridor. This opens up a massive unvisited search space on the ground!
- Turn 113149: Standing at (1, 13) in Map 0_228 (Cerulean Cave 1F) facing Up. The tile at (1, 13) is TYPE_4b8d and didn't warp us to 2F.
  - Looking at the screen, we see that the water in this southwest canal is of TYPE_2770, which is a light-purplish-blue color with a ripple pattern.
  - The tile at (3, 11) is a ladder graphic [=] labeled as TYPE_3fe2 (passable ground), sitting on the edge of the water canal.
  - Hypothesis: (1, 13) is a water ramp of TYPE_4b8d. By using Surf facing Up, we can mount the water at (1, 12) (TYPE_2770) and navigate the canal to reach the ladder at (3, 11).
  - Test Plan:
    1. Select POKéMON from the Start Menu, choose GEMMY, and select SURF to try and enter the water at (1, 12).
    2. If successful, navigate the water to (3, 12), then face Up to land on (3, 11) and see if we can transition.
- Turn 113204: Standing at (15, 9) on 2F West. We plan to test the passability of (13, 11) (currently labeled TYPE_2889) to resolve the outstanding hypothesis about 2F East and 2F West connectivity.
  - **Test Plan**:
    1. Navigate from (15, 9) to (12, 11) via the unblocked flat-ground path: Up to (15, 8), Left to (14, 8), Left to (13, 8), Down to (13, 9), Left to (12, 9), Down to (12, 10), Down to (12, 11).
    2. From (12, 11), press Right to attempt to step onto (13, 11).
    3. Verify if we collide (bump), physically proving (13, 11) is indeed an impassable rock wall blockage.