# Pokémon Mansion B1F Basement Exploration Records

## Switch & Gate States (Under active State A)
- **Active State**: State A (Default) is active.
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

## Precise Walkthrough Path to Secret Key (Turn 93147 Audit)
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
- **Turn 93263**: Moved Left to (17, 26) to bypass the NPC at (16, 23) and begin walking north to the west side to test the Row 17 gate at (1, 17) under State A.
- **Turn 93311**: Standing at (10, 14) facing Left under active **State A**. Pressed Left to test the passability of (9, 14) on foot.
  - **Result**: Direct collision bump (0 tiles visited), remaining at (10, 14).
  - **Conclusion**: Column 9 Row 14 is 100% solid and CLOSED/impassable under active State A as well. It is a permanent wall structure under both states.
- **Turn 93340**: Currently at (1, 18) facing Down under active State A. We will press Up to face and test the passability of (1, 17) under active State A.
- **Turn 93341**: Pressed Up to face and step into (1, 17) under active State A.
  - **Result**: Direct collision bump, remaining at (1, 18).
  - **Conclusion**: The west gate at (1, 17) is 100% CLOSED and impassable under active State A.
- **Turn 93353**: Standing at (12, 22) facing Up under active State A. Directly in front of us at (13, 22) is a yellow and black striped vertical bar structure of TYPE_a83b. We will press Right to face and test the passability of (13, 22) under active State A.