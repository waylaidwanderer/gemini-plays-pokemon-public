# Tile Mechanics
- FLOOR: Walkable surface. Verified.
- WALL: Impassable barrier. Verified.
- SHUTTER: Toggled by switches. Acts as WALL when closed, FLOOR when open.
- LADDER: Triggers map transition. Verified.

# Strategy: Switch Room Puzzle (Map 3_54)
- Goal: Reach the Underground Warehouse (Map 3_55).
- Method: Execute the 3-2-1 sequence (Turn ON Switch 3, then 2, then 1).
- Start Turn: ~9640
- Logic: Switch 3 (Left) toggles sets 1&2, Switch 2 (Middle) toggles 1&3, Switch 1 (Right) toggles 2&3.

## Switch Combination Log
- [3 ON, 2 ON, 1 ON]: Attempting now.

## Switch States
- Switch 3 (2, 1): ON
- Switch 2 (10, 1): OFF
- Switch 1 (16, 1): OFF

# Area Notes
- Warehouse Entrance: Likely a door in the southern unseen area (Map 3_55).
- Return Ladders: (23, 3), (21, 25), and (5, 25) all lead back to the main Underground (3_52).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).