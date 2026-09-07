# Route 22 Traversal & Mapping Scratchpad

## Goal: Clean Traversal from Viridian City to Route 22 Gatehouse at (8, 5)

### Viridian City Navigation Rules
- When outside Pokémon Center at (23, 26), DO NOT walk south into row 27 (row 27 is a south-facing ledge).
- Path to Route 22:
  1. From (23, 26): Walk Left to col 19 at (19, 26).
  2. Walk Up along col 19 to row 18 at (19, 18).
  3. Walk Left along row 18 to col 4 at (4, 18).
  4. Walk Up along col 4 to row 14 at (4, 14).
  5. Walk Left along row 14 to (0, 14) to enter Route 22 at (39, 6).

### Route 22 Empirical Probe Log & Negative Constraints
- **Turn 36130 Lower Road Probe**: Tested columns 8 down to 0 along row 14/15. Confirmed that row 13 is an unbroken, impassable south-facing cliff ledge from column 39 all the way to column 1 with ZERO northward passages.
- **Rule**: Lower road (rows 14-15) is strictly a one-way return avenue to Viridian City.
- **Rule**: NEVER step south into row 13/14 when traveling west.

### Route 22 Upper/Middle Tier Probing Plan
- Enter Route 22 at (39, 6).
- Step Left to (35, 6), Down to (35, 12), Left through statue gap at (34, 12) to (33, 12).
- From (33, 12), step IMMEDIATELY UP into middle grass at (33, 11) -> (33, 9).
- Probe westward corridor along rows 8-9 across columns 33 down to 8 to reach Gatehouse at (8, 5).