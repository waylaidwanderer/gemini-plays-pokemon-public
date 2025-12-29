# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable silver blocks. Absolute barrier.
- PIT: Player falls to 1F. Boulder destination.
- LADDER: Warp between floors. Resets boulder positions. Deactivates Strength.
- Strength: Active (Turn 30101).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.
- Blockages: Column 4 wall Row 0-12. Column 2 wall Row 10-17. Row 8 wall at (2,8)-(4,8).
- Reset Required: Completed. Boulders are at their initial positions.
- Strength: Inactive (Turn 30126). Reset by ladder warp.

# Strategy: Reactivate and Solve
- Phase 1: Reactivate Strength.
- Phase 2: Use `run_code` to calculate the full 3-boulder sequence from the initial state.
- Initial State Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Initial State Pits: (2, 5), (8, 3), (8, 7).

# Progress Log
- Turn 30121: Dialogue cleared. B8 marker corrected. Reset initiated.