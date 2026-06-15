# Pokémon Mansion B1F Basement Exploration Records

## Switch & Gate States (Under active State A)
- **Active State**: State A (Default) is active.
- **Starting Coordinates**: (23, 22) - landing tile from 1F Southeast stairs.
- **Observed Landmarks**:
  - Column 20: Thick solid vertical partition wall of TYPE_2889 extending from Row 18 to at least Row 26.
  - Column 29: Thick solid vertical partition wall of TYPE_2889 on Rows 18-26.
  - Left Side (Column 19): Contains an item ball at (19, 25).
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
- **Turn 93081**: Located at (22, 10) facing Up. We see a Burglar NPC sprite at (27, 11) on the eastern side. We plan to walk Down to Row 15, then Right to Column 27, and then Up to interact with the Burglar and explore the eastern pocket.