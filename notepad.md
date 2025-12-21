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
- Strategy: Execute sequence 3-2-1 from a clean (0,0,0) state.
- Start Turn: 10031
- Current State: (1, 1, 1) [S1: ON, S2: ON, S3: ON].
- Sequence Progress: 3 (ON) -> 2 (ON) -> 1 (ON). 3-2-1 Sequence Complete.

## Sequential Switch Logic (3-2-1)
- State (0, 0, 0): All shutters CLOSED? (Need to verify).
- State (0, 0, 1) [S3 ON]: (2,6) OPEN, (3,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (6,8) CLOSED, (12,8) OPEN.
- State (0, 1, 1) [3->2]: (2,6) OPEN, (3,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (6,8) CLOSED, (12,8) OPEN.
- State (1, 1, 1) [3->2->1]: Verifying... Expecting path to southeast warp to be open.

## Lessons Learned
- Turn 10050: Switches are sequential, not independent. Isolation data is misleading.
- Turn 10075: Always verify shutter states after each switch toggle to build an accurate sequential model.

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11), Burglar Eddie (9,12).
- Return Ladders: (23,3), (21,25), (5,25).