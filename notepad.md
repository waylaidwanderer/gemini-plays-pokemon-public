# Tile Mechanics
- FLOOR: Walkable surface.
- WALL: Impassable barrier.
- SHUTTER: Toggled by switches. Acts as WALL when closed, FLOOR when open. Verified at (2, 6), (10, 6), (12, 8), (16, 6).

# Strategy: Switch Room Puzzle (Map 3_54)
- Goal: Reach the Underground Warehouse (Map 3_55).
- Method: Execute the 3-2-1 sequence (Turn ON Switch 3, then 2, then 1).
- Logic: Order of switches matters. 3-2-1 is the standard solution from all-OFF state.
- Start Turn: 9640

## Switch Status (Turn 9764)
- Switch 3 (2, 1): 🟢 ON
- Switch 2 (10, 1): 🟢 ON
- Switch 1 (16, 1): 🔴 OFF

## Shutter States (Current: [ON, ON, OFF])
- (2, 6): FLOOR (OPEN)
- (10, 6): WALL (CLOSED)
- (12, 8): FLOOR (OPEN)
- (16, 6): WALL (CLOSED)

## Lessons Learned
- Verify shutter states in XML after every switch interaction.
- Order of operations is critical; resetting to a known state (all OFF) is the safest way to start a sequence.
- Map markers must reflect the current state, not the intended state.
- Paths are often wider than a single tile; check adjacent tiles for bypasses.

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).