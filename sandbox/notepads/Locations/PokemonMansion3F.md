# Pok�mon Mansion 3F - Map & Navigation Log

## Physical Barriers & Solid Walls (Verified Turn 69876)
- **Column 1 Row 9 is a Solid Wall:** Column 1 Row 9 is NOT a shutter gate. It is a permanent, solid partition wall that blocks vertical passage across Row 9 on Columns 1-7 in both State A and State B.
- **Row 12 Column 2 Shutter Gate:** Walkable in State A, CLOSED and impassable in State B.
- **Column 10 Vertical Corridor:** Column 10 is completely open and walkable on Rows 9-16 on 3F West (unlike 2F West where it is blocked by rubble), providing the primary vertical passage between the northern and southern halves of 3F West.
- **Row 8 Debris:** Blocked by solid rubble on Columns 8-11, making Row 8 impassable horizontally on these columns.
- **Column 12 Vertical Passage:** Completely open vertically on Rows 6-12, providing an alternate vertical passage on 3F West.
- **Column 19 Row 17 Solid Wall (Verified Turn 67854):** Column 19 Row 17 is a permanent, solid wall/cabinet structure in both State A and State B, blocking direct vertical passage down Column 19 from Row 16 to the balcony.

## 3F East - Mapping & Boundaries
- **Column 22 Partition Wall:** Solid vertical wall separating Columns 23-28 from Columns 15-21 on Rows 4-11.
- **Row 3 Horizontal Opening:** Row 3 is completely open across Column 22, allowing horizontal passage between 3F West/Middle and the northeastern Scientist room.
- **Row 8 Solid Partition Wall:** Solid horizontal wall on Columns 24-28, completely isolating the northeastern room (Rows 4-7, Columns 23-28) from the southern half of 3F East in both states.

## State A vs State B Gate Configurations (Verified Turn 69876)
- **State B (Default):**
  - Shutter gate at `(25, 13)` on Column 25 is CLOSED.
  - Shutter gate at `(4, 6)` on 3F West is OPEN.
  - Shutter gates at `(19, 2)` and `(21, 2)` on 3F East are CLOSED.
  - Shutter gate at `(21, 17)` on Column 21 (Balcony) is CLOSED.
  - The northeastern Scientist room on 3F East is completely isolated in State B.
- **State A:**
  - Shutter gate at `(25, 13)` on Column 25 is OPEN.
  - Shutter gate at `(4, 6)` on 3F West is CLOSED.
  - Shutter gates at `(19, 2)`, `(21, 2)` on 3F East are OPEN.
  - Shutter gate at `(21, 17)` on Column 21 (Balcony) is OPEN.
  - This allows horizontal crossing between 3F East and the southern half of 3F East via Row 2, Column 21 (gate at (21, 5) is OPEN in State A).

## The Intended Mansion 3F Puzzle Solution (State A Route)
1. **Verify State A:** The active Mewtwo switch pedestal on 3F West is located at `(2, 5)` (interact from `(2, 6)` facing UP, or `(1, 5)` facing RIGHT, or `(3, 5)` facing LEFT).
2. **Walk to 3F East Southern Room:** 
   - Walk UP Column 10 to Row 2.
   - Walk RIGHT along Row 2 past Column 22 (open in State A).
   - Walk DOWN Column 21 to Row 12 (gate at (21, 5) open in State A).
   - Walk RIGHT along Row 12 to Column 25.
   - Walk DOWN Column 25 past the open gate at (25, 13) to (25, 14).
3. **Fall through Pitfall (State A):** Walk onto the active pitfall in the southern half of 3F East to fall to the 1F East fenced room.


## Verified Layout & Obstacle Mapping (State-Dependent - Turn 70139)
- **Column 11 Row 16 is a Solid Wall:** Column 11 Row 16 is a permanent, solid vertical partition wall panel on 3F, preventing horizontal travel along Row 16 between 3F West and 3F East.
- **Row 6 Column 22 is a Solid Wall:** Column 22 Row 6 is a solid vertical wall panel, preventing horizontal crossing of Row 6 across Column 22.
- **Column 19 Row 7 is a Solid Wall:** Column 19 Row 7 is a permanent solid horizontal wall panel on Rows 7-8 on Columns 18-22. This blocks vertical passage down Column 19 from Row 6.
- **Row 4 Column 23-25:** Open and walkable floor in the vertical corridor on Column 23.
- **Column 26 Row 13 is a Solid Wall:** Column 26 Row 13 is a permanent solid wall panel, NOT a gate.
- **Column 25 Row 13 Shutter Gate:** OPEN in State A (pink checkered floor), CLOSED and blocked in State B.
- **Column 21 Row 17 Shutter Gate (Balcony):** OPEN in State A, CLOSED and blocked in State B.
- **The Only Valid Route to Balcony (State A):** Walk DOWN Column 26 to Row 12, LEFT Row 12 to Column 24, DOWN Column 24 to Row 16, LEFT Row 16 to Column 21, DOWN Column 21 past the open gate at (21, 17) to Row 18, LEFT Row 18 to Column 19 (balcony drop), and drop!

## Verified Layout & Obstacle Mapping (Turn 70613)
- **Obstacle at (12, 13):** Column 12 is blocked at Row 13 by a solid wall/cabinet structure.
- **Closed Gate at (14, 7) and (15, 7) in State A:** Closed shutter gates block vertical travel down Columns 14 and 15 in State A. These gates are OPEN in State B!
- **Rubble Block at (22, 12) and (23, 12):** Solid rubble permanently blocks horizontal travel along Row 12 between Columns 21 and 24.
- **Column 17 Vertical Pathway:** Completely open and walkable vertically from Row 3 to Row 12. No shutter gates block Column 17 on Row 7!
- **Row 16 and Column 12 Connection:** Completely open and gate-free in both State A and State B. Row 16 connects Column 12 to Column 21. Column 12 connects Row 11 to Row 16!
- **True Balcony Drop Solution:**
  1. Toggle Mansion to State B on 3F West.
  2. Walk to 3F East via Row 3, go down Column 14/15/17 (open in State B) to Row 16, and walk to (21, 16).
  3. Walk back to 3F West via Row 16 (open in State B), Column 12 (open in State B), Row 11, and stand at (3, 11).
  4. Toggle Mansion to State A. This opens the balcony gate at (21, 17)!
  5. Walk from (3, 11) to the balcony in State A: Right along Row 11 to Column 12, DOWN Column 12 to Row 16, RIGHT along Row 16 to (21, 16), and DOWN past the open gate at (21, 17) to Row 18, Left to Column 19, and drop!