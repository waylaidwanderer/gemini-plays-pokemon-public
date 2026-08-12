# Safari Zone - Overworld Layout & Navigation Guide

## Area 1 (East) Map & Transitions
- **Exit to Area 2 (North):** Located at `(0, 5)`.
  - **CRITICAL WARNING:** You must transition at Row 5 (`(0, 5)`), which warps you to Column 39, Row 31 of Area 2 (North) (leading to the walkable southern corridor).
  - Transitioning at Row 3 (`(0, 3)`) is a trap: it warps you to Column 39, Row 2 of Area 2 (North), which is an isolated ground-level dead end!

## Area 2 (North) Map & Collision Structures

### Key Landmarks & Buildings
- **Rest House 2:** Located at columns 21-25, rows 12-13. The entrance door is at `(22, 13)`.
- **Plateau Land Bridge:** A raised cliff system that provides the ONLY path connecting the northern/eastern sections of the map to the southern/western ground level (which leads to Area 3).
  - Central Plateau Area: Columns 22-23, rows 14-16.
  - **East Stairs (Plateau Entrance):** Located at `(32, 13)` and `(33, 13)` facing east on row 13.
  - **West Stairs:** Located at `(20, 15)` facing west on column 20.

### Major Boundaries & Blockages
- **Row 10 Tree Line:** A solid barrier of pine trees across columns 27-31, blocking direct southern traversal on columns 28-29.
- **Row 15-19 Isolation Barrier:**
  - Columns 2-11 on Row 15 have a solid tree wall.
  - Columns 12-18 on Row 15 are open grass, but they lead to the middle pond on rows 17-18 (columns 9-11) and a fenced animal pen bordered by grey Rhydon statues on row 19 (columns 10-17).
  - Because of this, the northwest area (Rest House 2, columns 1-14) is a physical dead end on the ground level. You cannot walk directly south or southwest to Area 3 from column 2.
- **Column 19 Tree Barrier:** A continuous vertical line of trees on rows 14-18, column 19, blocking direct horizontal passage on row 14. But row 12 and row 13 are open on column 19.
- **Column 16 Bush Barrier (Rows 12-19):** Solid vertical line of dark checkerboard bush/hedge tiles on column 16, rows 12-19. Completely blocks ground-level horizontal crossing on those rows.

---

## Macro-Level Layout Connection in Area 1 (East)
To reach the northern exit at `(0, 5)` from the bottom-left entrance at `(0, 22)`, the player must navigate the map in a spiral/zig-zag topology:
1. **Southern Ground Level:** Walk east from `(0, 22)` on the ground to `(20, 21)`.
2. **Southern Plateau Crossing:** Climb stairs at `(20, 21)` to `(20, 20)`. Walk west on the plateau to `(12, 20)`. Descend stairs at `(12, 21)` to ground level at `(12, 22)`.
3. **Western/Middle Ground Level:** Walk north on columns 8-9 to row 8, then east to `(12, 8)`.
4. **Northern Plateau Crossing (East-Bound):** Climb stairs at `(12, 7)` to `(12, 6)` on the northern plateau. Walk east on the plateau to `(17, 6)`. Descend stairs at `(17, 7)` to the northeastern ground level at `(17, 8)`.
5. **Northeastern/Northern Ground Passage:** From `(17, 8)`, walk right to column 18/19/20, then walk UP past the row 6-7 barrier to row 5 (northern ground level).
6. **Northwest Ground Level Exit:** From the northern ground level, walk west all the way to the top-left corner at `(0, 5)` to transition to Area 2 (North) at `(39, 31)`.

## Area 2 (North) - East-West Plateau Connections (Turn 27563-27565)
- **Eastern Land Bridge (Cols 37-38, Rows 14-26):** Empirically verified as a completely continuous, flat brown plateau land bridge on columns 37-38, rows 14-26. It connects the Eastern Southern Plateau (stairs at 28, 27) directly to the Northern Plateau on the north side.
- **Plateau Separation (Column 26):** The Eastern Southern Plateau and Western Southern Plateau do **NOT** connect horizontally on rows 24-26. They are separated by column 26 cliff wall and columns 22-25 ground-level tall grass.

## Area 3 (West) Layout & Discoveries

