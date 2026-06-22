# Cerulean Cave - Verified Records
- Quest Started: Turn 111394 on Sunday, June 21, 2026 at 9:15 PM PDT
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
- **(13, 7) Blockage (Verified Turn 113646)**:
  - Standing at (13, 6) facing Down, pressed Down. Result: Bumped against (13, 7) (TYPE_2889), proving it is a solid impassable rock wall on 2F West.
- **(16, 8) Blockage (Verified Turn 113874)**:
  - Standing at (16, 7) facing Down, pressed Down. Result: Bumped against (16, 8) (TYPE_2889), proving Column 16 is blocked at Row 8 on 2F West.
- **Topological Goal**:
  - To access the basement (B1F) where Mewtwo is, the player must locate the northwest ladder on 2F. This ladder descends into the isolated northwestern quadrant of 1F, which contains the stairs leading to B1F.
- **(15, 13) Rock Wall Blockage**:
  - Visually appearing as a rock wall but labeled TYPE_3fe2 in some overlays, (15, 13) is an impassable rock wall blocking any direct horizontal transition between Column 14 and Column 15 on Row 13.
- **(16, 13) Rock Wall Blockage (Verified Turns 112374, 112378)**:
  - While labeled as TYPE_3fe2 (open ground) in the visual overlay, (16, 13) is physically a solid, impassable rock wall.
  - Verification: On Turn 112374 and Turn 112378, standing at (17, 13), attempting to walk Left to (16, 13) resulted in zero coordinate change, proving that (16, 13) is impassable.
  - This definitively proves that the eastern section of 2F is blocked from navigating westwards at Row 13. We empirically tested the passability of (13, 11) on Turn 113207 by standing at (12, 11) and pressing Right. This resulted in a direct collision with zero coordinate change, physically proving that (13, 11) is a solid impassable rock wall of TYPE_2889. This definitively proves that 2F East is completely physically disconnected from 2F West on foot, confirming that the only way to navigate between them is to transition via the 1F water canals.

## Topological Connectivity and Progression Path to Mewtwo:
- **B1F Access**: The stairs down to B1F are located in the northwestern quadrant of 1F.
- **Northwest Quadrant of 1F**: This isolated quadrant can ONLY be accessed by descending from 2F via the Northwest Ladder at (1, 3). We have empirically verified that Column 4 Row 1 (4, 1), Column 4 Row 2 (4, 2), and Column 5 Row 3 (5, 3) are completely blocked by solid rock walls of TYPE_2889, physically and mathematically proving that the northwestern quadrant of 1F is completely isolated on foot from the rest of 1F.
- **Western/Southern Portion of 1F**: Impassable via the western water canal alone. While our empirical testing on Turns 112211-112224 and 112487-112495 proved that the western vertical canal (Columns 8-9) is a dead end on Row 16, Water Ramp 2 at (11, 13) provides an unblocked on-foot bridge. Dismounting at (11, 13), walking north and east to the central platform stairs at (17, 15) (descending to Row 17 on the ground floor), and then walking Left along Row 17 grants full on-foot access to the southwestern portion of 1F and the (3, 11) southwest ladder to 2F West. We empirically verified on Turn 112601 that Column 19 on Row 15 is physically impassable on foot, which definitively proves that the eastern entrance platform of 1F is completely physically isolated on foot from the western/southern portion of 1F. Thus, the only way to reach the western/southern portions of 1F is by climbing up to 2F, crossing over, and descending elsewhere, or via the horizontal water canals to dismount at Water Ramp 2.
- **Accessing Western 2F**: The eastern section of 2F is completely isolated from the western section of 2F on foot. This has been empirically proven by the rock wall blockages at (16, 13) and (13, 11). Thus, we must climb up a different ladder from 1F.
- **Water Canal**: Rows 4 and 5 on 1F contain water but are blocked horizontally at Column 13 by solid rock walls (TYPE_2889). However, this does NOT completely isolate the eastern and western halves of 1F, because we can bypass the Column 13 Row 4-5 blockage by surfing Down on Column 14 to Row 6/7, and then surfing Left through Column 13 Row 6/7 (which is completely open and passable water) to reach the western water canal.
  - *Proof of Work*: On Turn 112858, stood at (14, 5) on the water and pressed Left. Result: Collided, player remained at (14, 5). On Turn 112863, stood at (14, 4) on the water and pressed Left. Result: Collided, player remained at (14, 4). This empirically proves that the canal is blocked at Column 13 on Rows 4-5.
  - *Connection Proof*: On Turn 112818, we discovered that Rows 6 and 7 on Column 13 are completely open, passable water, which we successfully traversed on Turn 113044 and Turn 113066 to surf horizontally between the eastern and western halves of the cave.

  - **Ladder 5**:
  - Located on 1F at (7, 1) (labeled TYPE_3fe2). Ascending this ladder warps the player to 2F at (9, 1). This is located in the northwest isolated quadrant of 1F.

