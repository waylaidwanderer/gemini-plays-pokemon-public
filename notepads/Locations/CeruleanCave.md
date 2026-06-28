# Cerulean Cave Location Records

## Start Metrics
- **Start Turn**: 111394
- **Start Timestamp**: Sunday, June 21, 2026 at 9:15 PM PDT
- **Goal**: Safely navigate Cerulean Cave's floors to locate B1F and capture Mewtwo.
- **Map IDs**: 0_228 (1F), 0_226 (2F)

## 1F (0_228) Verified Layout & Blockages
- **Ladder (24, 17)**: Leads out of Cerulean Cave to Cerulean City.
- **Ladder (21, 11)**: Labeled TYPE_4b8d. One-way dropdown ladder; cannot be used to ascend from 1F.
- **Ladder (23, 7)**: Labeled TYPE_3fe2. Interacting with or stepping onto this tile immediately warps the player to 2F at (22, 6).
- **Staircase at (17, 15)**: Labeled TYPE_4b8d. Connects the central platform to the ground floor at (17, 16) (Verified Turn 113127).
- **Wooden Staircase at (1, 13)**: Labeled TYPE_4b8d. Connects the southwestern ground level to the elevated southwest plateau at (1, 12) (Verified Turn 113146).
- **Ramps to Water**: Located at (23, 3), (15, 3), (11, 13), and (25, 9) (TYPE_4b8d). Standing on any of these ramps facing the water and selecting SURF from the party menu successfully mounts the water.
- **Water Canal**: Rows 4 and 5 on 1F contain water but are blocked horizontally at Column 13 by solid rock walls (TYPE_2889). However, we can bypass the Column 13 Row 4-5 blockage by surfing Down on Column 14 to Row 6/7, and then surfing Left through Column 13 Row 6/7 (which is completely open and passable water) to reach the western water canal.
- **Southern Canal Boundary (Rows 16-17) Systematic Tests**:
  - Turn 113095: Stood at (8, 15) on water and pressed Down. Result: BUMPED (8, 16 is solid).
  - Turn 113098: Stood at (9, 15) on water and pressed Down. Result: BUMPED (9, 16 is solid).
  - Turn 113107: Stood at (10, 15) on water and pressed Down. Result: BUMPED (10, 16 is solid).
  - Turn 113109: Stood at (11, 15) on water and pressed Down. Result: BUMPED (11, 16 is solid).
  - Conclusion: The entire southern boundary of the western canal on Rows 16-17 across Columns 8-11 is a solid, continuous rock wall of TYPE_2889.
- **Northern Landmass Layout (Row 0-2 ground-level shortcut)**: Rows 0, 1, and 2 form an unblocked, completely walkable ground-level connection on foot from Column 23 (Water Ramp 1) all the way east to Column 28 (Ladder 2 landing at 27,1). Verified on Turns 112008-112012.
- **Verified Blockages on 1F (Map 0_228)**:
  - **(13, 17) Passable**: Labeled TYPE_3fe2 and empirically proven fully passable on foot on Turn 128756.
  - **(3, 14) Blockage**: Labeled TYPE_2770 but physically verified on Turn 125777 as solid rock wall of TYPE_2889.
  - **(5, 7) Blockage**: Labeled TYPE_2770 but physically verified on Turn 126196 as solid rock wall of TYPE_2889.
  - **(12, 13) and (13, 13) Blockages**: Physically verified on Turn 128723 as solid rock walls of TYPE_2889.
  - **(12, 14) and (13, 14) Blockages**: Physically verified on Turn 128751 as solid rock walls of TYPE_2889.
  - **(10, 5) Blockage**: Physically verified on Turn 131825 from below as solid rock wall of TYPE_2889.
  - **(11, 5) Blockage**: Physically verified on Turn 131831 from below as solid rock wall of TYPE_2889.
  - **(12, 5) Blockage**: Physically verified on Turn 131834 from below as solid rock wall of TYPE_2889.
  - **(9, 5) Blockage**: Physically verified on Turn 131751 from below as solid rock wall of TYPE_2889.
  - **(13, 4) Blockage**: Physically verified on Turn 131928 and Turn 131931 as solid rock wall of TYPE_2889 on water.
  - **(13, 5) Blockage**: Physically verified on Turn 131919 as solid rock wall of TYPE_2889 on water.
  - **(3, 13) Blockage**: Physically verified on Turn 128819 as a solid rock wall of TYPE_2889.
  - **(2, 13) Blockage**: Physically verified on Turn 128822 as a solid rock wall of TYPE_2889.
  - **(17, 17) Blockage**: Physically verified on Turn 129205 as a solid rock wall of TYPE_2889.
  - **(18, 17) Blockage**: Physically verified on Turn 129205 as a solid rock wall of TYPE_2889.
  - **(4, 15) Blockage**: Physically verified on Turn 129221 as a solid rock wall of TYPE_2889.
  - **(5, 15) Blockage**: Physically verified on Turn 129221 as a solid rock wall of TYPE_2889.
  - **(6, 15) Blockage**: Physically verified on Turn 129221 as a solid rock wall of TYPE_2889.
  - **(7, 15) Blockage**: Physically verified on Turn 129221 as a solid rock wall of TYPE_2889.
  - **(4, 1) Blockage**: Physically verified on Turn 130148. Stood at (5, 1) and pressed Left. Result: BUMP (visited 0 tiles). Conclusively disproves the on-foot path between (7, 1) and (1, 3) on 1F Northwest.
  - **Column 1 Row 7 Blockage**: Tested on Turn 122908. Standing at (1, 8) facing Up, pressed Up. Result: BUMP.