### Map Transitions & Connections
- **Entered from Area 2 (North):** Transition from Area 2 (North) at `(4, 35)` leads directly into Area 3 (West) at `(26, 0)` (Turn 27591).
- **East Edge Map Transition:** The far-right edge of Area 3 (West) at column 30, row 23 connects directly to Safari Zone Center at `(0, 11)` (Turn 27658).

### Overworld Obstacles & Paths
- **Vertical Hedge Wall (Column 24):** A solid vertical line of green hedge/bush tiles running from row 0 down to row 13 on column 24. This completely blocks horizontal ground-level passage in the north.
- **Hedge Wall Gap (Rows 14-15):** The vertical hedge wall ends at row 13. There is a wide, walkable open grass gap on rows 14-15, column 24, allowing ground-level horizontal crossing.
- **The Plateau (Rows 14-18, Columns 9-22):** A large, continuous raised plateau structure.
  - **East Stairs (Plateau Access):** Located at `(21, 17)`. These stairs face SOUTH. The player MUST approach them from the south at ground level `(21, 18)` and climb by walking UP (North) onto `(21, 17)` and then `(21, 16)` to reach the plateau. Direct horizontal access from the east at `(22, 17)` is completely blocked by the solid cliff wall.
  - **West Stairs (Plateau Descent):** Located at `(6, 19)`. Facing Down, these stairs allow the player to descend from the plateau onto the western ground level grass.
  - **Note:** The Plateau completely blocks ground-level horizontal crossing on rows 15-18.
- **Column 18 Vertical Barrier (Rows 20-23):** A solid tree/wall structure running vertically on Column 18 across rows 20-23, blocking horizontal ground-level passage.
- **Horizontal Cliff Wall (Rows 24-25):** Runs horizontally across the map, separating the north ground level from the south ground level:
  - Row 24 on Columns 2-9 is solid cliff wall/trees (Column 19 is the open gap to the south).
  - Row 25 on Columns 10-21 is solid cliff wall.
  - Row 24 on Columns 22-29 is solid cliff wall.

### Western Ground Level & Items
- **Western Ground Grass (Rows 20-24, Columns 2-12):** A large patch of tall grass where wild battles can occur.
- **Max Potion:** Located on the ground at `(8, 20)`. This is a solid overworld item ball sprite. It was successfully picked up by standing at `(7, 20)` facing Right on Turn 27623.
- **Signpost at (24, 22):** Reads "AREA 3 EAST: CENTER AREA" (Turn 27655).

### 🔍 Verified Area 3 (West) Landmarks & Paths
- **Rest House 3:** Located on the western ground level. The verified entrance door (doormat) is at `(11, 11)`. Inside is a Hiker NPC who gives standard Hiker dialogue (Rest House 3 does NOT contain Surf).
- **The Secret House:** Located in the isolated northwest ground section of Area 3 (West). The entrance door is at `(3, 8)`. The player can only reach this section by entering through the southwest ground-level transition of Area 2 (North) at `(4, 36)`. Inside the Secret House is the NPC who gives HM03 (Surf) at `(2, 7)`.
- **Southwest Area:** Walked Column 3 from Row 20 up to Row 14 (`(3, 20)` to `(3, 14)`), proving `(3, 19)` and `(3, 18)` are walkable grass/trees with NO secret warp or door.
- **Southern Passage Access:** The southern ground level (containing Row 24-28) is accessed from Column 21 on the east side. Walk south past the East Stairs on Column 21 to Row 24, and then walk west.
- **The Row 26 Highway:** Row 26 is completely open and serves as a horizontal ground-level path connecting the eastern area (Column 19/21) to the western area (Columns 3-10), bypassing the hedge barriers on Rows 24 and 25.

## Area 1 (East) Detailed Overworld Layout & Barriers