- **Ladder 6 (Southwest Ladder)**:
  - Located on 1F at (3, 11) (labeled TYPE_3fe2, marked with 🪜 map marker). Climbing this ladder warps the player to 2F West at (3, 11).
  - Located on 2F West at (3, 11). Descending this ladder warps the player to 1F Southwest at (3, 11).
- **Northwest Ladder (B1F Access)**:
  - Located on 1F at (1, 3) (labeled TYPE_3fe2). Ascending this ladder warps the player to 2F at (1, 3).
  - Located on 2F at (1, 3) (labeled [=], TYPE_3fe2). Descending this ladder warps the player to 1F at (1, 3). This is the critical gateway to the northwest isolated quadrant of 1F and the B1F stairs.
- **Wooden Staircase at (1, 13) on 1F**: Labeled TYPE_4b8d. Connects the southwestern ground level to the elevated plateau of TYPE_2770 at (1, 12).
- **Elevated Southwest Plateau on 1F**: Bounded at Rows 11 and 12, Columns 1 to 6 (TYPE_2770). Walkable on foot, connecting the staircase at (1, 13) to the southwest ladder at (3, 11).
- **(22, 9) Rock Wall Blockage [2F West] (Verified Turn 113224)**: Physically tested on foot by standing at (21, 9) and pressing Right. Result was a direct collision with zero coordinate change, proving that (22, 9) is a solid impassable rock wall of TYPE_2889. This definitively blocks horizontal crossover between Column 21 and Column 23 on Row 9, meaning the southwestern/central pocket (Columns 11-21, Rows 8-13) of 2F West is completely isolated from the main northern corridors of 2F West.
- **Row 8 Rock Wall Blockages [2F West]**:
  - **Column 3 Row 8 (Verified Turn 113985)**: Stood at (3, 9) facing Up, pressed Up. Result: Collision bump.
  - **Column 4 Row 8 (Verified Turn 115147)**: Stood at (4, 9) facing Up, pressed Up. Result: Collision bump.
  - **Column 5 Row 8 (Verified Turn 115151)**: Stood at (5, 9) facing Up, pressed Up. Result: Collision bump.
  - **Column 6 Row 8 (Verified Turn 115158)**: Stood at (6, 9) facing Up, pressed Up. Result: Collision bump.
  - **Column 7 Row 8 (Verified Turn 115163)**: Stood at (7, 9) facing Up, pressed Up. Result: Collision bump.
  - **Column 8 Row 8 (Verified Turn 115167)**: Stood at (8, 9) facing Up, pressed Up. Result: Collision bump.
  - **Column 9 Row 8 (Verified Turn 113759)**: Stood at (9, 9) facing Up, pressed Up. Result: Collision bump.
  - **Column 10 Row 8 (Verified Turn 113955)**: Stood at (10, 9) facing Up, pressed Up. Result: Collision bump.
  - **Column 11 Row 8 (Verified Turn 113960)**: Stood at (11, 9) facing Up, pressed Up. Result: Collision bump.
  - **Column 12 Row 8 (Verified Turn 113964)**: Stood at (12, 9) facing Up, pressed Up. Result: Collision bump.
