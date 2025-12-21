# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP). Toggles specific shutters.
- LADDER: Warp point to another map.
- WARP_CARPET_DOWN: Warp point to another map.

# Puzzle: Goldenrod Underground Switch Room
- Puzzle Start Turn: ~10125
- Hint: "3-2-1" sequence (Left to Right).

## Research: Shutter States (S3, S2, S1)
- Note: Tiles must be SEEN after a toggle to verify state. Mental Map may be stale.
| State | (2,6) | (10,6) | (16,6) | (12,8) | (17,6) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (0,0,0) | OPEN | CLOSED | CLOSED | CLOSED | CLOSED |
| (1,0,0) | OPEN | CLOSED | CLOSED | OPEN | CLOSED |
| (1,1,1) | ? | ? | CLOSED | CLOSED | CLOSED |

## Strategy: 3-2-1 Sequence Execution
- Goal: Open path to the southeast Warehouse Entrance.
- Start Turn: 10284
- Sequence: S3 (Left) -> S2 (Middle) -> S1 (Right).
- Current Progress: S2 toggled ON. Moving to Switch 1 at (16, 1).
- Verified Shutter States (1,0,0): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (6,8) CLOSED, (12,8) OPEN, (17,6) CLOSED. (Verified turn 10287)

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).
- Obstacle: Rocket Grunt at (17, 2) is facing down. Row 2 corridor at X=11-12 may be blocked by another NPC.

# Lessons Learned
- **Sprite Verification:** Always verify the "Map Objects" list and the current screen before assuming an NPC is blocking a path. Visual hallucinations of obstructions can lead to inefficient routing.
- **Switch Logic:** In Crystal, sequence puzzles often depend on the order of activation from a neutral (all OFF) state. Use a systematic reset to ensure the sequence is applied correctly.