# Pokémon Mansion B1F Basement Exploration Records

## Switch & Gate States (Under active State B)
- **Active State**: State A is active. Toggled functional Mewtwo Statue at (24, 3) to active State A on Turn 93901, opening Northwest Gate (9, 7) and Gate (16, 16)-(17, 16) while closing Center Gate (13, 22) and East Gate (26, 17).
- **Starting Coordinates**: (23, 22) - landing tile from 1F Southeast stairs.
- **Observed Landmarks**:
  - Column 20: Thick solid vertical partition wall of TYPE_2889 extending from Row 18 to at least Row 26.
  - Column 29: Thick solid vertical partition wall of TYPE_2889 on Rows 18-26.
  - Left Side (Column 19): Contains an item ball (TM14 - Blizzard) at (19, 25) [Collected on Turn 93157].
  - Column 28 Corridor: Completely open and passable floor of TYPE_3fe2 from Row 18 to Row 26.
- **Exploration Log**:
  - **Turn 92928**: Arrived on B1F at (23, 22) from the 1F Southeast stairs.
  - **Turn 92936**: Walked Right to (28, 22) to inspect the eastern boundary.
  - **Turn 92944**: Verified Column 29 is solid wall.
## Exploration log (continued)
- **Turn 92951**: Starting systematic exploration of B1F from (28, 26).
- **Turn 92964**: Arrived at (17, 14) facing Left. From here, we see that the floor to the left is open.
  - (16, 14): TYPE_3fe2
  - (15, 14): TYPE_3fe2
  - (14, 14): TYPE_3fe2
  - (13, 14): TYPE_3fe2
  - (13, 15): TYPE_3fe2
  - Below Row 15, there are partition blocks of TYPE_2889 (solid columns/specimen tanks/tables):
    - (13, 16)-(13, 18): TYPE_2889 (vertical wall)
    - (14, 16)-(14, 17): TYPE_2889 (specimen tank)
    - (15, 16)-(15, 17): TYPE_2889 (specimen tank)
    - (18, 16)-(18, 17): TYPE_2889 (specimen tank)
    - (19, 16)-(19, 17): TYPE_2889 (specimen tank)
    - (20, 16)-(20, 18): TYPE_2889 (vertical wall of Column 20, which has its opening on Row 14/15)
  - Rows 16 and 17 on Column 16 and 17 are open floor (TYPE_3fe2), forming a vertical walkway between the specimen tanks!
    - (16, 16), (16, 17) are TYPE_3fe2
    - (17, 16), (17, 17) are TYPE_3fe2
  - There is a bottom horizontal hallway on Row 18:
    - (14, 18) to (19, 18) are TYPE_3fe2
- **Turn 93016**: Reached the southwest corner of B1F at (1, 26).
  - Row 27 is completely solid wall (TYPE_2889) across Columns 0-6.
  - Column 0 is solid vertical wall (TYPE_2889) from Row 22 to 26.
  - The southwest section is a large rectangular room with clear, passable floor (TYPE_3fe2) spanning Columns 1 to 7 and Rows 18 to 26.
  - No items or switch statues are present in this southwest quadrant.
  - The overworld item at (1, 22) (originally visually appearing as a Pokéball) was interacted with on Turn 92998 by pressing A while standing at (2, 22) facing Left. The sprite vanished, confirming the interaction registered. However, our inventory remained completely unchanged at 13 items with identical quantities. Since unmodded Red/Blue has no overworld item ball at this location, this is confirmed as a decorative/unloaded sprite or visual artifact rather than a true item drop.

## Active Hypotheses & Strategic Notes:
- **Northwest Room Access**: The northwest room (Columns 1-8, Rows 10-17) is currently blocked under active State A. However, we hypothesize that the 'solid wall' at Column 9 (Rows 14-16) contains a closed gate of TYPE_2889 that will open and become passable of TYPE_3fe2 when the global gate switch is toggled to State B. We must find a Mewtwo Statue on B1F (or use one on an upper floor if reachable, though B1F is preferred) to toggle to State B and test this hypothesis.
- **Turn 93081**: Located at (22, 10) facing Up. We see a Burglar NPC sprite at (27, 11) on the eastern side.
- **Turn 93132**: Walked from (10, 14) Right 6 steps to (16, 14) on Row 14 to bypass the Column 13 wall.

