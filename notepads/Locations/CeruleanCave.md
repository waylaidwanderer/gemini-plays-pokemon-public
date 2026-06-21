# Cerulean Cave - Verified Records
- Map ID: 0_228 (1F), 0_226 (2F)

## 1F (0_228) Verified Layout:
- **Ladder (24, 17)**: Leads out of Cerulean Cave to Cerulean City.
- **Ladder (21, 11)**: Labeled TYPE_4b8d. One-way dropdown ladder; cannot be used to ascend from 1F.
- **Ladder (23, 7)**: Labeled TYPE_3fe2. Interacting with or stepping onto this tile immediately warps the player to 2F at (22, 6).
- **Ladder (22, 6) [2F]**: Connects back down to 1F at (23, 7).
- **Staircase at (17, 15)**: Labeled TYPE_4b8d. Connects the central platform to the ground floor at (17, 16) (Verified Turn 113127).
- **Wooden Staircase at (1, 13)**: Labeled TYPE_4b8d. Connects the southwestern ground level to the elevated southwest plateau at (1, 12) (Verified Turn 113146).
- **Ramps to Water**:
  - Located at (23, 3), (15, 3), (11, 13), and (25, 9) (TYPE_4b8d).
  - Standing on any of these ramps facing the water and selecting SURF from the party menu successfully mounts the water.
- **Water Canal**: Rows 4 and 5 on 1F are water (TYPE_4e8c) and can be surfed upon. While Rows 4-5 are blocked horizontally at Column 13 by solid rock walls (TYPE_2889), the eastern and western water canal systems are bidirectionally connected via the open water on Rows 6-7, making continuous water navigation fully possible across the entire northern half of 1F. Verified on Turn 112918.
- **Water Canal Boundary at (27, 12) (Verified Turn 112949)**:
  - Attempting to dismount Down from (27, 11) on foot results in a solid collision at (27, 12). This physically proves that (27, 12) is completely impassable.
- **Southern Canal Boundary (Rows 16-17) Systematic Tests**:
  - Turn 113095: Stood at (8, 15) on water and pressed Down to test (8, 16) passability. Result: BUMPED, remaining at (8, 15). Physically proves (8, 16) is a solid, impassable wall.
  - Turn 113098: Stood at (9, 15) on water and pressed Down to test (9, 16) passability. Result: BUMPED, remaining at (9, 15). Physically proves (9, 16) is a solid, impassable wall.
  - Turn 113107: Stood at (10, 15) on water and pressed Down to test (10, 16) passability. Result: BUMPED, remaining at (10, 15). Physically proves (10, 16) is a solid, impassable wall.
  - Turn 113109: Stood at (11, 15) on water and pressed Down to test (11, 16) passability. Result: BUMPED, remaining at (11, 15). Physically proves (11, 16) is a solid, impassable wall.
  - Conclusion: The entire southern boundary of the western canal on Rows 16-17 across Columns 8-11 is a solid, continuous rock wall of TYPE_2889, confirming the canal is indeed a dead end going south. Any horizontal or vertical passage to Row 17 on foot or surfing here is completely impossible.
- **Northern Landmass Layout (Row 0-2 ground-level shortcut)**:
  - Rows 0, 1, and 2 form an unblocked, completely walkable ground-level connection on foot from Column 23 (Water Ramp 1) all the way east to Column 28 (Ladder 2 landing at 27,1). There is NO solid rock barrier on Column 26 on 1F, allowing the player to bypass the 2F serpentine path entirely when navigating from the western water canal to the northeast section of 1F. Verified on Turns 112008-112012.
- **Visual Artifact Note**: Red flower tiles (TYPE_3fe2) (such as at 19, 3) visually resemble red-and-white Poké Balls in the Crystal palette swap but are passable ground tiles with no physical items.

## 2F (0_226) Verified Layout:
- **Serpentine Bypass**:
  - Located at Column 25, Row 9. Bypasses the solid Column 26 rock barrier to allow access to the northeast section of 2F.
- **Ladder 2**:
  - Located at (29, 1) (labeled [=], TYPE_3fe2).
  - To reach it from (29, 3): walk Left to (28, 3), Up 2 steps to (28, 1), and Right to (29, 1). Descending this ladder lands on 1F at (27, 1).
