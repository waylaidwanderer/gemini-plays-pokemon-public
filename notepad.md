# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable. (8, 8) is solid (verified Turn 30113).
- PIT: Player falls to 1F. Boulder destination. (8, 7) is currently empty.
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Inactive (Lost Turn 30108).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.

# Strategy: Boulder Puzzle
- Goal: Drop all boulders into pits.
- Current Status: B8 is at (8, 11). Strength is OFF.
- Plan:
  1. Navigate to (8, 10).
  2. Face down, press A to activate Strength on B8.
  3. Push B8 down to (8, 12).
  4. Re-run solve_blackthorn_boulders.
- Hypothesis: B8 needs to detour through Row 13 to reach the left side or Row 1 to reach (8, 3).