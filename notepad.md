# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763 (Jan 8, 10:15 AM)
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7)
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 15)
- Status: Strength ACTIVE (Turn 34932)

## Tile Mechanics (2F)
- Vertical Barriers: Column 4 (Row 0-12), Column 2 (Row 10-17), Column 9 (Row 12-17).
- Center Block: (6, 2-4, 6), (7, 4, 6).
- Navigation Gaps: (4, 13) connects left/right, (5, 4) is a narrow vertical passage.
- Dead Ends: Column 8 (Row 10-17) is blocked by walls at (8, 8-9).

## Puzzle Plan
- Goal: Move B8 from (8, 15) to P3 (8, 7) or P1 (8, 3).
- Obstacle: Walls at (8, 8-9) block direct northern movement.
- Strategy: Push B8 south to (8, 16), then navigate to (8, 16) to push it north? No, that doesn't solve the wall at (8, 9).
- Alternative: Push B8 to a gap. (7, 13) is FLOOR. Can B8 be pushed to (7, 13)? Requires player at (9, 13), but (9, 13) is WALL.
- Verification: Use `puzzle_strategist` to audit the wall at (9, 13) and (8, 8-9).

## Training Strategy
- Location: Route 45 grass (near 15, 60).
- Goal: Xenon (Haunter) and Kimchi (Gloom) to Lv40.
- Start Turn: 30928.
- Progress: Haunter Lv36, Gloom Lv33.