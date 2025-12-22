# Tile Mechanics
- FLOOR: Traversable. Always verify.
- WALL: Impassable. Always verify.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN. Toggled by switches.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP).
- LADDER: Warp point to another map.
- WARP_CARPET_DOWN: Warp point to another map.

# Puzzle: Goldenrod Underground Switch Room
- Switch Puzzle Start: Turn 10284
- Solution Sequence: 3-2-1 (Left, Middle, Right).

## Shutter Toggle Logic (Hypothesis)
- S3 (2,1): Toggles (2,6), (3,6), (12,8).
- S2 (10,1): Toggles (10,6), (12,8), (6,8).
- S1 (16,1): Toggles (16,6), (10,6), (6,8), (17,6).

## Verified Shutter States (S3, S2, S1)
- (0,0,0): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (12,8) CLOSED, (6,8) OPEN, (17,6) CLOSED.
- (1,0,0): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (12,8) OPEN, (6,8) CLOSED.
- (1,1,1): (10,6) CLOSED, (16,6) CLOSED, (12,8) CLOSED, (6,8) CLOSED, (17,6) CLOSED. (Verified Turn 10376 via tile change detection)

## Shutter Sequence Log
- Attempt 3 (Turn 10373): Reset -> 3-2-1. Result: (10,6), (16,6), (12,8) all CLOSED. FAILED.
- Observation: The "3-2-1" sequence from an all-OFF state did not open the path.

## Systematic Mapping Plan
- Goal: Determine exact toggle logic for each switch.
- Steps:
  1. Reset all switches to OFF.
  2. Toggle S1 ON. Record all shutter changes. Reset to OFF.
  3. Toggle S2 ON. Record all shutter changes. Reset to OFF.
  4. Toggle S3 ON. Record all shutter changes. Reset to OFF.

# Area Notes
- Warehouse Entrance: Southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).

# Lessons Learned
- **Sequence Reset:** Always reset all switches to OFF before starting a sequence puzzle.
- **Visual Verification:** Don't rely on stale mental map data for shutters; verify visually after toggles.
- **Toggle Logic:** Shutter states depend on the combination of active switches. Mapping individual switch effects from (0,0,0) is essential.