### Vertical & Horizontal Barriers
- **Column 6 Rhydon Statue Barrier:** Grey Rhydon statues at `(6, 22)` and `(6, 23)` completely block ground-level horizontal crossing on row 22.
- **Western Row 6 Tree Barrier:** A continuous vertical barrier of trees at columns 0-10 on row 6, blocking all direct northern traversal on the west ground level.
- **Row 12 NPC Block:** A stationary NPC at `(15, 12)` completely blocks row 12 ground traversal, making it impossible to walk directly from the west ground to the east ground on rows 12-13.
- **Middle Pond Separator:** A large water pond at columns 11-17, rows 10-14, which completely divides the west ground level from the east ground level.
- **Northeastern/Northern Barriers:**
  - Row 4 is blocked by trees at columns 20-27.
  - Row 3 is blocked by a tree at `(28, 3)`.

### Key Bridges & Plateaus
- **The Northern Plateau Island:** Raised cliff system at columns 11-18, rows 4-7. This serves as the ONLY physical bridge connecting the western ground level to the eastern ground level.
  - **West Climbing Stairs:** Located at `(12, 7)` facing UP on column 12.
  - **East Climbing Stairs:** Located at `(17, 7)` facing UP on column 17.

### Map Transitions & Exits
- **Exit to Area 2 (North):** Located at `(0, 5)` on row 5, which is reachable from the northern ground corridor.
- **Column 20 Hedge Passage (Rows 4-6):** Empirically verified on Turn 29054. Hedges on Column 20 at Rows 4 and 6 have 0% collision, enabling players to walk directly UP to Row 3.
- **Row 3 Obstruction (Col 5):** A solid pine tree at `(5, 3)` blocks direct horizontal passage on Row 3.
- **Northern Corridor Bypass Route:** From Column 20 Row 3, walk left to `(7, 3)`, walk Down to `(7, 5)` (bypassing the `(6, 4)` building door and the `(5, 3)` pine tree), and then walk Left along Row 5 to `(0, 5)` to transition to Area 2 (North) safely. Avoid transitioning at `(0, 3)`, which is a trap!

## Safari Zone Center - Detailed Layout & Obstacles

### Key Discoveries & Pathways
- **The Column 11 Tree Wall:** A solid vertical line of pine trees on Column 11 across Rows 0-7, completely blocking direct ground-level horizontal crossing on those rows.
- **The Southern Ground Corridor:** Rows 10-22 are open ground, allowing players to walk Left to Column 0 around the central water pond.
- **Western Edge Transition to Area 3 (West):** Located on Column 0, Row 11 (`(0, 11)`), transitioning directly to Area 3 (West) at `(30, 23)`. This ground-level path completely bypasses Area 2 (North).

## Gold-Standard Speedrun Route from Area 1 (East) to Area 3 (West)
1. **Northeast Channel:** From Area 1 (East) ground level, walk UP Column 20 (which is completely open and walkable, including the tree graphic at `(20, 4)`) to Row 5 (`(20, 5)`).
2. **Northern Corridor:** Walk LEFT along Row 5 to Column 0, then walk LEFT to transition to Area 2 (North) at `(39, 31)`.
3. **Area 2 Southern Corridor to Area 3 (West):** Walk LEFT along Row 31 to Column 22, walk UP to Row 23, climb Western Southern Plateau stairs at `(22, 23)` onto plateau, walk West to `(16, 23)`, walk DOWN to `(16, 27)` to descend stairs to `(16, 28)`. Walk Left to `(12, 33)`, bypass the Rhydon statues via Column 8-9 gap, and walk LEFT/DOWN to transition directly into **Area 3 (West)** at `(26, 0)`.
## Area 2 (North) - Completed Spatial Map & Route to East Stairs
- Ground Level is on Rows 0-11 (North) and Rows 16-35 (South).
- Rows 12-15 is the Northern Plateau (East side, columns 32-38).
- Column 16 Bush Barrier (Rows 12-19) and Row 11 barriers (Rhydon statues at cols 21-31, trees at 16-17) completely divide the Northwest ground level from the Northeast and South ground levels.
- The ONLY way to go from the Northwest ground level (Rest House 2, cols 1-15) to the South/East is to walk UP to Row 9, walk East along Row 9 (which is completely open and has 0% trees), and then walk back down.
- On the East side, Columns 32-38 row 12-15 is the Northern Plateau. The East Stairs at `(32, 13)` and `(33, 13)` face WEST (accessed from Column 31 on the ground, walking RIGHT/EAST onto the stairs).
- Column 31 is completely open on rows 12-13.
- To reach Column 31 from the Southern Corridor (Row 30/31):
  1. Walk to Column 25 (ground level separation between Eastern and Western Southern Plateaus).
  2. Walk UP Column 25 past the plateaus to Row 17 (ground level).
  3. Walk East along Row 17 to Column 31 (ground level).
  4. Walk UP Column 31 to Row 13, and walk RIGHT onto the East Stairs at `(32, 13)` to climb onto the plateau!

