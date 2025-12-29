# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable silver blocks.
- PIT: Warp for player (to 1F), destination for boulders.
- LADDER: Warp between floors.
- Strength: Active (Turn 30009). Required to push boulders.

# Blackthorn Gym 2F State
- Boulders: B6 (3, 6), B7 (6, 1), B8 (8, 12).
- Pits: (2, 5), (8, 3), (8, 7).
- B8 Status: Marker says (8, 12). Overwatch suggests it might be in (8, 7). Need to verify.
- NPCs: Cody (4, 1), Fran (4, 11). Both defeated.

# Strategy: Breaking the Deadlock
- Problem: Idealized BFS says puzzle is impossible with current WALL layout.
- Hypothesis: One or more "WALL" tiles are actually passable, or NPCs move.
- Test 1: Is (4, 1) (Cody's tile) passable? Result: NO (Turn 30080).
- Test 2: Is (3, 0) a fake wall? Result: NO (Turn 30070).
- Test 3: Is (2, 13) actually a WALL? Result: YES (Turn 30021).
- Test 4: Is (4, 5) a fake wall? Result: YES (Turn 30059).
- B8 Status: Need to verify if it's at (8, 12) or in pit (8, 7).

# Puzzle Start Turn: 29931.