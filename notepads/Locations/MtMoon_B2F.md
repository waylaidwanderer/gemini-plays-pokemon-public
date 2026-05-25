# Mt. Moon B2F Location Records

## Connections:
- **Ladder to B1F**: Located at (15, 27). Connects to Mt. Moon B1F at (13, 27). Verified on Turn 6309.
- **Stairs to B1F (TYPE_4b8d)**: Located at (24, 23) and (25, 23). Verified on Turn 6238 as passable platform stairs.
- **Southern Section Exploration & Partial Blockage (Turn 8199)**:
  - The eastern corridor at Row 21 on B2F (accessible via the ladder at (15, 27) and moving east) is blocked. Standing at (28, 22) on Turn 8199, we attempted to walk Up into (28, 21) (TYPE_2889) and directly collided with the wall (0 tiles visited), proving that the eastern corridor is blocked at Row 21.
  - **Unverified Hypothesis**: The western corridor (Columns 12-16) near Row 21 has not been physically tested for vertical passability. It is currently unverified whether a path exists connecting the southern section to the central/northern section on the west side of B2F.

## Layout & Floor Navigation:
- **Passable Cavern Floor**: TYPE_2770 is the primary passable cavern floor.
- **Cavern Obstacles (TYPE_de37)**: Visually structured like rectangular pillars/walls. Tested and confirmed solid (impassable) on Turn 6205 at (13, 25), on Turn 6213 at (14, 28), on Turn 6577 at (15, 28) (by pressing Down from the (15, 27) ladder), and on Turn 6615 at (21, 28) (by pressing Down from (21, 27)). These individual coordinate tests show that TYPE_de37 blocks horizontal and vertical movement at those specific coordinates. Other columns of Row 28 (such as columns 12-14, 16-20, and 22-27) are visual obstacles of TYPE_de37 and are treated as unverified visual theories until tested.
- **Eastern Corridor**: Located at columns 28 & 29. Verified passable from row 26 up to row 22.

## Strategic Markers:
- `(15, 27): 🚪 Ladder to B1F`
- `(15, 24): ☠️ Rocket Grunt defeated`
- `(25, 21): ✅ HP UP collected`
- `(29, 5): ✅ TM01 (Mega Punch) collected (Turn 6803)`
- `(29, 17): ☠️ Rocket Grunt defeated (Turn 7155)`

## Northern Section (Accessible via B1F ladder at (17, 11) leading to B2F at (25, 9)):
- **Verified Fact (Turn 8592)**: The Northern Section (Rows 5-11, Columns 24-30) is a completely enclosed, isolated cul-de-sac pocket. Row 12 Column 25 acts as a solid rock cliff wall (mismarked as TYPE_2770 on the overlay) which prevents any southern traversal to the central stairs. It is a dead end.
- Ladder to B1F: Located at (25, 9). Leads to B1F at (17, 11).
- TM01 (Mega Punch) collected at (29, 5) on Turn 6803.
- Turn 6910: Verified that stairs at (28, 7) and (29, 7) are fully passable, bidirectional stairs. They connect the elevated platform (Row 7) to a lower, enclosed 4x2 alcove consisting of rows 5-6 and columns 27-30 (TYPE_2770). This alcove has walls (TYPE_2889) on all other sides (Row 4, column 26, column 31). This is where TM01 (Mega Punch) was collected at (29, 5). No other pathways exist in this small alcove.
- **Ladder to B1F (Central/NW section)**: Located at (21, 17). Connects to Mt. Moon B1F at (21, 17). Verified on Turn 7029. This ladder leads to a central elevated platform area on B2F.
- **Central Elevated Platform Area (around Row 13-18, Columns 20-26)**:
  - Accessible via (21, 17) ladder.
  - Walkable ground is TYPE_2770.
  - To the east (column 25-26), there are tiles of type TYPE_3fe2 at Rows 16-18.
  - Let's explore this platform.
  - Central Platform Stairs: Located at (26, 15) and (27, 15) (TYPE_4b8d), providing transition from the elevated central platform to the eastern floor area.
- **Passable Cavern Floor (TYPE_3fe2)**: Verified on Turn 7064. Successfully moved Down from (26, 15) to (26, 16) (TYPE_3fe2) without collision, proving that the dark patterned tiles in rows 16-18 are fully passable cavern floor on B2F.
- **Eastern Floor Area (Columns 25-31, Rows 16-18)**:
  - Accessible via stairs at (26, 15) and (27, 15).
  - Walkable floor is TYPE_3fe2.
  - Rocket Grunt located at (29, 17) (TYPE_3fe2). Talked to him on Turn 7074, initiating a trainer battle. (Previously misidentified as a floor item due to the orange/black sprite, but confirmed as a Rocket Grunt).

## Southern Platform (Rows 21-23, Columns 23-26):
- **Layout & Isolation Constraint (Turn 8170 Verification)**: 
  - Accessible from the lower floor via stairs at (24, 23) and (25, 23) (TYPE_4b8d).
  - Walkable floor on the platform consists of (23, 21-22), (24-25, 21-22), (26, 21-22), and (25, 23).
  - The western boundary of this platform at Column 22 on Rows 21 and 22, and Column 23 on Row 23, consists of solid rock walls (TYPE_2889).
  - Standing at (25, 21) on Turn 8170, the visual grid overlay clearly confirms (22, 21) and (21, 21) are solid rock walls (TYPE_2889).
  - This platform is completely isolated from the Central Elevated Platform and does not allow any western or northern traversal beyond Column 23, making it a dead end where only HP UP was obtained at (25, 21). Verified on Turn 8170.
- **Verified Fact (Turn 9694)**: Standing at (32, 11) facing Down, we attempted to walk south onto (32, 12). The action resulted in 0 tiles visited, proving that Row 12 Columns 31-35 consists of a solid rock wall (despite being labeled as TYPE_2770). It is NOT a jumpable ledge. This confirms that the Northern Section of B2F is a completely isolated cul-de-sac dead end.
- **Verified Fact (Turn 9700)**: Since B2F (25, 9) is a dead end, we backtracked up to 1F at (17, 11). The true route to the fossils must be via the Central Platform ladder at B1F (21, 17) -> B2F (21, 17), then walking east to the Central Platform stairs at (26, 15)/(27, 15), walking east past the Rocket Grunt at (29, 17), and finally exploring north on Columns 31-35.
- **Verified Fact (Turn 9771)**: While standing at (34, 12) on the eastern elevated platform of Mt. Moon B2F, we attempted to move north into (34, 11) (TYPE_3fe2) and collided.
- **Verified Fact (Turn 9771)**: While standing at (35, 12) on the eastern elevated platform of Mt. Moon B2F, we attempted to move north into (35, 11) (TYPE_3fe2) and collided.
- **Conclusion**: The entire Row 11/12 boundary from Column 28 to Column 35 is a completely impassable cliff face in both directions, separating the central platform's eastern stairs from the northern section of B2F.