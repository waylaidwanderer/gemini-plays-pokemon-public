# Safari Zone - Overworld Layout & Navigation Guide

## Run Statistics (Current Run)
- **Start Turn:** 22902 (Fresh run, paid ¥500, received 30 Safari Balls, 500 step budget)
- **Current Turn:** 23071 (334 steps taken)
- **Steps Taken:** 334 steps
- **Remaining Steps:** 166 steps

## Area 0 (Center) Map & Collision Structures
- **Counter Barrier (Row 25):** Solid counters block columns 2-13.
- **Exit Triggers (14, 24) and (15, 24):** Stepping here triggers the "Leaving early?" dialogue with the gatekeeper, warping the player back to the lobby. Avoid stepping onto row 24 at column 14/15 if you wish to stay in the Safari Zone!
- **Bottom Highway (Row 26):** Completely open and connected grass corridor from Column 15 to Column 30.
- **East Boundary (Column 29):** Solid wall of trees except for openings at Y=11 and Y=23.
  - Transition at (29, 11) in Center warps the player to (0, 23) in Area 1 (East) with Y-offset of +12.
  - Transition at (29, 23) in Center warps the player to (0, 11) in Area 1 (East) with Y-offset of -12.

## Area 1 (East) Map & Collision Structures
- **Starting Pocket:** Column 0-5 on Rows 21-24 is a pocket bounded by hedges at Row 20 and Row 25.
- **Column 6 Barrier:** Blocked by a hedge at (6, 21) and mailboxes/posts at (6, 22) and (6, 23).
- **Opening at Row 24:** Row 24 is completely open at column 6, allowing players to walk East horizontally from the starting pocket along Row 24.
- **Western Grass Corridor:** Columns 8 and 9 are open grass corridors going UP from Row 22 to Row 7.
- **Central Pond Blockage:** Column 11/12 has a water pond on rows 10-11 and rows 14-16, but Row 9 and Row 8 are open grass across columns 11-13! This allows horizontal crossing of columns 11-13 along Row 9 or Row 8 to reach Column 12 on the ground level.
- **Northern Plateau Stairs (Stairs Entrance):** Located at `(12, 7)` facing south. Leads to the plateau at `(12, 6)`.

## Area 2 (North) Map & Collision Structures
- **Staircase Warps:**
  - Southern Stairs (Plateau Entrance): Located at `(22, 23)` facing south. Leads to plateau at `(22, 22)`.
  - Western Stairs: Located at `(16, 27)` facing west. Leads to ground level at `(16, 28)`.
  - East Stairs (Plateau Entrance): Located at `(32, 13)` and `(33, 13)` facing east on row 13.
- **Column 16 Barrier:** Blocked on ground level at Row 15 by a solid cliff wall. Traversal north must occur entirely ON TOP of the plateau, not on the ground!
- **Column 5 Barrier:** Solid vertical tree wall on Rows 26-33 on the ground level.

---

## Gold-Standard Speedrun Route to Area 3 (West)

To transition from the northwestern ground level to the southwestern exit of Area 2 (North) (which connects to Area 3 (West) and the Secret House), the player must use the eastern plateau stairs:

1. **Circumvent Rest House 2:** From column 19, walk Up to row 9 (open grass), then walk East to column 35 (bypassing the row 10 tree line).
2. **Access the East Stairs:** Walk Down column 35 to row 13, then walk west and climb UP onto the plateau using the stairs at `(32, 13)` or `(33, 13)`.
3. **Traverse the Plateau:** Walk south and west along the plateau structure to reach the southern cliffside.
4. **Reach Southern Ground Level:** Walk down the stairs or jump down the south-facing ledges at the south-eastern/south-middle part of the plateau to land on the southern ground level (rows 25-35).
5. **Walk West to Area 3:** Follow the open southern grass corridor west, detouring South to Row 34 or 35 to bypass the solid Column 5 tree barrier, then walk West past Column 5 and transition to **Area 3 (West)** at columns 0-4, rows 30-35.
