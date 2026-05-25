# Mt. Moon B2F Location Records

## Connections:
- **Ladder to B1F**: Located at (15, 27). Connects to Mt. Moon B1F at (13, 27). Verified on Turn 6309.
- **Stairs to B1F (TYPE_4b8d)**: Located at (24, 23) and (25, 23). Verified on Turn 6238 as passable platform stairs.

## Layout & Floor Navigation:
- **Passable Cavern Floor**: TYPE_2770 is the primary passable cavern floor.
- **Cavern Obstacles (TYPE_de37)**: Visually structured like rectangular pillars/walls. Tested and confirmed solid (impassable) on Turn 6205 at (13, 25), on Turn 6213 at (14, 28), on Turn 6577 at (15, 28) (by pressing Down from the (15, 27) ladder), and on Turn 6615 at (21, 28) (by pressing Down from (21, 27)). These individual coordinate tests show that TYPE_de37 blocks horizontal and vertical movement at those specific coordinates. Other columns of Row 28 (such as columns 12-14, 16-20, and 22-27) are visual obstacles of TYPE_de37 and are treated as unverified visual theories until tested.
- **Eastern Corridor**: Located at columns 28 & 29. Verified passable from row 26 up to row 22.

## Strategic Markers:
- `(15, 27): 🚪 Ladder to B1F`
- `(15, 24): ☠️ Rocket Grunt defeated`
- `(25, 21): ✅ HP UP collected`
- `(29, 5): ✅ TM01 (Mega Punch) collected (Turn 6803)`

## Northern Section (Accessible via B1F ladder at (17, 11) leading to B2F at (25, 9)):
- Ladder to B1F: Located at (25, 9). Leads to B1F at (17, 11).
- TM01 (Mega Punch) collected at (29, 5) on Turn 6803.
- Observed potential trainer/grunt at (29, 11).
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