# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 10).
- Status: Strength is ACTIVE.

# Game Mechanics
- Strength: Deactivated when changing maps or using ladders. Must be re-activated on a boulder.
- Pushing: First push (with text box) -> Player stays in place. Subsequent pushes -> Player moves into boulder's old tile. (Verified Turn 34813, 34815, 34833).
- Ladders: (1, 7) and (7, 9) reset boulder positions on 2F.

# Tile Mechanics (2F)
- WALL: Impassable. (4, 0-10, 12), (2, 8), (3, 8), (4, 8), (7, 10, 11), (9, 12-17).
- GAP: (4, 1) and (4, 13-17) are passable.
- Verification Needed: Are (8, 8) and (8, 9) walls? (Testing at Turn 34835).

# Strategy: Blackthorn Gym 2F
- Step 1: Test Column 8 walls by pushing B8 UP.
- Step 2: Use BFS solver (run_code) with verified layout.