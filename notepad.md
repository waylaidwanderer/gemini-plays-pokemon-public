# Tile Mechanics
- FLOOR: Walkable surface. Verified.
- WALL: Impassable barrier. Verified.
- SHUTTER: Toggled by switches. Acts as WALL when closed, FLOOR when open.
- LADDER: Triggers map transition. Verified.

# Strategy: Switch Room Puzzle (Map 3_54)
- Goal: Reach the Underground Warehouse (Map 3_55).
- Method: Execute the 3-2-1 sequence (Switch 3 -> Switch 2 -> Switch 1).
- Start Turn: ~9640

## Switch-Shutter Mappings (Observed)
- Switch 1 (16, 1): Toggles (12, 8). [ON -> WALL]
- Switch 2 (10, 1): Toggles (2, 6). [OFF -> WALL]
- Switch 3 (2, 1): Toggles (16, 6). [OFF -> FLOOR]

## Current Switch States
- Switch 1: OFF
- Switch 2: ON
- Switch 3: ON

## Shutter States (Turn 9721)
- (2, 6): FLOOR (Open)
- (10, 6): WALL (Closed)
- (12, 8): FLOOR (Open)
- (16, 6): WALL (Closed)

# Area Notes
- Warehouse Entrance: Likely a door in the southern unseen area (Map 3_55).
- Return Ladders: (23, 3), (21, 25), and (5, 25) all lead back to the main Underground (3_52).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).