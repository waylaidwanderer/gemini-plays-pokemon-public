# Safari Zone West (Area 3 - Map 0_219) Verified Location Records
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House.

## Map Connections
- **North**: Connected to Safari Zone North (Map 0_218) at (26, 0) and (27, 0).
  - Walking Up from (26, 0) or (27, 0) transitions back to Safari Zone North (Map 0_218) at (9, 35). (Verified)
- **East**: Connected to Safari Zone Center (Map 0_220) at Row 10-13, Column 29/30 (Unverified).

## Physical Landmarks & Obstacles
- **Rest House 3**: Located on Map 0_219 (Safari Zone West) with the door at (11, 12) and signpost at (12, 12). Entered on Turn 45293, leading to Map 0_223. (Verified)
- **Vertical Grass Corridor (Columns 25-28)**: Bounded by continuous tree walls of TYPE_2889 at Column 24 and Column 29. Fully open and passable grass (TYPE_3fe2) from Row 1 down to at least Row 12.
## Ground-Level Connectivity between Southwest and Northwest (Blocked)
- **Hypothesis I: Western Ground Corridor Blockage (VERIFIED)**: On Turn 46257, we physically verified on foot that the western vertical corridor on Columns 2 and 3 is blocked at Row 13 by water of TYPE_4e8c, and Column 1 is blocked by trees of TYPE_2889 at (1, 13) and (1, 14). This proves that there is no direct ground-level pathway along the west edge between the southwest and northwest quadrants of Safari Zone West.
  - On Turn 46701, Column 2 Row 13 was physically proven blocked by water (TYPE_4e8c).
  - On Turn 46706, Column 6 Row 16 was physically proven blocked by a solid cliff face (TYPE_2770).
- **Plateau Route Requirement**: To reach the northern part of Safari Zone West (where the Gold Teeth and Secret House are), both the western and eastern ground corridors are completely blocked, making the elevated plateau the ONLY possible route.

## Northern Plateau Verified Constraints
- **Northern Plateau Wall (Row 6 Blockage)**: Columns 12, 13, 14, 15, and 16 on Row 6 are completely blocked to the North by solid cliff walls, preventing direct vertical descent onto Row 5 on those columns. (Verified on Turns 46615-46651)
- **Horizontal Row 7 / Row 6 Passability**: Row 7 and Row 6 are fully open horizontally, allowing us to bypass the vertical partition wall at Column 16 by walking Down to Row 7, Left to Column 15, and Up to Row 6. (Verified on Turn 46629)
## Southwest Ground-Level Boundary Verifications (Turn 46877-46882)
- **Column 1 Passability**: Column 1 is fully passable of TYPE_3fe2 (cosmetic tree tile with no active collision) from Row 16 down to Row 23, allowing us to walk on Column 1 to avoid tall grass wild encounters on Column 2/3.
- **Column 1 Northern Blockage**:
  - Standing at (1, 16) on Turn 46877, attempted to walk Up into (1, 15). Result: Collision, physically proving that Column 1 Row 15 (TYPE_2889) is a solid, impassable tree wall.
  - Standing at (2, 14) on Turn 46882, attempted to walk Left into (1, 14). Result: Collision, physically proving that Column 1 Row 14 (TYPE_2889) is also a solid, impassable tree wall.
- **Column 0 Border Blockage**: Standing at (1, 16) on Turn 46880, attempted to walk Left into (0, 16). Result: Collision, physically proving that Column 0 (the western map boundary) is solid and impassable at Row 16.