## 2F (0_226) Verified Layout & Blockages
- **Serpentine Bypass**: Located at Column 25, Row 9. Bypasses the solid Column 26 rock barrier to allow access to the northeast section of 2F.
- **Ladder 2**: Located at (29, 1). To reach it from (29, 3): walk Left to (28, 3), Up 2 steps to (28, 1), and Right to (29, 1). Descending this ladder lands on 1F at (27, 1).
- **(5, 4) Blockage**: Labeled TYPE_3fe2 but physically verified on Turn 131664 as solid rock wall of TYPE_2889.
- **(6, 4), (7, 4), and (8, 4) Blockages**: Physically verified on Turns 131784, 131780, and 131775 respectively as solid rock walls of TYPE_2889.
- **Row 11 Passage**: Row 11 forms a completely open, unblocked horizontal passage from Column 18 to Column 24.
- **Row 16 Blockage**: Row 16 contains a solid horizontal rock wall from Column 14 to Column 20, blocking direct downward access from Row 15 to Row 17.
- **Row 9 Blockage**: Row 9 is blocked by rock walls at (22, 9) and (24, 9), so it is not a continuous horizontal corridor.
- **Row 7 Blockage (Verified Turn 113364)**: Row 7 contains a solid horizontal rock wall at (17, 7) of TYPE_2889, physically blocking on-foot horizontal crossover between Column 18 and Column 16.
- **(13, 7) Blockage (Verified Turn 113646)**: Standing at (13, 6) facing Down, pressed Down. Result: Bumped against (13, 7) (TYPE_2889).
- **(16, 8) Blockage (Verified Turn 113874)**: Standing at (16, 7) facing Down, pressed Down. Result: Bumped against (16, 8) (TYPE_2889).
- **(15, 13) Rock Wall Blockage**: Labeled TYPE_3fe2 but physically impassable horizontally between Column 14 and Column 15 on Row 13.
- **(16, 13) Rock Wall Blockage (Verified Turns 112374, 112378)**: Standing at (17, 13), attempting to walk Left to (16, 13) resulted in zero coordinate change, proving (16, 13) is impassable.
- **Verification of (12, 6) Blockage (Turn 129029)**: Standing at (12, 5) facing Down and pressing Down. Result: BUMP.
- **(22, 9) Rock Wall Blockage [2F West] (Verified Turn 113224)**: Standing at (21, 9) and pressing Right. Result: BUMP. Blocks horizontal crossover on Row 9, separating southwestern/central pocket from northern corridors.
- **Row 8 Rock Wall Blockages [2F West]**: Columns 3 to 12 are completely blocked on Row 8 by solid rock walls of TYPE_2889. Verified by systematic vertical tests from Row 9 facing Up (Turn 113759-115167).
- **2F West Upper-Central Corridor to Western Corridors Connection - DISPROVEN**: Verified on Turn 118905-119868 and Turn 130709 that 2F West's northern corridor (Component 1) is completely isolated on foot from the western area containing Northwest Ladder (1, 3). Row 6 and Row 7 form a solid, impassable vertical barrier.
- **Column 1 Corridor Passable - DISPROVEN Turn 121123**: Tested on Turn 121123 and 123226. (1, 11) is indeed a solid impassable rock wall of TYPE_2889.
- **Row 16 Blockage (Columns 2 and 3) (Verified Turn 122484)**: Column 2 Row 16 (2, 16) and Column 3 Row 16 (3, 16) are completely solid, impassable rock walls of TYPE_2889 on Map 0_226.
- **(1, 10) Blockage [2F West] (Verified Turn 122772)**: Standing at (2, 10) facing Left, pressed Left. Result: BUMP.
- **Verified Blockages on 2F (Map 0_226)**:
  - **(11, 15) Blockage**: Physically verified on Turn 128180 as solid rock wall of TYPE_2889.
  - **(6, 0) Blockage**: Physically verified on Turn 128645 as solid rock wall of TYPE_2889.
  - **(10, 6) Blockage**: Physically verified on Turn 128677 as solid rock wall of TYPE_2889.
  - **(3, 8) Blockage**: Physically verified on Turn 129254 as solid rock wall of TYPE_2889.
  - **(3, 4) Blockage**: Physically verified on Turn 129355 as solid rock wall of TYPE_2889.
  - **(8, 5) Blockage (Verified Turn 129701)**: Physically verified on Turn 129701 as solid rock wall of TYPE_2889.

## B1F (Basement) Verified Layout & Mewtwo Access
- **B1F Access**: The stairs down to B1F are located in the northwestern quadrant of 1F at (1, 3).
- **Basement Navigation**: Once on B1F, navigate the basement maze to locate and capture Mewtwo.
- **Mewtwo Battle Prep**: As we enter B1F, we will use our specialized custom agent 'mewtwo_combat_strategist' to plan the battle and capture strategy. We currently have 1 Master Ball in our bag, which guarantees a 100% catch rate! We also have 1 Ultra Ball. We will use the Master Ball to safely and instantly catch Mewtwo!
- **Verification of (4, 4) Blockage (Turn 131464)**: Standing at (4, 3) facing Left and pressing Down. Result: BUMP (visited 0 tiles). This conclusively disproves on-foot passage through (4, 4) on 2F West. Row 4 is completely impassable on 2F West.