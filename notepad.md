# Warehouse Switch Puzzle - Solution
- Tile Types: `TYPE_3fe2` = Walkable (Blue Floor). `TYPE_2889` = Solid (Metal Plate).
- Mechanic: Switch 1 OFF closed Shutter 2 at (6, 8) (Changed 3fe2 -> 2889).
- Deduction: Switch 1 MUST BE ON to open Shutter 2.
- Conflict: Switch 1 ON also opens Shutter 1 (Trap Path).
- Solution: Turn Switch 1 ON, but ignore Shutter 1. Go through Shutter 2.
- Current Status: Turning Switch 1 ON.

## Plan
1. Interact with Switch 1 (Turn ON).
2. Move to (6, 8) via main corridor (Row 4/5).
3. Enter Shutter 2.
4. Proceed to Director (9, 12).