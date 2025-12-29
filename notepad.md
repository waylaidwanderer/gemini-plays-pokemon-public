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
- Strength: Active (Turn 30130). Activated on Boulder 8 at (8, 14).

# Strategy: Reactivate and Solve
- Phase 1: Reactivate Strength.
- Phase 2: Use `run_code` to calculate the full 3-boulder sequence from the initial state.
- Initial State Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Initial State Pits: (2, 5), (8, 3), (8, 7).

# Progress Log
- Turn 30121: Dialogue cleared. B8 marker corrected. Reset initiated.

# Hypothesis Testing: Boulder 8 Path
- Observation: Mental Map shows WALL at (8, 9) and (8, 8).
- Hypothesis: Tiles (8, 9) and (8, 8) are actually FLOOR, allowing Boulder 8 to reach pit (8, 7).
- Test: Push Boulder 8 north from (8, 11) to (8, 7).
- Step 1: Push to (8, 10). (In progress)