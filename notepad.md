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
- Test 1: Talk to Cody at (4, 1). Result: Pending.
- Test 2: Attempt to move onto (4, 2).
- Test 3: Attempt to move onto (3, 0).
- Test 4: Attempt to move onto (3, 8).
- Test 5: Verify B8 status at (8, 12) or (8, 7).

# Puzzle Start Turn: 29931.