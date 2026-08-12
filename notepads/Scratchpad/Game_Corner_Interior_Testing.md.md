# Game Corner Interior Empirical Testing Log

## Single-Stepping Tile Passability Protocol (Turn 51111)
- Current Position: (6, 7) facing Right in Celadon Game Corner.
- Goal: Systematically test tile passability 1 step at a time across Columns 6 through 12 to reach East Casino floor (x>=10).
- Rules: Never issue 'Down' while at y=7 (exit mat). Always verify tile passability before issuing multi-step macros.

## Verified Tile Log
- (3, 7) / (4, 7): Exit mats (warps outside if 'Down' is pressed).
- (5, 7) / (6, 7): Open carpet on Row 7 cross-aisle.
- (6, 5), (6, 4), (6, 3), (6, 2), (6, 0): Solid obstacles along Column 6.
- Testing (7, 7) from (6, 7).