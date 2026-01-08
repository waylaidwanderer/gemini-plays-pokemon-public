# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763 (Jan 8, 10:15 AM)
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7)
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 15)
- Status: Strength ACTIVE (Turn 34932)

## Tile Mechanics (2F)
- WALL: XML data + (4, 1), (4, 11), (1, 7), (7, 9)
- PIT: (8, 3), (2, 5), (8, 7)
- LADDER: (1, 7), (7, 9)
- FLOOR: (6, 10), (4, 13) gap

## solve_boulders Schema Reminder
- boulders: {"ID": [X, Y], ...}
- player_pos: [X, Y]
- walls: [[X, Y], ...]

## Puzzle Strategy
- Step 1: Call `solve_boulders` with exact [X, Y] coordinates and string IDs.
- Step 2: Ensure walls list includes XML walls, NPCs, and ladders.

## Training Strategy
- Location: Route 45 grass (near 15, 60).
- Goal: Xenon (Haunter) and Kimchi (Gloom) to Lv40.
- Start Turn: 30928.
- Progress: Haunter Lv36, Gloom Lv33.