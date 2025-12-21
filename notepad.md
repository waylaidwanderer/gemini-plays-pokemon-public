# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP). Toggles specific shutters.
- LADDER: Warp point to another map.
- WARP_CARPET_DOWN: Warp point to another map.

# Puzzle: Goldenrod Underground Switch Room
- Puzzle Start Turn: ~10125
## Strategy: Shutter Sequence Testing
- Goal: Open path to the southeast (cols 14+).
- Current Switch States: S3=OFF, S2=OFF, S1=ON (0,0,1)
- Reset Plan:
  1. Turn Switch 1 OFF.
  2. All switches will be OFF (0,0,0). Verify all shutters closed.
- Execution Plan (3-2-1 sequence):
  1. Toggle Switch 3 ON.
  2. Toggle Switch 2 ON.
  3. Toggle Switch 1 ON.
  4. Verify path to southeast.

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).