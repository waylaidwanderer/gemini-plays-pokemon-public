# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 10).
- Status: Strength is ACTIVE.

# Game Mechanics
- Strength: Deactivated when changing maps or using ladders. Must be re-activated by interacting with a boulder.
- Pushing: Pushing a boulder keeps the player in their current tile. (Verified Turn 34832).
- Ladders: (1, 7) and (7, 9) reset boulder positions on 2F.

# Tile Mechanics (2F)
- WALL: Impassable. (4, 0, 2-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11), (9, 12-17).
- GAP: (4, 1) and (4, 13-17) are passable.
- LADDER: Walkable for player, impassable for boulders.
- PIT: Impassable for player (warp), target for boulders.

# Strategy: Blackthorn Gym 2F
- Step 1: Define robust BFS tool for boulder navigation with 'stay in place' mechanic.
- Step 2: Solve puzzle.

# Training Progress
- Goal: Xenon and Kimchi to Lv40.
- Started: Turn 30928 (Approx).
- Progress: Xenon Lv36, Kimchi Lv33.