## Precise Walkthrough Path to TM14 Blizzard (Turn 93147 Audit)
- **Starting Position**: (8, 18) facing Down.
- **Active State**: State A (Default).
- **Item Ball (TM14 - Blizzard)**: (19, 25).
- **Walkable Route Proof of Work**:
  1. Stand at (8, 18) facing Down. Walk Right 2 steps to (10, 18) (all tiles are TYPE_3fe2).
  2. Walk Up 4 steps to (10, 14) (all tiles are TYPE_3fe2).
  3. Walk Right 6 steps to (16, 14) (this bypasses the solid Column 13 partition wall at Row 14, where (13, 14) is open floor of TYPE_3fe2).
  4. Walk Down 4 steps to (16, 18) (this travels through the open vertical walkway on Column 16, which is completely open of TYPE_3fe2 between the solid specimen tanks).
  5. Walk Right 3 steps to (19, 18) (all tiles are open floor of TYPE_3fe2).
  6. Walk Down 7 steps to (19, 25) (Column 19 contains no closed gates, walls, or obstacles between Row 18 and Row 25 under State A, making this path completely open on foot to retrieve the TM14 - Blizzard item ball).

- **Turn 93181**: Currently standing at (14, 22) facing Down. Toggling State B closed the gate at (16, 16)-(17, 16). We are executing a foot detour: walking Left 2 steps to cross Column 13 at Row 22 (13, 22) (which is open of TYPE_3fe2), then walking Up 8 steps to reach the western hallway at (12, 14).

## Systematic Passability Audit of Column 9 Gate under State B (Turn 93207)
- **Objective**: Systematically test and document the physical passability of Column 9 Rows 14, 15, and 16 under active State B.
- **Test 1 (Row 14)**:
  - **Turn 93206**: Stood at (10, 14) facing Left under active State B. Pressed Left to attempt to step onto (9, 14).
  - **Result**: Direct collision bump (0 tiles visited), remaining at (10, 14) on Turn 93207 facing Left.
  - **Conclusion**: Column 9 Row 14 is 100% solid and CLOSED/impassable under active State B.
- **Turn 93210**: Confirmed Column 9 Row 14 is solid wall under State B. Navigated south to Row 18, then west to Column 1 to test the west gate at (1, 17) under active State B, proving it is closed.
- **Turn 93253**: Successfully interacted with the Mewtwo Statue at (18, 25) to toggle the global gate state back to **State A**.
- **Turn 93263**: Moved Left to (17, 26) to bypass the NPC at (16, 23).
- **Turn 93311**: Standing at (10, 14) facing Left under active **State A**. Pressed Left to test the passability of (9, 14) on foot.
  - **Result**: Direct collision bump (0 tiles visited), remaining at (10, 14).
  - **Conclusion**: Column 9 Row 14 is 100% solid and CLOSED/impassable under active State A as well. It is a permanent wall structure under both states.
- **Turn 93340**: Currently at (1, 18) facing Down under active State A.
- **Turn 93341**: Pressed Up to face and step into (1, 17) under active State A.
  - **Result**: Direct collision bump, remaining at (1, 18).
  - **Conclusion**: The west gate at (1, 17) is 100% CLOSED and impassable under active State A.
- **Turn 93353**: Standing at (12, 22) facing Up under active State A. Directly in front of us at (13, 22) is a yellow and black striped vertical bar structure of TYPE_a83b.
- **Turn 93354**: Pressed Right to face and step into (13, 22) under active State A.
  - **Result**: Direct collision bump (0 tiles visited), remaining at (12, 22) but facing Right.
  - **Conclusion**: The Column 13 gate at (13, 22) and (13, 23) is CLOSED and impassable under active State A.
- **Turn 93398**: Currently standing at (1, 18) facing Up under active **State B**. Directly above us at (1, 17) is the west gate of TYPE_2889.
- **Turn 93399**: Pressed Up to face and step into (1, 17) under active State B.
  - **Result**: Direct collision bump, remaining at (1, 18) facing Up.
  - **Conclusion**: The west gate at (1, 17) is 100% CLOSED and impassable under active State B. Along with Turn 93341 (CLOSED under State A), this proves the Row 17 West Gate is closed under BOTH global states on foot.
- **Turn 93428**: Standing at (10, 22) facing Down under active State B. Our target is the eastern room's open Gate 26/27 at (26, 17)-(27, 17).

## Systematic Passability Protocol of Column 9 on Rows 11, 12, 13 under active State B
- **Objective**: Determine if there is an open gate/passable tile on Column 9 at Rows 11, 12, or 13 under active State B, which would grant access to the northwest compartment containing the Secret Key.
- **Methodology**:
  1. Navigate north along Column 26 to check the northern compartments of B1F East.
  2. Find the horizontal crossover that allows us to walk west across Column 25 and Column 20 in the northern section (Rows 1-9).
  3. Reach the central corridor (Column 10/11) on Rows 11-13.
  4. Walk to Column 10 and face Left.
  5. Attempt to step Left onto Column 9 for each of the three candidate rows (11, 12, 13) and document if we bump (CLOSED) or walk through (OPEN).
