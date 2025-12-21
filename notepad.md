# Tile Mechanics
- FLOOR: Traversable. Always verify.
- WALL: Impassable. Always verify.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN. Toggled by switches.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP).
- LADDER: Warp point to another map.
- WARP_CARPET_DOWN: Warp point to another map.

# Puzzle: Goldenrod Underground Switch Room
- Puzzle Start Turn: 10284 (Current Attempt)
- Sequence: 3-2-1 (Left to Right).

## Shutter Toggle Logic (Verified Relationships)
- S3 (2,1): Toggles (2,6), (3,6), (12,8).
- S2 (10,1): Toggles (10,6), (12,8), (6,8).
- S1 (16,1): Toggles (16,6), (10,6), (6,8).
- Note: (17,6) is a shutter tile, not a permanent wall.

## Research: Shutter States (S3, S2, S1)
- State (0,0,0): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (12,8) CLOSED, (6,8) OPEN? (Verify 6,8)
- State (1,0,0): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (12,8) OPEN, (6,8) CLOSED.
- State (1,1,0): To be verified.

## Strategy: 3-2-1 Sequence Execution
- Goal: Open path to the Warehouse Entrance in the southeast.
- Sequence: S3 (Left) -> S2 (Middle) -> S1 (Right).
- Attempt 2 (Started from 0,0,0):
  - 1. S3 ON (Turn 10313): Done.
  - 2. S2 ON (Turn 10321): Keeping ON.
  - 3. S1 ON: Next.

# Area Notes
- Warehouse Entrance: Southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).

# Lessons Learned
- **Sprite Verification:** Check "Map Objects" for actual obstructions.
- **Sequence Reset:** For order-based puzzles, reset all switches to a known state (OFF) before starting the sequence.