# Tile Mechanics
- FLOOR: Traversable. Collision type: FLOOR.
- WALL: Impassable. Collision type: WALL.
- LADDER: Warp point. Interaction triggers map transition.
- WARP_CARPET_DOWN: Warp point. Walking onto it triggers map transition.
- SHUTTER: Dynamic collision. WALL when CLOSED, FLOOR when OPEN.
- SwitchScript (2,1), (10,1), (16,1): Interactable from adjacent tile (e.g., from row 2 facing UP). Toggles specific shutters.

# Puzzle: Goldenrod Underground Switch Room
- Goal: Reach the Underground Warehouse (Map 3_55).
- Hint: Rocket Grunt mentioned "3-2-1".
- Current State: (0, 0, 0) [Switch 1: OFF, Switch 2: OFF, Switch 3: OFF].
- Sequence Progress: 3 (OFF) -> 2 (OFF) -> 1 (OFF). Reset Complete.

## Sequential Switch Logic (3-2-1)
- State (0, 0, 0): All shutters CLOSED? (Need to verify).
- State (0, 0, 1) [S3 ON]: (2,6) CLOSED (Verified Turn 10060), (3,6) CLOSED, (10,6) CLOSED, (16,6) CLOSED, (6,8) OPEN (?), (12,8) CLOSED.
- State (0, 1, 1) [3->2]: (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (6,8) OPEN, (12,8) OPEN.
- State (1, 1, 1) [3->2->1]: Target state to open the final path.

## Shutter Toggle Data (Isolation - FLAWED, Sequential Logic applies)
- S1 (16,1): (1,0,0) -> (16,6) OPEN, (12,8) OPEN.
- S2 (10,1): (0,1,0) -> (10,6) OPEN, (6,8) OPEN.
- S3 (2,1): (0,0,1) -> (2,6) OPEN, (3,6) CLOSED (?), (6,8) OPEN.

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11), Burglar Eddie (9,12).
- Return Ladders: (23,3), (21,25), (5,25).