- **Row 11 Passage**:
  - Row 11 forms a completely open, unblocked horizontal passage from Column 18 to Column 24.
- **Row 16 Blockage**:
  - Row 16 contains a solid horizontal rock wall from Column 14 to Column 20, blocking direct downward access from Row 15 to Row 17.
- **Row 9 Blockage**:
  - Row 9 is blocked by rock walls at (22, 9) and (24, 9), so it is not a continuous horizontal corridor.
- **Row 7 Blockage (Verified Turn 113364)**:
  - Row 7 contains a solid horizontal rock wall at (17, 7) of TYPE_2889, physically blocking on-foot horizontal crossover between Column 18 and Column 16. Stood at (18, 7) facing Left, pressed Left, and collided with the wall at (17, 7) with zero coordinate change, proving it is impassable.
- **Topological Goal**:
  - To access the basement (B1F) where Mewtwo is, the player must locate the northwest ladder on 2F. This ladder descends into the isolated northwestern quadrant of 1F, which contains the stairs leading to B1F.
- **(15, 13) Rock Wall Blockage**:
  - Visually appearing as a rock wall but labeled TYPE_3fe2 in some overlays, (15, 13) is an impassable rock wall blocking any direct horizontal transition between Column 14 and Column 15 on Row 13.
- **(16, 13) Rock Wall Blockage (Verified Turns 112374, 112378)**:
  - While labeled as TYPE_3fe2 (open ground) in the visual overlay, (16, 13) is physically a solid, impassable rock wall.
  - Verification: On Turn 112374 and Turn 112378, standing at (17, 13), attempting to walk Left to (16, 13) resulted in zero coordinate change, proving that (16, 13) is impassable.
  - This definitively proves that the eastern section of 2F is blocked from navigating westwards at Row 13. We empirically tested the passability of (13, 11) on Turn 113207 by standing at (12, 11) and pressing Right. This resulted in a direct collision with zero coordinate change, physically proving that (13, 11) is a solid impassable rock wall of TYPE_2889. This definitively proves that 2F East is completely physically disconnected from 2F West on foot, confirming that the only way to navigate between them is to transition via the 1F water canals.

## Topological Connectivity and Progression Path to Mewtwo:
- **B1F Access**: The stairs down to B1F are located in the isolated northwestern quadrant of 1F.
- **Northwest Quadrant of 1F**: This isolated quadrant can ONLY be accessed by descending from 2F via a specific ladder located in the northwestern portion of 2F.
- **Western/Southern Portion of 1F**: Impassable via the western water canal alone. While our empirical testing on Turns 112211-112224 and 112487-112495 proved that the western vertical canal (Columns 8-9) is a dead end on Row 16, Water Ramp 2 at (11, 13) provides an unblocked on-foot bridge. Dismounting at (11, 13), walking north and east to the central platform stairs at (17, 15) (descending to Row 17 on the ground floor), and then walking Left along Row 17 grants full on-foot access to the southwestern portion of 1F and the (3, 11) southwest ladder to 2F West. We empirically verified on Turn 112601 that Column 19 on Row 15 is physically impassable on foot, which definitively proves that the eastern entrance platform of 1F is completely physically isolated on foot from the western/southern portion of 1F. Thus, the only way to reach the western/southern portions of 1F is by climbing up to 2F, crossing over, and descending elsewhere, or via the horizontal water canals to dismount at Water Ramp 2.
- **Accessing Western 2F**: The eastern section of 2F is completely isolated from the western section of 2F on foot. This has been empirically proven by the rock wall blockages at (16, 13) and (13, 11). Thus, we must climb up a different ladder from 1F.
- **Water Canal**: Rows 4 and 5 on 1F contain water but are blocked horizontally at Column 13 by solid rock walls (TYPE_2889). However, this does NOT completely isolate the eastern and western halves of 1F, because we can bypass the Column 13 Row 4-5 blockage by surfing Down on Column 14 to Row 6/7, and then surfing Left through Column 13 Row 6/7 (which is completely open and passable water) to reach the western water canal.
  - *Proof of Work*: On Turn 112858, stood at (14, 5) on the water and pressed Left. Result: Collided, player remained at (14, 5). On Turn 112863, stood at (14, 4) on the water and pressed Left. Result: Collided, player remained at (14, 4). This empirically proves that the canal is blocked at Column 13 on Rows 4-5.
  - *Connection Proof*: On Turn 112818, we discovered that Rows 6 and 7 on Column 13 are completely open, passable water, which we successfully traversed on Turn 113044 and Turn 113066 to surf horizontally between the eastern and western halves of the cave.

