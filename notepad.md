# Tile Mechanics
- FLOOR: Traversable. Always verify.
- WALL: Impassable. Always verify.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN. Toggled by switches.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP).
- LADDER: Warp point to another map.
- WARP_CARPET_DOWN: Warp point to another map.

# Puzzle: Goldenrod Underground Switch Room
- Puzzle Start Turn: 10284 (Attempt 2)
- Solution Sequence: 3-2-1 (Left, Middle, Right).

## Shutter Toggle Logic (Hypothesis)
- S3 (2,1): Toggles (2,6), (3,6), (12,8).
- S2 (10,1): Toggles (10,6), (12,8), (6,8).
- S1 (16,1): Toggles (16,6), (10,6), (6,8), (17,6).

## Verified Shutter States
- (0,0,0): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (12,8) CLOSED, (6,8) OPEN, (17,6) CLOSED.
- (1,0,0): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (12,8) OPEN, (6,8) CLOSED.
- (1,1,0): To be verified.
- (1,1,1): (10,6) CLOSED, (16,6) CLOSED, (12,8) OPEN, (6,8) CLOSED, (17,6) CLOSED. (Turn 10297)

# Strategy: 3-2-1 Sequence Execution
- Goal: Open path to the Warehouse Entrance in the southeast.
- Attempt 2 Progress:
  - 1. S3 ON: Done (Turn 10313).
  - 2. S2 ON: Done (Turn 10324).
  - 3. S1 ON: In progress (Turn 10325).

# Area Notes
- Warehouse Entrance: Southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).

# Lessons Learned
- **Sequence Reset:** For order-based puzzles, reset all switches to a known state (OFF) before starting the sequence.
- **Verification:** Always check shutter states after each toggle to confirm logic.