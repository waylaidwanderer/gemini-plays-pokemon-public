# Warehouse Switch Puzzle - Active
- Clue: "The switch on the end is the one to press first." -> Switch 3 (Left).
- Current State: Sw3 ON, Sw2 ON, Sw1 OFF.
- Problem: Path South from (6, 5) is BLOCKED at (6, 6) despite XML saying it's open.
- Hypothesis: Switch 2 ON might be blocking it? Or maybe I need a specific sequence.

## Plan
1. Confirm blockage at (6, 6) (Interact).
2. Go to Switch 2 (10, 1) and turn it OFF.
3. Check if (6, 6) opens with [Sw3 ON, Sw2 OFF, Sw1 OFF].
4. If that fails, Reset All to OFF and start fresh with Switch 3.