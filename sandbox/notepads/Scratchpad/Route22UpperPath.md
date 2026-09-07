# Route 22 Traversal & Mapping Scratchpad

## Goal: Clean Traversal from Viridian City to Route 22 Gatehouse at (8, 5)

### Viridian City Navigation Rules
- When outside Pokémon Center at (23, 26), DO NOT walk south into row 27 (row 27 is a south-facing ledge).
- Path from Pokémon Center (23, 26) to Route 22:
  1. (23, 26) -> Left 3 to (20, 26).
  2. Up 8 along col 20 to row 18 at (20, 18).
  3. Left 16 along row 18 to col 4 at (4, 18).
  4. Up 4 along col 4 to row 14 at (4, 14).
  5. Left 5 along row 14 to (0, 14) to enter Route 22 at (39, 6).

### Northwest Cut Corridor Constraint
- In Viridian City, row 4 across columns 14..6 is an open lawn behind the Cut tree at (14, 4).
- The western boundary at column 5 is a solid vertical tree/cliff wall with ZERO westward passage directly into Route 22.
- Column 6 connects south to row 14, leading to the west exit at (0, 14).

### Route 22 Empirical Map & Negative Constraints
- **Lower Road (rows 14-15)**: Row 13 is an unbroken, impassable south-facing cliff ledge from column 39 to column 1 with ZERO northward passages. Lower road is strictly a one-way return avenue to Viridian City.
- **Rule**: NEVER step south into row 13/14 when traveling west.
- **Battle Protocol in Grass**: DO NOT use 'Down' to run from battles in the middle grass (to prevent leaking downward inputs into overworld). Instead, press 'A', 'A' to one-shot wild Pokémon with lead Blastoise (Lv 72).

### Route 22 Middle Corridor Traversal Steps
1. Enter Route 22 at (39, 6).
2. Walk Left to (35, 6), Down to (35, 12), Left 2 through statue gap at (34, 12) to (33, 12).
3. From (33, 12), step IMMEDIATELY UP 4 steps into middle grass to row 8 at (33, 8).
4. Walk WEST along row 8 across columns 33 down to 8 to reach (8, 8).
5. Walk North 3 steps to (8, 5) and step into the Gatehouse door.