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

## Research: Isolation Testing Matrix (S3, S2, S1)
| State | (2,6) | (3,6) | (10,6) | (16,6) | (6,8) | (12,8) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (0,0,0) | OPEN | OPEN | CLOSED | CLOSED | CLOSED | CLOSED |

## Strategy: Shutter Sequence Testing
- Goal: Open path to the southeast (cols 14+). Requires (16,6) or (17,6) to be OPEN.
- Current Switch States: S3=OFF, S2=OFF, S1=OFF (0,0,0)
- Execution Plan (3-2-1 sequence):
  1. Toggle Switch 3 (2,1) ON.
  2. Toggle Switch 2 (10,1) ON.
  3. Toggle Switch 1 (16,1) ON.
  4. Verify path to southeast.
- Current Step: Moving to Switch 3.

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).

# Lessons Learned
- **Sprite Verification:** Always verify the "Map Objects" list and the current screen before assuming an NPC is blocking a path. Visual hallucinations of obstructions can lead to inefficient routing.
- **Switch Logic:** In Crystal, sequence puzzles often depend on the order of activation from a neutral (all OFF) state. Use a systematic reset to ensure the sequence is applied correctly.