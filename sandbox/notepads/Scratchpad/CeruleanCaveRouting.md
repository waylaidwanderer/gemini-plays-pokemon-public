# Scratchpad: Cerulean Cave 2F Routing & Frontier Verification

## Objective
Establish an empirical path to Ladder A at (1, 3) leading to B1F (Mewtwo) through the 2F main maze.

## Verified Landmarks & Corridors
- Ladder B at (22, 6) connects down to Row 11 at (23, 11).
- Row 11 connects to Row 13 via (17, 11..13).
- Row 13 connects to Column 22 (22, 13..15) -> (21, 15..17) to Row 17.
- Row 17 connects east via Column 28 (28, 16..14) -> Column 26 (26, 14..9) -> (25, 9) into the Southwest Corridor toward (4, 15).
- TM14 Blizzard collected at (4, 15).
- Ladder A visually confirmed at (1, 3) with open floor at (0..7, 5).

## Unverified Frontier Hypothesis: SW-to-NW Vertical Corridor
- **Hypothesis**: The open floor at (4, 15) connects westward to Column 0/1 (0..1, 15) and runs northward along Column 0/1 up through rows 14..5 to connect with the open floor at (0..1, 5) leading directly into Ladder A (1, 3).
- **Frontier Verification Protocol**:
  1. Once arriving at (4, 15), halt macro-routing.
  2. Test westward tiles along Row 15: (3, 15), (2, 15), (1, 15), (0, 15).
  3. For each open column, test northward traversal row-by-row (Row 14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8 -> 7 -> 6 -> 5).
  4. Log exact coordinates, cardinal barriers, and turn numbers for every tested tile.
  5. If an impassable barrier is encountered, systematically test adjacent parallel columns (cols 1..4).