## 🧪 Empirical Proof of Safari Zone Center Compartmentalization (Turn 30402)
We have systematically probed the horizontal and vertical boundaries of Safari Zone Center and proven that the map is divided into two completely unconnected ground-level compartments: the **South/East Entrance Compartment** and the **Northwest Area 3 Transition Compartment**. There is **NO DIRECT SHORTCUT** between them.

### Refutation of Hypothesized Shortcuts:
1. **The Row 11 Shortcut (Refuted Turn 30392):** Walking Left along Row 11 is completely blocked by the central water pond on Columns 18-21 (visually confirmed blue water tiles on screen).
2. **The Row 16/17 Shortcut (Refuted Turn 30402):** Row 16 on Columns 2-5 is blocked by a continuous horizontal hedge wall (visually confirmed in `player_around_6_16.png` and at coordinate `(2, 17)`). Columns 0-1 on Row 16 and 17 are blocked by solid overworld pine trees.
3. **The Rest House / Pond Block:** Rest House 1 blocks Columns 10-15 on Rows 14-15. The pond blocks Columns 9-17 on Rows 10-14. This creates an unbroken barrier of water and buildings across the middle.

### Conclusion:
To reach Area 3 (West), the player **MUST** use the intended speedrun route across three maps:
**Safari Zone Center -> Area 1 (East) -> Area 2 (North) -> Area 3 (West)**.
Any attempt to find a ground-level shortcut within Safari Zone Center is mathematically blocked by map collision.
### Verified Collisions & Landmarks in Area 3 (West) (Turns 32706 - 32738)
- **Column 18 Shrub Barrier:** Solid green shrubs run vertically on column 18, rows 20-23, causing a bump when walking Left from `(19, 23)` to `(18, 23)`.
- **Row 24 Shrub Barrier:** Solid green shrubs run horizontally on row 24, columns 17-29 (with a corridor on row 24 columns 18-21), blocking Left movement from `(18, 24)` to `(17, 24)`.
- **Verified Collisions (Turns 32923 - 32936):**
  - Attempted Left from `(18, 24)` to `(17, 24)` (solid shrub, bumped on Turn 32923).
  - Attempted Down from `(18, 24)` to `(18, 25)` (solid shrub, bumped on Turn 32923).
  - Attempted Left from `(18, 19)` to `(17, 19)` (cliff wall, bumped on Turn 32924).
  - Attempted Down from `(18, 19)` to `(18, 20)` (solid tree, bumped on Turn 32924).
  - Attempted Up from `(11, 20)` to `(11, 19)` (cliff wall, bumped on Turn 32936).
## Safari Zone Center - Completed Spatial Map & Route (Turn 34275)
### Verified Barriers & Topography
1. **North-South Ground Division (Row 25):** Row 25 is completely blocked from Column 0 to Column 29 by solid Rhydon statues and wooden fences. The ONLY opening is at `(15, 25)` which contains the exit warp back to the Gatehouse.
2. **The Ledge (Row 23):** A horizontal south-facing ledge runs across Row 23, blocking all direct UP (North) movement from Row 24 to Row 23, except at Column 15 (the entrance corridor).
3. **The Plateau North Edge Cliff (Row 11/12):** The northern edge of the plateau (Columns 20-27, Row 12) is completely blocked by a solid cliff face. Walking UP from Row 12 to Row 11 is 100% blocked on Column 21 and Column 22.
4. **The Column 29 Shrub Wall:** Column 29 has solid trees/shrubs on Rows 12-25, completely blocking ground-horizontal crossing. Crossing Column 29 is only possible on Row 26 (South) and Rows 10-11 (North).
5. **The Pond & Rest House 1:** Completely block the middle-western ground level on Rows 10-15 across Columns 9-19.

