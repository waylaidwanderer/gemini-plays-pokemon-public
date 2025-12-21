# Tile Mechanics
- FLOOR: Walkable surface.
- WALL: Impassable barrier.
- SHUTTER: Toggled by switches. Acts as WALL when closed, FLOOR when open.

# Strategy: Switch Room Puzzle (Map 3_54)
- Goal: Reach the Underground Warehouse (Map 3_55).
- Method: Execute the 3-2-1 sequence (Turn ON Switch 3, then 2, then 1).
- Start Turn: ~9640
- Logic: Order of switches matters. 3-2-1 is the solution.

## Switch Reset (Current Status)
- Switch 1 (16, 1): 🔴 OFF
- Switch 2 (10, 1): 🔴 OFF
- Switch 3 (2, 1): 🟢 ON (Moving to turn OFF)

## Shutter Truth Table
| Configuration [3, 2, 1] | (2, 6) | (10, 6) | (12, 8) | (16, 6) |
|-------------------------|--------|---------|---------|---------|
| [ON, OFF, OFF] (9752)   | FLOOR  | WALL    | FLOOR   | WALL    |

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).