- **2F West Upper-Central Corridor to Western Corridors Connection - VERIFIED FACT**:
  - **Column 8 Row 1 Passage**: Visually and physically verified on Turn 115295 on foot. Standing at (9, 1) facing Left, we pressed Left and successfully walked onto (8, 1) [TYPE_3fe2]. From there, we successfully walked all the way Left to (3, 1) on Row 1, and Down to (3, 3) on foot with zero obstacles. This conclusively disproves the previous unverified hypothesis of upper-central corridor isolation!
  - **Northwest Quadrant Access on Foot**: The upper-central corridor (where Ladder 5 at (9, 1) lands us) is directly connected to the western/northern section of 2F West on foot via Row 1!

- **Column 2 Row 1-3 Passage**: Successfully walked Left from (5, 1) to (1, 1) on Turn 117599, directly crossing Column 2 Row 1 on foot! This empirically disproves any blockage at (2, 1) and shows that there is a direct, open horizontal corridor along Row 1 that connects Ladder 5 directly to the Northwest Ladder!
  - **Column 2 Row 2-3**: To be physically tested on foot from the north. Currently, the corridor on Row 1 (including 2, 1) is 100% open and passable.
  - **Column 4 Row 4 Blockage**: Verified on Turn 115017 that standing at (4, 3) and attempting to walk Down results in a collision bump, proving (4, 4) is a solid rock wall of TYPE_2889.
  - **Column 5 Row 4 Blockage**: Verified on Turn 115032 that standing at (5, 3) and attempting to walk Down results in a collision bump, proving (5, 4) is a solid rock wall of TYPE_2889.
  - **Column 6 Row 4 Blockage**: Verified on Turn 115040 that standing at (6, 3) and attempting to walk Down results in a collision bump, proving (6, 4) is a solid rock wall of TYPE_2889.
  - **Column 7 Row 4 Blockage**: Verified on Turn 115047 that standing at (7, 3) and attempting to walk Down results in a collision bump, proving (7, 4) is a solid rock wall of TYPE_2889.
  - **Column 3 Row 4 Blockage**: Empirically tested on Turn 113495. Standing at (3, 3) facing Down, we pressed Down. Result: Collision with zero coordinate change, remaining at (3, 3). This physically proves that (3, 4) is a solid, impassable wall.
  - **Column 8 Row 4 Blockage**: Empirically tested on Turn 115315. Standing at (9, 4) facing Left, we pressed Left. Result: Collision with zero coordinate change, remaining at (9, 4), physically proving (8, 4) is a solid, impassable wall.
  - **Column 8 Row 5 Blockage**: Empirically tested on Turn 113499. Standing at (9, 5) facing Left, we pressed Left. Result: Collision with zero coordinate change, remaining at (9, 5). This physically proves that (8, 5) is a solid, impassable wall.
  - **Column 9 Row 6 Blockage**: Empirically tested on Turn 113503. Standing at (9, 5) facing Down, we pressed Down. Result: Collision with zero coordinate change, remaining at (9, 5). This physically proves that (9, 6) is a solid, impassable wall.
