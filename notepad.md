# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable silver blocks. 
- PIT: Player falls to 1F. Boulder destination.
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Active (Turn 30101).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Solid.
- Choke Point 1: B8 at (8, 11). To reach Pit (8, 7), it must go through (8, 10), (8, 9), (8, 8). 
- Choke Point 2: Walls at (8, 9) and (8, 8) block Column 8.
- Choke Point 3: Wall at (7, 10) and (7, 11) block pushing B8 Right into Column 9.

# Strategy: Testing Boundaries
- Hypothesis: One of the silver blocks in the right quadrant is passable.
- Test 1: Is (7, 10) or (7, 11) passable? (Allows pushing B8 Right).
- Test 2: Is (8, 8) or (8, 9) passable? (Allows pushing B8 Up).
- Plan:
  1. Navigate to (6, 10).
  2. Attempt to move Right to (7, 10).
  3. Navigate to (6, 8).
  4. Attempt to move Right to (7, 8) then to (8, 8).