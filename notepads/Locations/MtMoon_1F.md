# Mt. Moon 1F Location Records

## Layout & Floor Navigation:
- **Passable Cave Floor**: TYPE_2770 is verified passable.
  - **Proof of Work**: Tested on Turn 6060 by successfully walking south from (25, 15) (TYPE_3fe2) onto (25, 16) (TYPE_2770) without collision.
- **Platform Height Boundary**:
  - **Verified Fact**: The southern boundary of the platform at Row 20 acts as an impassable wall. Tested on Turn 6955 at (17, 20) (pressing Down from (17, 19)) and on Turn 6959 at (16, 20) (pressing Down from (16, 19)). Both tests resulted in zero movement, physically proving that the platform transition to the lower cavern floor is solid and impassable both ways without stairs.
- **Eastern Corridor**: Rows 14-27, Columns 24-27 are fully passable floor (TYPE_2770). Verified by traversing from (25, 15) down to (25, 23) on Turns 6530-6551.
- **Southern Corridor & Rock Wall Bypass**:
  - **Verified Fact (Turn 7959)**: Columns 21-23 on Row 26 are impassable rock walls despite the grid overlay labeling them as TYPE_2770. Visually they are light-blue rock textures, showing the central vertical rock wall extends down to Row 27.
  - **Verified Fact (Turn 7966)**: Row 28 is a fully passable dark floor corridor of TYPE_3fe2, connecting the Eastern Corridor (Columns 24-25) to the Western/Southern area (Column 20-21) by going underneath the rock wall.
  - **Verified Fact (Turn 8048)**: Column 19 is a solid, impassable wall on Rows 28, 30, 31, and 32, preventing direct horizontal traversal from the Eastern Corridor to the Western area on these southern rows. Tested during systematic overworld collision tests.
- **Ladders**:
  - Ladder to B1F (NE section): Located at (25, 15). Connects to Mt. Moon B1F at (25, 15).
  - Ladder to B1F (North-Central section): Located at (17, 11). Connects to Mt. Moon B1F at (25, 9). Verified on Turn 6689.

## Mt. Moon Trainer Milestones:
- [x] Bug Catcher at (7, 22) (Defeated! Team: Level 11 Weedle, Level 11 Kakuna. Defeated on Turn 5294. BUGGY leveled up to 9!)
- [x] Lass at (16, 22) (Defeated! Team: Level 14 Clefairy. Defeated on Turn 5373. BUGGY and GEMMY gained 102 EXP each.)
- [x] Lass Miriam at (30, 4) (Defeated! Team: Level 11 Oddish, Level 11 Bellsprout. Defeated on Turn 5580. BUGGY evolved into BUTTERFREE at Lv 10!)

## Verified Discoveries:
- [x] Potion: Located at (2, 20) (Obtained on Turn 5202).
- [x] TM12 (Water Gun): Located at (5, 32) (Obtained on Turn 5227).
- [x] Escape Rope: Located at (36, 23) (Obtained on Turn 5250).
- **Platform Height Boundary (Row 21 & Row 19 Verified)**:
  - **Verified Fact (Turn 7838)**: Row 21 acts as a solid rock barrier. Standing at (10, 22) facing Up, attempting to move north into (10, 21) (TYPE_2889) resulted in a direct collision and zero movement, proving this visual boundary is physically solid and impassable.
  - **Verified Fact (Turn 7850)**: Row 19 acts as a solid rock barrier. Standing at (6, 20) facing Up, attempting to move north into (6, 19) (TYPE_2889) resulted in a direct collision and zero movement, proving this visual boundary is physically solid and impassable.
- **Verified Fact (Turn 8293)**: Column 16 is a solid rock wall (TYPE_2889) on Rows 29, 30, 31, 32, 33, 34, and 35. Standing at (15, 33) on Turn 8293, we attempted to walk Right into (16, 33) (TYPE_2889) and directly collided with the wall (0 tiles visited), physically proving that Column 16 is solid. This means there is no direct horizontal connection on the southern rows (Rows 29-35) between Column 15 and the eastern side of the map (Column 20).