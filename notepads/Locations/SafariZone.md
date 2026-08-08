# Safari Zone - Overworld Layout & Navigation Guide

## Run Statistics (Previous Run - Ended)
- **Start Turn:** 23448 (Run ended due to step budget exhaustion on Turn 23787)
- **End Turn:** 23787
- **Result:** Explored Area 1 (East) and entered Area 2 (North) up to Column 25. Fully mapped the island plateau bypass in Area 1.

## Area 1 (East) Map & Transitions
- **Exit to Area 2 (North):** Located at (0, 5).

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

## Macro-Level Layout Connection in Area 1 (East)
To reach the northern exit at `(0, 5)` from the bottom-left entrance at `(0, 22)`, the player must navigate the map in a spiral/zig-zag topology:
1. **Southern Ground Level:** Walk east from `(0, 22)` on the ground to `(20, 21)`.
2. **Southern Plateau Crossing:** Climb stairs at `(20, 21)` to `(20, 20)`. Walk west on the plateau to `(12, 20)`. Descend stairs at `(12, 21)` to ground level at `(12, 22)`.
3. **Western/Middle Ground Level:** Walk north on columns 8-9 to row 8, then east to `(12, 8)`.
4. **Northern Plateau Crossing (East-Bound):** Climb stairs at `(12, 7)` to `(12, 6)` on the northern plateau. Walk east on the plateau to `(17, 6)`. Descend stairs at `(17, 7)` to the northeastern ground level at `(17, 8)`.
5. **Northeastern/Northern Ground Passage:** From `(17, 8)`, walk right to column 18/19/20, then walk UP past the row 6-7 barrier to row 5 (northern ground level).
6. **Northwest Ground Level Exit:** From the northern ground level, walk west all the way to the top-left corner at `(0, 5)` to transition to Area 2 (North) at `(39, 31)`.
## Safari Game Over Dialogue Flow & Reset Mechanics
When the 500 step budget expires:
1. **Dialogue Box 1:** `PA: Ding-dong!` -> press `A` or `B` to advance.
2. **Dialogue Box 2:** `Time's up! Your SAFARI GAME is over!` -> press `A` or `B` to advance.
3. **Automatic Warp:** Warps player to Safari Zone Gatehouse at `(4, 0)` facing DOWN.
4. **Dialogue Box 3:** `Did you get a good haul? Come again!` (renders in two chunks: "Did you get a good haul?" and "Come again!"). -> Press `A` or `B` to completely dismiss dialogue and return to overworld.
5. **Fuchsia City Reset:** Walk DOWN to Fuchsia City to reset the gatekeeper, then walk UP to re-enter. Speak to clerk at `(6, 2)` or counter at `(4, 2)` to start a new Safari run.