### The Ground-Level Eastern Passage Status
We have empirically verified that Column 28 is 100% OPEN and walkable on Rows 12-15 (verified on Turn 35165). This allows a highly optimized ground-level bypass route that completely circumvents the Central Plateau detour, saving 22 steps!

### 🚫 Verified Obstacles & Collision Coordinates (Safari Zone Center)
- **Signposts (Solid):** Located at `(13, 24)`, `(16, 24)`, `(22, 24)`, and `(27, 24)`. These are 2-tile high solid structures that block all horizontal and vertical passage.
- **The Ledge (Row 23):** South-facing ledge running from Column 0 to 29. Solid horizontally and UP from Row 24, except for the opening at `(15, 23)`.
- **Rhydon Statues & Fences (Row 25):** Completely solid from Column 0 to 29, separating the entrance from Row 26.
- **Column 29 Shrub Wall:** Solid green hedges running vertically on Column 29 from Row 12 to Row 25. Horizontal crossing is only possible on Row 26 (South) and Rows 10-11 (North).
- **Western Bypass Block (Column 8):** Ground-level Column 8 is physically blocked by a solid tree/bush at `(8, 15)` and a cliff wall at `(8, 13)`.
### 🧪 Verified Physical Boundaries & Collision Coordinates (Area 3 & Center)
- **Column 24 Hedge Wall (Area 3 West):** Solid vertical line of green hedges on Column 24 from Row 0 to Row 13. Rows 14-17 on Column 24 are open grass.
- **Row 19 Cliff Wall (Area 3 West):** Solid horizontal cliff face running across Rows 19-20 on Columns 9-22. Prevents any vertical ground-level traversal from south to north across Row 19.
- **Column 18 Vertical Barrier (Area 3 West):** Solid vertical tree barrier on Column 18 across Rows 20-23, blocking horizontal ground-level passage.
- **Row 24 Hedge Wall (Area 3 West):** Solid green hedges running horizontally on Row 24 across Columns 22-29, blocking all downward ground-level vertical passage.
- **Column 0-1 Tree Barrier (Area 3 West):** Solid tree trunks on Columns 0 and 1, Rows 24 and 25, blocking downward ground-level vertical passage.
- **Hedge-Maze Compartmentalization in Center:**
  - Row 15 has solid green hedges on Columns 6, 7, 8, 9.
  - Row 16 has solid green hedges on Columns 1, 2, 3, 4, 5.
  - This forms an interlocking hedge maze that completely prevents ground-level vertical passage from the Northwest Compartment of Center to the South/East Compartment.
- **Pond & Rest House 1 in Center:** Completely block the middle-western ground level on Rows 10-15 across Columns 9-19.
- **Center Compartment Wrapping:** The Northwest Compartment of Center is completely isolated from the South/East Compartment. Transitioning RIGHT from Area 3 (West) on Row 23/26 always warps the player into this isolated Northwest Compartment of Center. To enter the South/East Compartment, we must enter directly from the Gatehouse entrance at (15, 25).

### 🧪 Newly Verified Physical Boundaries & Collisions (Turns 35858-35971)
- **Column 5 Row 23 Solid Fence (Area 1 East):** Solid white horizontal wood fence bordering Row 23 from Column 5 onwards, completely blocking direct downward/horizontal movement on Row 23 and forcing a detour to Row 24.
- **Column 23 Row 24 Cliff Face (Area 2 North):** Solid cliff face bordering the Eastern Southern Plateau stairs on the East, completely blocking rightward movement at Row 24.
- **Column 15 Row 27 Cliff Wall (Area 2 North):** Solid cliff wall tile causing a bump when walking Up from `(15, 28)`.
- **Column 5 Shrub Barrier (Area 2 North):** Continuous dark green hedge/shrub wall from Row 20 to Row 33, completely blocking direct ground-horizontal crossing.
- **Row 34/35 Statue Barriers (Area 2 North):** Row 34 is blocked by statues across Columns 4-7 and Columns 10-11, with a walkable gap on Columns 8-9. Row 35 is blocked by statues at `(7, 35)` and `(10, 35)`.
- **Row 4 Column 26 Ledge (Area 3 West):** Solid horizontal ledge at `(26, 4)` preventing direct ground-level downward passage from `(26, 3)`.
