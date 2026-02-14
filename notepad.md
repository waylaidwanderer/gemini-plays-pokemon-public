# Warehouse Switch Puzzle - Active
- Clue: "The switch on the end is the one to press first." -> Switch 3 (Left) correct.
- Current State: Sw3 ON, Sw2 ON, Sw1 OFF.
- Map Data: Shutter (6, 8) is OPEN (TYPE_2889 in XML).
- Obstacle: Trainer at (4, 8) guarding the path.
- Trap Check: (12, 9) is a trap. (6, 9) is likely safe (Parallel structure: Left = Safe, Right = Trap).

## Plan
1. Move South to (6, 8).
2. Engage/Defeat Trainer at (4, 8).
3. Proceed to (6, 9) -> (9, 12).
4. Save Director.