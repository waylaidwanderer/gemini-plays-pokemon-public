# Tile Mechanics
- FLOOR: Walkable surface.
- WALL: Impassable barrier.
- SHUTTER: Toggled by switches. Acts as WALL when closed, FLOOR when open. Verified at (2, 6), (10, 6), (12, 8), (16, 6).

# Strategy: Switch Room Puzzle (Map 3_54)
- Goal: Reach the Underground Warehouse (Map 3_55).
- Method: Execute the 3-2-1 sequence (Turn ON Switch 3, then 2, then 1).
- Logic: Order of switches matters. 3-2-1 is the standard solution from all-OFF state.
- Start Turn: 9640

## Switch Status (Turn 9772)
- Switch 3 (2, 1): 🟢 ON
- Switch 2 (10, 1): 🟢 ON
- Switch 1 (16, 1): 🟢 ON (Just turned ON)

## Shutter States (Current: [ON, ON, OFF])
- (2, 6): FLOOR (OPEN)
- (10, 6): WALL (CLOSED)
- (12, 8): FLOOR (OPEN)
- (16, 6): WALL (CLOSED)

## Switch-Shutter Observations (Current Hypothesis)
- Switch 3 (Turn 9731): Turning ON made (2, 6) and (12, 8) FLOOR.
- Switch 2 (Turn 9761): Turning ON (Waiting to see effect).
- Switch 1 (Turn 9710): Turning ON made (12, 8) WALL.
- The goal is to have (10, 6), (12, 8), and (16, 6) all as FLOOR to reach the exit.

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).