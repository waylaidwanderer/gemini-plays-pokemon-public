# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763 (Jan 8, 10:15 AM)
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7)
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 15)
- Status: Strength ACTIVE (Turn 34932)

## Tile Mechanics (2F)
- WALL: (0, 0-17), (9, 0-17), (4, 0-12), (6, 2-4, 6), (7, 4, 6, 10, 11, 14, 15), (8, 0, 4, 8, 9), (2, 2, 8, 10-17), (5, 0, 10, 12, 16, 17), (3, 0, 8), (1, 0, 2)
- PIT: (8, 3), (2, 5), (8, 7)
- LADDER: (1, 7), (7, 9)
- FLOOR: (6, 10), (5, 4) gap, (4, 13) gap

## Puzzle Strategy (2F) - Systematic Re-Verification
- Hypothesis: Some "confirmed" walls are actually floor tiles, creating a path for B8.
- Goal: Verify every "Confirmed WALL" marker in the central and right areas.
- Current Plan:
  1. Test (5, 10) -> Result: WALL (Turn 34973).
  2. Test (6, 10) -> Result: FLOOR (Turn 34914).
  3. Test (7, 10) -> Result: WALL (Turn 34898).
  4. Test (8, 9) and (8, 8) -> Result: WALL (Turn 34903, 34925).
  5. Test (6, 6) and (7, 6) -> Result: WALL (Turn 34910, 34908).
- Observation: B8 (8, 15) is trapped by walls at (7, 15), (7, 14), (8, 8), (8, 9), (9, 15).
- New Hypothesis: B8 must be pushed through the gap at (4, 13) to reach the pits on the left? No, pits are at (8,3), (2,5), (8,7). P2 (2,5) is on the left. P1 and P3 are on the right.
- Goal: Find path for B8 to (8, 7) and (8, 3).

## Training Strategy
- Location: Route 45 grass (near 15, 60).
- Goal: Xenon (Haunter) and Kimchi (Gloom) to Lv40.
- Start Turn: 30928.
- Progress: Haunter Lv36, Gloom Lv33.