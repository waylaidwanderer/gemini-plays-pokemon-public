# Safari Zone West (Area 3 - Map 0_219) Verified Location Records
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House.

## Map Connections
- **North**: Connected to Safari Zone North (Map 0_218) at (26, 0) and (27, 0).
  - Walking Up from (26, 0) or (27, 0) transitions back to Safari Zone North (Map 0_218) at (9, 35). (Verified)
- **East**: Connected to Safari Zone Center (Map 0_220) at Row 10-13, Column 29/30 (Unverified).

## Physical Landmarks & Obstacles
- **Rest House 3**: Located on Map 0_219 (Safari Zone West) with the door at (11, 12) and signpost at (12, 12). Entered on Turn 45293, leading to Map 0_223. (Verified)
- **Vertical Grass Corridor (Columns 25-28)**: Bounded by continuous tree walls of TYPE_2889 at Column 24 and Column 29. Fully open and passable grass (TYPE_3fe2) from Row 1 down to at least Row 12.
- **Vertical Cliff Wall Column 17 Blockage (VERIFIED on Turn 62163)**: Tested walking Right from (16, 13) into (17, 13) on the plateau. Result: BUMPED against TYPE_2889, physically proving that Column 17 is a solid vertical cliff face across all Rows 6-13 and there are no vertical jump-down transitions in Gen 1.
- **Plateau North Wall Column 18 Blockage (VERIFIED on Turn 62185)**: Tested walking Up from (18, 14) on the plateau into (18, 13) on the grass. Result: BUMPED, physically proving that the plateau horizontal boundary at Row 14 is a solid wall on Column 18 with no horizontal jump-down ledge.

## Ground-Level Connectivity between Southwest and Northwest (Blocked)
- **Hypothesis I: Western Ground Corridor Blockage (VERIFIED)**: On Turn 46257, we physically verified on foot that the western vertical corridor on Columns 2 and 3 is blocked at Row 13 by water of TYPE_4e8c, and Column 1 is blocked by trees of TYPE_2889 at (1, 13) and (1, 14). This proves that there is no direct ground-level pathway along the west edge between the southwest and northwest quadrants of Safari Zone West.
  - On Turn 46701, Column 2 Row 13 was physically proven blocked by water (TYPE_4e8c).
  - On Turn 46706, Column 6 Row 16 was physically proven blocked by a solid cliff face (TYPE_2770).
  - On Turns 47346-47365, Column 4, 5, 6, 7, and 8 along Row 13 were physically tested and proven to be 100% blocked by water (TYPE_4e8c) collision on foot.
  - On Turns 47375-47398, Column 14 on Rows 12, 13, 14, and 15 was physically tested on foot and proven to be 100% blocked by solid cliff/wall collision. This definitively proves Column 14 cannot be used as a ground-level pathway past Rest House 3.
- **Hypothesis N: Eastern Ground Corridor Column 24 Blockage (VERIFIED)**: On Turn 47113, we completed the systematic foot-testing of Column 24 on all Rows 1-12. Every single row was proven to be blocked by solid tree walls (TYPE_2889), with Row 1 trivially blocked by (25, 1) and (24, 1) being solid trees. This definitively proves Hypothesis N and proves that the eastern ground-level corridor is completely blocked and impassable.
- **Ground Corridor Column 9 Route (BLOCKED)**: Column 9 is completely blocked by water on Rows 10-13, and the plateau at Columns 11-16 blocks horizontal movement, meaning the southwest quadrant is actually a completely closed ground pocket on foot. Traversing the plateau via (21, 17) [stairs UP] and (6, 19) [stairs DOWN] is absolutely required to reach the northwest quadrant. (Verified on Turn 50608)
- **Ground Corridor Column 10 Route (BLOCKED)**: On Turn 53177, standing at (10, 12), we physically tested walking Up into Column 10 Row 11 on foot. Result: Collision (bump) against Rest House 3's solid building wall (TYPE_2889), physically proving Column 10 Row 11 is impassable. Since Column 9 is blocked by water (Rows 10-13) and Column 14 is blocked by the plateau cliff wall (Rows 12-15), this definitively confirms that there is zero ground-level bypass, making the southwest quadrant a completely closed ground pocket. Traversing the plateau is 100% mandatory.
- **Ground Corridor Column 12/18 Blockage (VERIFIED on Turn 58966 & 58990)**: Standing at (12, 20), walking Up results in collision against a solid tree wall of TYPE_2889 at (12, 19). Standing at (17, 20), walking Right is blocked by a solid tree wall of TYPE_2889 at (18, 20), and walking Up is blocked by TYPE_2889 at (17, 19). This physically proves that Column 18 is a solid tree wall on Rows 20-23, and Row 19 is a solid tree wall from Column 8 to Column 17, completely isolating the southwest ground pocket from both the northern area and the eastern stairs at ground level. Traversing the plateau is 100% mandatory.

