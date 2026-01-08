# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.

# Verified Obstacles
- (5, 10), (5, 12), (6, 6), (8, 9), (9, 12), (9, 13), (7, 11) are WALLs (pillars).
- Fran (4, 11) is an impassable NPC.

# Connectivity & Hypotheses
- (4, 13) is a FLOOR (4-way intersection).
- (7, 11) is a WALL (Verified Turn 34732).
- Hypothesis: Defeated trainer Cody (4, 1) is passable, allowing B6 to reach P2.

# Strategy: Blackthorn Gym 2F
- Step 1: Test passability of Cody (4, 1).
- Step 2: Test passability of (8, 8) and (8, 9).
- Step 3: Use BFS solver if any new paths are found.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).