- **Ladder 5**:
  - Located on 1F at (7, 1) (labeled TYPE_3fe2). Ascending this ladder warps the player to 2F at (6, 1). This is located in the northwest isolated quadrant of 1F.

- **Ladder 6 (Southwest Ladder)**:
  - Located on 1F at (3, 11) (labeled TYPE_3fe2, marked with 🪜 map marker). Climbing this ladder warps the player to 2F West at (3, 11).
  - Located on 2F West at (3, 11). Descending this ladder warps the player to 1F Southwest at (3, 11).
- **Northwest Ladder (B1F Access)**:
  - Located on 1F at (1, 3) (labeled TYPE_3fe2). Ascending this ladder warps the player to 2F at (1, 3).
  - Located on 2F at (1, 3) (labeled [=], TYPE_3fe2). Descending this ladder warps the player to 1F at (1, 3). This is the critical gateway to the northwest isolated quadrant of 1F and the B1F stairs.
- **Wooden Staircase at (1, 13) on 1F**: Labeled TYPE_4b8d. Connects the southwestern ground level to the elevated plateau of TYPE_2770 at (1, 12).
- **Elevated Southwest Plateau on 1F**: Bounded at Rows 11 and 12, Columns 1 to 6 (TYPE_2770). Walkable on foot, connecting the staircase at (1, 13) to the southwest ladder at (3, 11).
- **(22, 9) Rock Wall Blockage [2F West] (Verified Turn 113224)**: Physically tested on foot by standing at (21, 9) and pressing Right. Result was a direct collision with zero coordinate change, proving that (22, 9) is a solid impassable rock wall of TYPE_2889. This definitively blocks horizontal crossover between Column 21 and Column 23 on Row 9, meaning the southwestern/central pocket (Columns 11-21, Rows 8-13) of 2F West is completely isolated from the main northern corridors of 2F West.
- **2F West Upper-Central Corridor Isolation Empirical Verification**:
  - **Column 2 Row 0-4 Blockage**: Verified on Turn 112893 that Column 2 is a solid rock wall (TYPE_2889) across Rows 0-4, blocking direct horizontal crossover on the north side.
  - **Column 3 Row 4 Blockage**: Empirically tested on Turn 113495. Standing at (3, 3) facing Down, we pressed Down. Result: Collision with zero coordinate change, remaining at (3, 3). This physically proves that (3, 4) is a solid, impassable wall.
  - **Column 8 Row 5 Blockage**: Empirically tested on Turn 113499. Standing at (9, 5) facing Left, we pressed Left. Result: Collision with zero coordinate change, remaining at (9, 5). This physically proves that (8, 5) is a solid, impassable wall.
  - **Column 9 Row 6 Blockage**: Empirically tested on Turn 113503. Standing at (9, 5) facing Down, we pressed Down. Result: Collision with zero coordinate change, remaining at (9, 5). This physically proves that (9, 6) is a solid, impassable wall.
  - **Conclusion**: These rigorous empirical tests mathematically and physically prove that the upper-central corridor of 2F West (Columns 9-14, Rows 1-5) is completely and permanently isolated on foot from the western/southern sections of 2F West. There is no on-foot path between them. Climbing Ladder 5 at (7, 1) on 1F lands us in this closed pocket. Thus, to reach the Northwest Ladder at (1, 3) on 2F West, we must find a different entryway or transition.
- Turn 112959: Tested passability of (25, 12) from (25, 11) by pressing Down. Result: Bumped against (25, 12) (TYPE_2889), player remained at (25, 11). This empirically proves that (25, 12) is completely impassable.
- Turn 112961: Tested passability of (24, 12) from (24, 11) by pressing Down. Result: Bumped against (24, 12) (TYPE_2889), player remained at (24, 11). This empirically proves that (24, 12) is completely impassable.
- Conclusion (Turn 112964): Both (24, 12) and (25, 12) are completely solid rock walls. This definitively proves that the eastern vertical water canal is a closed pocket terminating at Row 11, and does not continue further south to connect with any southern water corridor. Backtracking west is the only mathematically possible option.