# Tile Mechanics
- FLOOR: Traversable. Always verify.
- WALL: Impassable. Always verify.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN. Toggled by switches.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP).
- LADDER: Warp point to another map.
- WARP_CARPET_DOWN: Warp point to another map.

# Puzzle: Goldenrod Underground Switch Room
- Switch Puzzle Start: Turn 10284
- Phase: Executing 3-2-1 Sequence. Step 2 Complete.
- Sequence: S3 (Left) -> S2 (Middle) -> S1 (Right).
- Time Tracking: Started Turn 10284. Currently Turn 10368.

## Verified Shutter Logic
- S3 (2,1): Toggles (2,6), (3,6), (12,8). (Verified Turn 10313)

## Hypothesized Shutter Logic
- S2 (10,1): Toggles (10,6), (12,8), (6,8).
- S1 (16,1): Toggles (16,6), (10,6), (6,8), (17,6).
- Note: (17,6) needs verification (WALL vs SHUTTER).

## Shutter Sequence Log
- Attempt 3 (Turn 10373): Reset -> 3-2-1. Result: (10,6), (16,6), (12,8) all CLOSED. FAILED.
- Observation: The "3-2-1" sequence from an all-OFF state did not open the path.

## Systematic Mapping Plan (Post-Battle)
- Goal: Determine exact toggle logic for each switch.
- Method:
  1. Reset all switches to OFF.
  2. Toggle S1 ON. Check all shutters (2,6), (3,6), (10,6), (16,6), (6,8), (12,8), (17,6).
  3. Reset to OFF.
  4. Toggle S2 ON. Check all shutters.
  5. Reset to OFF.
  6. Toggle S3 ON. Check all shutters.
- Current Status: Defeating Rocket Grunt at (11,2).

# Area Notes
- Warehouse Entrance: Southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).

# Lessons Learned
- **Sequence Reset:** Always reset all switches to OFF before starting a sequence puzzle.
- **Visual Verification:** Don't rely on stale mental map data for shutters; verify visually after toggles.