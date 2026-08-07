# Safari Zone - Overworld Layout & Navigation Guide

## Run Statistics (Previous Run - Ended)
- **Start Turn:** 23448 (Run ended due to step budget exhaustion on Turn 23787)
- **End Turn:** 23787
- **Result:** Explored Area 1 (East) and entered Area 2 (North) up to Column 25. Fully mapped the island plateau bypass in Area 1.

## Active Run Statistics (Current Run)
- **Current Position:** `(8, 10) (Safari Zone Area 1 - East, Ground Level)`
- **Steps Taken:** 216
- **Steps Remaining:** 284

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

---

## Gold-Standard Speedrun Route to Area 3 (West)

To transition from the northwestern ground level to the southwestern exit of Area 2 (North) (which connects to Area 3 (West) and the Secret House), the player must use the eastern plateau stairs:

1. **Circumvent Rest House 2:** From column 19, walk Up to row 9 (open grass), then walk East to column 35 (bypassing the row 10 tree line).
2. **Access the East Stairs:** Walk Down column 35 to row 13, then walk west and climb UP onto the plateau using the stairs at `(32, 13)` or `(33, 13)`.
3. **Traverse the Plateau:** Walk south and west along the plateau structure to reach the southern cliffside.
4. **Reach Southern Ground Level:** Walk down the stairs or jump down the south-facing ledges at the south-eastern/south-middle part of the plateau to land on the southern ground level (rows 25-35).
5. **Walk West to Area 3:** Follow the open southern grass corridor (around row 30) all the way west to the bottom-left corner of Area 2 (North) (columns 0-4, rows 30-35) to transition to **Area 3 (West)**.
## Verified Traversal Path & Environmental Discoveries (Current Run)

We have systematically traversed and verified the following segments, establishing the definitive overworld layout of Safari Zone Center and Area 1 (East):

1. **Safari Zone Center Entrance:** Spawned at `(14, 25)`.
2. **First East Transition Test (Stale Run):** Left Center at `(29, 11)`, warping to Area 1 (East) at `(0, 23)` (pocket). This pocket is bounded by trees on Row 20 and Column 6, making it a dead end. We returned to Center at `(29, 10)` via the `(0, 23)` -> `(29, 10)` reciprocal transition.
3. **Second East Transition Test (Active Run):** Walked north along Column 28 in Center to `(28, 10)`, then Right to `(29, 10)`, warping to Area 1 (East) at `(0, 22)` (pocket).
4. **Pocket Bypass (Row 24 Corridor):** From `(0, 22)` in Area 1, walked East to `(4, 22)`, Down to Row 24 at `(4, 24)`, and East along Row 24.
   - *Collision Check:* Attempted to go Up at `(12, 24)` and bumped at `(12, 23)`. Row 23 is a continuous solid tree line from Column 8 to 16.
   - *Collision Check:* Attempted to go Up at `(17, 24)` and bumped at `(17, 21)`. Row 21 is a continuous solid rocky cliff from Column 13 to 22.
5. **Plateau Ascent (Southern Stairs):** Walked East along Row 22 to Column 20, and climbed UP the southern stairs at `(20, 21-20)` to reach `(20, 19)` on the plateau.
6. **Eastern Plateau Dead End:**
   - Walked north to `(21, 12)`. Confirmed Row 12 has a solid cliff wall blocking northern progress.
   - Walked east and descended the eastern stairs at `(24, 15)` to ground level at `(24, 16)`. Bounded by cliffs on the West/North and trees on the East/South, this is a dead end. Collected the Poké Ball item in this pocket, then walked back up the stairs to the plateau at `(24, 14)`.
7. **Plateau West Crossing (Island Pond Bypass):** Bypassed the central plateau pond (Columns 16-19, Rows 15-17) by walking around its southern edge:
   - Walked Left to `(21, 14)`, Down Column 21 to `(21, 18)`, Left to `(20, 18)`, Down to `(20, 19)`, and Left along Row 19 to `(14, 19)`.
8. **Southwest Stairs Descent:** Reached the top of the southwest stairs at `(12, 20)`. Walked Down through the stairs at `(12, 21)` to reach the western ground level at `(12, 22)`.
   - *Socratic Collision Proof:* Walking Up from `(11, 18)` to `(11, 17)` bumps because the staircase facing West has a solid southern cliff face on Row 18. Entering the stairs must be done from the East at Column 12 or the West at Column 10.
