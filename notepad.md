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

## Strategy: 3-2-1 Sequence Execution (Attempt 3)
- Goal: Open path to the Warehouse Entrance in the southeast.
- Progress:
  - 1. S3 ON: Done (Turn 10357).
  - 2. S2 ON: Done (Turn 10365).
  - 3. S1 ON: Done (Turn 10372). Sequence Complete.
- Switch Puzzle Start: Turn 10284. Phase: Verification.
- Sequence History:
  - Attempt 1: Mixed -> 3-2-1 (Failed)
  - Attempt 2: Reset -> 3-2-1 (S2 accidental toggle) -> (Failed)
  - Attempt 3: Reset -> 3-2-1 (Current)
- Verification: Move south to check if path to Map 3_55 is open at (10,6), (16,6), and (17,6).

# Area Notes
- Warehouse Entrance: Southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).

# Lessons Learned
- **Sequence Reset:** Always reset all switches to OFF before starting a sequence puzzle.
- **Visual Verification:** Don't rely on stale mental map data for shutters; verify visually after toggles.