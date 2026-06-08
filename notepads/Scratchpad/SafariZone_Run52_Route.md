# Safari Zone Exploration - Run 52 (Turn 73099 - Active)
- Current Status: Standing at (2, 17) [z=0] inside Safari Zone West (Map 0_219) on Turn 73099, facing UP with exactly 161 remaining steps in RAM.
- Inventory Status: 15/20 items, 30 Safari Balls.

## Master Run 52 Campaign Plan & Route (The Ultimate Double Retrieval)

### 3. Safari Zone North Traversal [45 steps] (Completed)
- Completed the entire Northern crossover segment in exactly 45 overworld steps, transitioning to Safari Zone West on Turn 73043.

### 4. Safari Zone West Traversal [90 steps total to Secret House] (In Progress)
- Walk Down 18 to (27, 18) -> 18 steps (Completed, Turn 73048).
- Walk Left 6 to (21, 18) -> 6 steps (Completed, Turn 73052).
- Climb Eastern stairs: Up 2 to (21, 16) [z=1] -> 2 steps (Completed, Turn 73059).
- Traverse bridge to (16, 16): Left 5 [z=1] -> 5 steps (Completed, Turn 73059).
- Move to (16, 8): Up 7 [z=1], bumped on sideways jump candidate, stepped Up 1 to (16, 8) [z=1] -> 8 steps (Completed, Turn 73065).
- Walk Down to Koga's bridge crossover: Down 8 steps to (16, 16) [z=1] -> 8 steps (Completed, Turn 73072).
- Walk to (19, 15): Right 1 to (17, 16) [z=1], Up 2 to (17, 14) [z=1], bumped 9 times at (17, 13) [z=0] cliff wall, Right 2 to (19, 14) [z=1], Down 1 to (19, 15) [z=1] -> 6 steps (Completed, Turn 73073).
- Backtrack to Western stairs: Left 3 steps along Row 15 to (16, 15) [z=1], Down 1 to (16, 16) [z=1], Left 10 along Row 16 bridge to (6, 16) [z=1], and Down 3 to stairs top at (6, 19) [z=1] -> 17 steps.
- Descend Western stairs to ground: Down 1 step to (6, 20) [z=0] -> 1 step.
- Walk Southwest ground corridor to (2, 14) [z=0]: Left 4 steps along Row 20 to (2, 20) -> 4 steps. Up 6 steps along Column 2 to (2, 14) -> 6 steps.
- Walk to (10, 14) [z=0]: Right 8 steps along Row 14 -> 8 steps.
- Bypass Rest House 3 to (10, 10) [z=0]: Right 3 steps to (13, 14) -> 3 steps. Up 4 steps along Column 13 to (13, 10) -> 4 steps. Left 3 steps to (10, 10) -> 3 steps.
- Climb Western-West Plateau: Up 1 step to climb stairs at (10, 9) and reach (10, 8) [z=1] -> 2 steps.
- Jump West (Left) over Column 4 ledge: Left 6 steps along Row 8 on plateau to (4, 8) -> 6 steps. Left 1 step to jump West to (3, 8) [z=0] in Northwest quadrant -> 1 step.
- Retrieve Gold Teeth: Up 1 to (3, 7) -> 1 step. Right 15 along Row 7 to stand adjacent to Teeth Pokéball at (19, 7) [standing at (18, 7) facing Right or (19, 8) facing Up/(19, 6) facing Down] -> 15 steps. Collect with 'A' -> 0 steps.
- Walk to enter Secret House: Walk Left 15 steps along Row 7 back to (3, 7) -> 15 steps. Walk Up 4 steps along Column 3 to enter Secret House at (3, 3) -> 4 steps.
- Obtain Surf!

## Backtrack Route Step-by-Step Step-Budget Math:
- Starting steps at (19, 15) [z=1]: **186 steps**.
- Backtrack to stairs top at (6, 19) [z=1]: 186 - 17 = **169 steps remaining**.
- Descend stairs to ground level at (6, 20) [z=0]: 169 - 1 = **168 steps remaining**.
- Reach (2, 14) [z=0] Southwest corridor: 168 - 10 = **158 steps remaining**.
- Reach (10, 14) [z=0]: 158 - 8 = **150 steps remaining**.
- Bypass Rest House 3 to (10, 10) [z=0]: 150 - 10 = **140 steps remaining**.
- Climb Western-West Plateau & jump West over Column 4 to (3, 8) [z=0]: 140 - 9 = **131 steps remaining**.
- Retrieve Gold Teeth at (19, 7) and stand back at (3, 7) [z=0]: 131 - 31 = **100 steps remaining**.
- Enter Secret House at (3, 3) [z=0]: 100 - 4 = **96 steps remaining** inside the Secret House!
- Safety margin inside the Secret House: **96 steps remaining** (plenty of headroom!).

## Verification of Koga's Ground-Level Bridge Blockage:
- Koga's bridge (Row 16, Columns 5-22) is elevated at plateau level z=1. At ground level z=0, the bridge structure acts as a solid vertical wall.
- Our permanent records in 'Locations/SafariZone_West' confirm:
  "Standing at (12, 20), walking Up results in collision against a solid tree wall of TYPE_2889 at (12, 19). Standing at (17, 20), walking Right is blocked by a solid tree wall of TYPE_2889 at (18, 20)... This physically proves that Column 18 is a solid tree wall on Rows 20-23, and Row 19 is a solid tree wall from Column 8 to Column 17... making the southwest quadrant a completely closed ground pocket on foot. Traversing the plateau is 100% mandatory."
- Therefore, there is zero direct vertical traversal on ground level under Koga's bridge. We must navigate the ground corridor: Left 4, Up 6, and Right 8 steps to reach Column 10 on Row 14.