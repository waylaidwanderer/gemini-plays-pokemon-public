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

### Verified Empirical Sector Geometry (Turns 36192-36203)
- **Middle Grass Pocket (`cols 30-33, rows 8-12`)**:
  - West: Column 29 solid rock cliff wall from row 7 to row 13. Zero westward passages.
  - North: Row 7 south-facing ledge.
  - South: Row 13 south-facing ledge.
  - East: Column 34 statues. The ONLY east exit is at (34, 12).
- **Lower Road (`cols 0-39, rows 14-15`)**:
  - Row 13 is an unbroken south-facing ledge from col 39 to col 1. One-way return to Viridian City.
- **East Sector (`cols 35-39, rows 6-12`)**:
  - Open grass and paved road connecting to Viridian City.
- **Upper Highway (`cols 8-35, rows 4-5`)**:
  - Unbroken open brick road leading directly to Gatehouse at (8, 5).