- **Turn 93385**: Verified that the Column 13 gate at (13, 22) is OPEN under active State B by walking left through it.
- **Turn 93446**: Verified that the B1F-East gate at (26, 17)-(27, 17) is OPEN under active State B by walking up through it.
- **Turn 93461**: Currently standing at (10, 7) facing Left under active **State B**. Directly to our left at (9, 7) is the vertical gate of TYPE_a83b.
- **Turn 93462**: Pressed Left to test the gate at (9, 7) under active State B. Result: Bump, remaining at (10, 7). This physically proves that (9, 7) is CLOSED/impassable under active State B.
- **Turn 93514**: Arrived at (10, 13) facing Up under active State B.
- **Turn 93516**: Pressed Left to test (9, 13) under active State B. Result: Bump, remaining at (10, 13). This physically proves Column 9 Row 13 is CLOSED/impassable under active State B.
- **Turn 93519**: Arrived at (10, 12) facing Up under active State B.
- **Turn 93522**: Pressed Left to test (9, 12) under active State B. Result: Bump, remaining at (10, 12) facing Left. This physically proves Column 9 Row 12 is CLOSED/impassable under active State B.
- **Turn 93524**: Pressed Left to test (9, 11) under active State B. Result: Bump, remaining at (10, 11) facing Left (subsequently turned Down on Turn 93527). This physically proves Column 9 Row 11 is CLOSED/impassable under active State B. All candidate rows (11, 12, 13) on Column 9 are confirmed CLOSED under active State B on foot.
## Route back to West B1F under Active State A (Turn 93634)
- **Objective**: Navigate back to B1F West to access the newly opened West Gate at (1, 17) and retrieve the Secret Key.
- **Current Position**: (17, 22), facing Up.
- **Active State**: State A.
- **Routing Constraints & Obstacles**:
  - Center Gate at (13, 22)-(13, 23) is now CLOSED under State A. We cannot walk Left through Row 22.
  - The table at (16, 20)-(17, 21) is solid rubble of TYPE_2889 and blocks Column 16 and Column 17 on Rows 20 and 21. We must detour around it to go north.
  - Specimen tanks of TYPE_2889 block Columns 14, 15, 18, 19 on Rows 16 and 17.
  - The walkway at Columns 16 and 17 on Rows 16 and 17 is completely open.
- **Detoured Zig-Zag Path**:
  1. We are at (17, 22). Move Right 1 step to (18, 22) to bypass the table.
  2. Move Up 4 steps to (18, 18) (Row 18 is open all the way).
  3. Move Left 1 step to (17, 18) (aligning with the open walkway on Column 17).
  4. Move Up 4 steps to (17, 14) (Row 14 is open).
  5. Move Left to reach B1F West. From (17, 14), we can walk Left to Column 8 or 10, then Down to Row 18.
  6. Test the true B1F-Northwest Gate at Column 9 Row 7 (open under State A).

- **Systematic West Wall State A Test (Turn 93674)**: Completed. All columns (1-7) on Row 17 are 100% impassable under active State A on foot.
## B1F Basement Master Walkthrough Plan (Turn 93791) - Corrected for State B
- **Problem**: Under active State B, the gate at (16, 16)-(17, 16) is CLOSED, blocking Column 17. The Northwest Gate at (9, 7) is CLOSED.
- **Solution Route to B1F East North under active State B**:
  1. From (18, 26), walk Left 1 to (17, 26) and Up 4 to (17, 22).
  2. Walk Left 5 along Row 22 to (12, 22) (crosses open B1F-Center Gate at (13, 22)-(13, 23)).
  3. Walk Up 8 along Column 12 to (12, 14).
  4. Walk Right 9 along Row 14 to (21, 14) (crosses the Column 20 opening at (20, 14)).
  5. Walk Down 8 along Column 21 to (21, 22) (east side of Column 20).
  6. Walk Right 5 along Row 22 to (26, 22) (reaches B1F East South).
  7. Walk Up 5 along Column 26 to (26, 17) (inside open B1F-East Gate at (26, 17)-(27, 17)).
  8. Walk Up through B1F-East Gate to (26, 7) (reaches B1F East North!).
  9. Walk north to Row 7, then west to the northeast room.
  10. Locate the Mewtwo Statue in the northeast room (B1F East North) and toggle it to active State A.
  11. Now that State A is active, the Northwest Gate at (9, 7) is OPEN.
  12. Walk west along Row 7, pass through (9, 7) into the Northwest Room, and retrieve the Secret Key!
  13. Use an Escape Rope to exit the Mansion instantly.