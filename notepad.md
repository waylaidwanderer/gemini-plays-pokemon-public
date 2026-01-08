# Blackthorn Gym (Puzzle Progress)
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14) [Current Positions].
- Reset Mechanic: Ladders (1, 7) and (7, 9) reset 2F boulders.
- Push Mechanic: Player stays in tile after push.
- Status: Strength is ACTIVE. B6 is at (3, 3).

# Verified Obstacles (2F)
- (4, 1): Cody NPC. Impassable.
- (4, 0-12): WALLs or NPC. No horizontal passage except (4, 13).
- (4, 13): FLOOR. The only gap between Left and Right sides.
- (8, 4), (8, 8, 9): WALL.
- (6, 2, 3, 4, 6): WALL.

# Puzzle Analysis (2F)
- B6 (3, 3) must likely go to P2 (2, 5).
- Path for P2: Boulder must enter from (2, 6) pushing UP, or (1, 5) pushing RIGHT.
- Accessing P2 from (2, 6) requires standing at (2, 7) (FLOOR).
- Accessing P2 from (1, 5) requires standing at (0, 5) (FLOOR).
- B6 can reach the bottom area (Row 13) by pushing DOWN through Col 3.
- B8 (8, 14) can reach (4, 13) to cross to the left side.

# Strategy: Blackthorn Gym 2F
- Step 1: Move player to (0, 1) to avoid blocking BFS.
- Step 2: Run solve_puzzle_v5.
- Step 3: Execute sequence.