- Turn 112959: Tested passability of (25, 12) from (25, 11) by pressing Down. Result: Bumped against (25, 12) (TYPE_2889), player remained at (25, 11). This empirically proves that (25, 12) is completely impassable.
- Turn 112961: Tested passability of (24, 12) from (24, 11) by pressing Down. Result: Bumped against (24, 12) (TYPE_2889), player remained at (24, 11). This empirically proves that (24, 12) is completely impassable.
- Conclusion (Turn 112964): Both (24, 12) and (25, 12) are completely solid rock walls. This definitively proves that the eastern vertical water canal is a closed pocket terminating at Row 11, and does not continue further south to connect with any southern water corridor. Backtracking west is the only mathematically possible option.
- **Column 1 Row 11 Blockage (Verified Turn 115431)**: Standing at (2, 11) facing Left, pressed Left. Result: BUMP collision, player remained at (2, 11). Physically proves that (1, 11) is a solid, impassable wall of TYPE_2889 on 2F West.
- **Column 3 Row 0 Blockage (Verified Turn 116635)**: Physically bumped into (3, 0) on 2F West, proving it is a solid wall of TYPE_2889.
- **Column 9 Row 2 Blockage (Verified Turn 116451)**: Physically bumped into (9, 2) on 2F West, proving it is a solid wall of TYPE_2889.
- **Column 1 Row 10 Blockage (Verified Turn 115435-115436)**: Standing at (2, 10) facing Left, pressed Left. Result: BUMP collision, player remained at (2, 10). Physically proves that (1, 10) is a solid, impassable wall of TYPE_2889 on 2F West.
- **Column 2 Row 12 Blockage (Verified Turn 115454)**: Standing at (2, 11) facing Down, pressed Down. Result: BUMP collision, player remained at (2, 11). Physically proves that (2, 12) is a solid, impassable wall of TYPE_2889 on 2F West.
- **Column 4 Row 1 Blockage (Verified Turn 115518)**: Standing at (5, 1) facing Left, pressed Left. Result: BUMP collision, player remained at (5, 1). Physically proves that Column 4 Row 1 (4, 1) is a solid, impassable rock wall of TYPE_2889 on 1F Northwest. This empirically disproves the 1F Northwest on-foot shortcut hypothesis.
- **Column 4 Row 2 Blockage (Verified Turn 115542)**: Standing at (5, 2) facing Left, pressed Left. Result: BUMP collision, player remained at (5, 2). Physically proves that Column 4 Row 2 (4, 2) is a solid, impassable rock wall of TYPE_2889 on 1F Northwest.
- **Column 5 Row 3 Blockage (Verified Turn 115543)**: Standing at (5, 2) facing Down, pressed Down. Result: BUMP collision, player remained at (5, 2). Physically proves that Column 5 Row 3 (5, 3) is a solid, impassable rock wall of TYPE_2889 on 1F Northwest, blocking vertical access to Row 3 on the eastern side. Together, these three tests mathematically and physically prove that the northern plateau (Columns 5+, Rows 0-2) is completely isolated on foot from the western area containing (1, 3) on 1F Northwest, meaning access to the B1F stairs requires 2F West.
- **Column 7 Row 6 Blockage (Verified Turn 116663)**: Physically bumped into (7, 6) on 1F, proving it is a solid wall of TYPE_2889.
- **Turn 116934 Empirical & Logical Proof of 2F West Isolation**:
  - We ran a BFS component analysis on the actual visual screen layout on Turn 116933, which proved that 2F West is physically divided into two completely isolated ground-level components:
    - Component 1: Contains the (9, 1) ladder (from 1F Northwest) and the northern corridors.
    - Component 3: Contains the (1, 3) Northwest Ladder (to 1F Northwest / B1F stairs) and the (3, 11) Southwest Ladder (from 1F Southwest).
  - Component 1 and Component 3 are completely disconnected on foot because:
    1. Column 2 is occupied by solid rock walls (TYPE_2889) across Rows 1, 2, 3, and 4.
    2. Row 4 is blocked by solid rock walls (TYPE_2889) from Column 3 to Column 8.
    3. Row 6 is blocked by solid rock walls (TYPE_2889) from Column 7 to Column 12.
    4. Row 5 has a solid rock wall (TYPE_2889) at (8, 5).
  - Therefore, there is NO physically passable on-foot pathway between the (9, 1) ladder and the (1, 3) Northwest Ladder on 2F West. We cannot reach (1, 3) from (9, 1) on foot.
  - This conclusively disproves the hypothesis that we can access the Northwest Ladder from Ladder 5, and proves that our backtracking route via 1F Southwest and Southwest Ladder 6 at (3, 11) is 100% physically mandatory.