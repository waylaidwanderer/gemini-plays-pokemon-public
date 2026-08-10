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

## Area 3 (West) Layout & Discoveries

### Map Transitions & Connections
- **Entered from Area 2 (North):** Transition from Area 2 (North) at `(4, 35)` leads directly into Area 3 (West) at `(26, 0)`.
- **East Edge Map Transition:** The far-right edge of Area 3 (West) at column 30, row 23 connects directly to Safari Zone Center at `(0, 11)`.

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

### 🔍 The Southern Ground Level Hypothesis
- **Theory:** The southern ground level of Area 3 (West) is hypothesized to contain the Gold Teeth and the Secret House (where HM03 Surf is obtained). It is a separate compartment in Area 3 (West). Its exact connection and access route from other Safari Zone areas (such as the southern corridor of Area 2 North or the West Compartment of Safari Zone Center) are currently unverified hypotheses that must be systematically tested and proven.

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

## 🧭 The Gold-Standard Speedrun Route to Area 3 (West)
1. **Safari Zone Center to Area 1 (East):** From (18, 25) entrance, walk to the transition to Area 1 (East) at (29, 11).
2. **Area 1 (East) to Area 2 (North):**
   - From (0, 23), walk Down/Right to (9, 24) to bypass the Rhydon statues.
   - Walk east to Column 20, climb the Southern Plateau stairs at (20, 21), walk west to (12, 20), descend stairs at (12, 21) to (12, 22).
   - Walk Left to Column 8, walk UP Column 8 to Row 8, walk East to (12, 8).
   - Climb Northern Plateau stairs at (12, 7) to (12, 6), walk east on plateau to (17, 6), descend stairs at (17, 7) to (17, 8).
   - Walk right to Column 20, walk UP Column 20 to Row 5, walk UP to Row 3.
   - Walk left to (7, 3), walk Down to (7, 5) (bypassing the building door at (6, 4) and tree at (5, 3)), walk Left along Row 5 to (0, 5) to transition to Area 2 (North) at (39, 31).
3. **Area 2 (North) to Area 3 (West):**
   - Walk Left along Row 31 to Column 22.
   - Walk UP Column 22 to (22, 23) and climb Western Southern Plateau stairs to (22, 22).
   - Walk West on plateau to (16, 22), walk Down Column 16 to (16, 27) (descending stairs), and walk to (16, 28) (ground level).
   - Walk Left to (12, 33), bypass Rhydon statues, and walk Left/Down to transition directly to Area 3 (West) at (26, 0).
