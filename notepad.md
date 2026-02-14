# Warehouse Switch Puzzle - Solution
- Tile Types: `TYPE_3fe2` = Walkable (Blue Floor). `TYPE_2889` = Solid (Metal Plate).
- Mechanic: Switch 1 OFF closed Shutter 2 at (6, 8) (Changed 3fe2 -> 2889).
- Deduction: Switch 1 MUST BE ON to open Shutter 2.
- Conflict: Switch 1 ON also opens Shutter 1 (Trap Path).
- Solution: Turn Switch 1 ON, but ignore Shutter 1. Go through Shutter 2.

## Plan
1. Go to Switch 1 (16, 1).
2. Turn Switch 1 ON.
3. Verify Shutter 2 (6, 8) opens (becomes `TYPE_3fe2`).
4. Enter Shutter 2.
5. Proceed to Director (9, 12).