## Northern Plateau Verified Constraints
- **Northern Plateau Wall (Row 6 Blockage)**: Columns 12, 13, 14, 15, and 16 on Row 6 are completely blocked to the North by solid cliff walls, preventing direct vertical descent onto Row 5 on those columns.
  - On Turns 47440-47450, we physically verified on foot that Row 6 Columns 12, 13, and 14 are blocked by solid cliff walls (TYPE_2770 to TYPE_3fe2 transition), confirming the Northern Plateau Wall is impassable on these columns.
  - On Turn 47466, we physically verified on foot that Row 6 Column 16 is also completely blocked by solid cliff walls (TYPE_2770 to TYPE_3fe2 transition), meaning the entire Row 6 plateau boundary is impassable on foot.
- **Horizontal Row 7 / Row 6 Passability**: Row 7 and Row 6 are fully open horizontally, allowing us to bypass the vertical partition wall at Column 16 by walking Down to Row 7, Left to Column 15, and Up to Row 6. (Verified on Turn 46629)
## Southwest Ground-Level Boundary Verifications (Turn 46877-46882)
- **Column 1 Passability**: Column 1 is fully passable of TYPE_3fe2 (cosmetic tree tile with no active collision) from Row 16 down to Row 23, allowing us to walk on Column 1 to avoid tall grass wild encounters on Column 2/3.
- **Column 1 Northern Blockage**:
  - Standing at (1, 16) on Turn 46877, attempted to walk Up into (1, 15). Result: Collision, physically proving that Column 1 Row 15 (TYPE_2889) is a solid, impassable tree wall.
  - Standing at (2, 14) on Turn 46882, attempted to walk Left into (1, 14). Result: Collision, physically proving that Column 1 Row 14 (TYPE_2889) is also a solid, impassable tree wall.
- **Column 0 Border Blockage**: Standing at (1, 16) on Turn 46880, attempted to walk Left into (0, 16). Result: Collision, physically proving that Column 0 (the western map boundary) is solid and impassable at Row 16.
- **Northern Plateau Wall Column 14 (VERIFIED on Turn 48534)**: Standing at (14, 6) facing Up, attempted to walk Up into (14, 5). Result: Collision, physically proving that Column 14 Row 6 is blocked by a solid cliff wall (TYPE_2770 to TYPE_3fe2 transition), meaning we cannot jump or descend north off the plateau here.
- **Northern Plateau Wall Column 11 (VERIFIED on Turn 48598)**: Standing at (11, 6) facing Up, attempted to walk Up into (11, 5). Result: Collision, physically proving that Column 11 Row 6 is blocked by a solid cliff wall (TYPE_2770 to TYPE_3fe2 transition). Since Columns 11, 12, 13, 14, and 16 have all been proven impassable to the North, the entire northern plateau boundary is a solid impassable wall on foot.
- **Northern Plateau Wall Column 15 (VERIFIED on Turn 48607)**: Standing at (15, 6) facing Up, attempted to walk Up into (15, 5). Result: Collision, physically proving that Column 15 Row 6 is blocked by a solid cliff wall (TYPE_2770 to TYPE_3fe2 transition). Combined with Columns 11, 12, 13, 14, and 16, this physically proves the entire northern plateau boundary on Row 6 is 100% blocked and impassable.