# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable silver blocks. 
- PIT: Player falls to 1F. Boulder destination.
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Inactive (Lost Turn 30108 via ladder).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.
- Verified Walls: (4, 5), (9, 13), (2, 13), (3, 0), (7, 10), (7, 11).

# Strategy: Boundary Testing
- Goal: Find the "fake" wall or path that makes the puzzle solvable.
- Test 1: Is (8, 8) or (8, 9) passable? (Allows B8 to reach (8, 7)).
- Test 2: Is (4, 3) or (4, 2) passable? (Allows B6 to reach (2, 5)).
- Test 3: Is (6, 0) passable? (Allows pushing B7 Down).
- Plan:
  1. Navigate to (7, 8).
  2. Attempt to move Right to (8, 8).
  3. Navigate to (8, 12), face B8 at (8, 11), and press A to activate Strength.
  4. Push B8 UP to (8, 10) and test (8, 9).