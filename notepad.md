# Warehouse Switch Puzzle - Active
- Clue: "The switch on the end is the one to press first." -> Switch 3 (Left).
- Current State: Sw3 ON, Sw2 ON, Sw1 OFF.
- Problem: Path South from (6, 5) blocked. Metal plate at (6, 6) is solid.
- Hypothesis: Switch 2 ON is keeping the (6, 6) shutter closed.
- Goal: Turn Switch 2 OFF.

## Plan
1. Move to (10, 2) (Below Switch 2).
2. Turn Switch 2 OFF.
3. Return to (6, 5) and check path South.
4. If failed, reset all switches.