# Pokémon Mansion 3F - Map & Navigation Log

## Layout & Spatial Boundaries (Verified)
- **Column 10 Vertical Corridor:** Column 10 is completely open and walkable on Rows 9-16 in both State A and State B, allowing vertical passage between the northern and southern halves of 3F West.
- **Rubble block at (2, 11):** The Mewtwo statue pedestal at `(2, 11)` behaves as a solid block.
- **Rubble block at (23, 7):** Column 23 Row 7 contains solid rubble and is completely impassable.
- **Blocked tiles at (28, 4):** On 3F East, `(28, 4)` is blocked on Down and Left.
- **Pitfall Trap at (26, 6):** The pitfall trap on 3F East is located at `(26, 6)`. Walking onto `(26, 6)` drops the player down to 1F East at `(25, 6)`.
- **Row 3 horizontal crossing:** Row 3 is open horizontally from Column 20 to Column 26.

## Turn 66391 - Empirical Boundary Verification
- Standing at `(9, 11)` on 3F West in State B:
  - `(9, 10)` (UP) is OPEN.
  - `(9, 12)` (DOWN) is BLOCKED (solid wall/rubble).
  - `(8, 11)` (LEFT) is OPEN.
  - `(10, 11)` (RIGHT) is BLOCKED (the Row 11/12 shutter gate is closed in State B!).
- Therefore, direct horizontal crossing to 3F East on Row 11 is blocked in State B. We must find another way to cross Column 10/11.
- **Solid Wall at Column 4 Row 8:** Column 4 Row 8 has been physically verified to be a solid permanent vertical wall separating Columns 1-3 from Column 5 (Turn 66401).
- **Gate at (2, 12) is CLOSED in State B:** Standing at `(2, 13)` and trying to walk UP to `(2, 12)` fails in State B (Turn 66415).