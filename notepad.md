# Tile Mechanics
- FLOOR: Traversable.
- SHUTTER: WALL when CLOSED, FLOOR when OPEN.

# Puzzle: Goldenrod Underground Switch Room
- Goal: Reach the Underground Warehouse (Map 3_55).
- Strategy: Identify the sequence that clears row 6 and row 8.

## Switch Logic (Isolation)
- S1 (1,0,0): (16,6) OPEN, (12,8) OPEN.
- S2 (0,1,0): (10,6) OPEN, (6,8) OPEN, (6,9) OPEN.
- S3 (0,0,1): (2,6) OPEN.

## Sequence Results
- 3 -> 2 (0,1,1): (2,6) OPEN, (10,6) CLOSED, (12,8) OPEN.
- 3 -> 2 -> 1 (1,1,1): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED. BLOCKED.

## Plan
1. Reset to (0,0,0) (All switches OFF).
2. Execute 3-2-1 sequence: S3 ON -> S2 ON -> S1 ON.
3. Explore southeast quadrant for Warehouse warp.

# Area Notes
- Warehouse Entrance: Likely southeast warp.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11), Burglar Eddie (9,12).
- Return Ladders: (23,3), (21,25), (5,25).