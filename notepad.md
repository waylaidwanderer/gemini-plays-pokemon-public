# Tile Mechanics (Global)
- FLOOR: Passable terrain.
- WALL: Impassable silver blocks. Absolute barrier.
- PIT: Player falls to 1F. Boulder destination (forms bridge on 1F).
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Active (Turn 30101). Verified: Pushing B8 worked at Turn 30116.

# Blackthorn Gym 2F State (Reset Status)
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 10).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.
- Choke Point: Column 4 is a wall from Row 0-12. Row 13 is the only horizontal crossing.
- B8 Status: At (8, 10). Pushed north once.

# Time Tracking
- Puzzle Start Turn: 29931.
- Current Attempt Start: Turn 30104.
- Note: Puzzle resets whenever leaving the gym or floor (via ladder). All boulders must be pushed in one session.

# Strategy: Boulder Puzzle
- Goal: Fill all three pits.
- Plan:
  1. Move to (8, 11) to get behind Boulder 8.
  2. Use `puzzle_analyst` and `solve_blackthorn_boulders` (dynamic) to find the solution.
  3. Execute pushes for B8, then B6 and B7.