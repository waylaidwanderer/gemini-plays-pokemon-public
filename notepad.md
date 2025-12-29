# Blackthorn Gym Boulder Puzzle
- Start Turn: 30123
- Boulders (Verified): B7 (3, 3), B8 (6, 1), B9 (8, 13).
- Boulders (Searching): B6 (Initial pos 6, 7).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.
- Strength: Active.

# Strategy: Final Verification
1. Navigate to (6, 7) to confirm if B6 exists at its initial position.
2. Once all boulders are located, use run_code to find the definitive solution path.
3. Execute the solution strictly following the path.

# Verified Map Constraints (XML)
- Row 0 and Row 17: Boundaries.
- Column 0 and Column 9: Boundaries.
- Column 2 Wall: Rows 10-17.
- Column 4 Wall: Rows 2-10, 12.
- Column 6 Wall: Rows 2-4, 6, 8.
- Column 8 Wall: Rows 8-9.