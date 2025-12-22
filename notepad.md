# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN. Toggled by switches.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP).
- LADDER: Warp point to another map.
- WARP_CARPET_DOWN: Warp point to another map.

# Puzzle: Goldenrod Underground Switch Room
- Switch Puzzle Start: Turn 10284
- Goal: Open path to the Warehouse Entrance in the southeast.

## Shutter Toggle Logic (Hypothesis)
- S3 (2,1): Toggles (2,6), (3,6), (12,8).
- S2 (10,1): Toggles (10,6), (12,8), (6,8).
- S1 (16,1): Toggles (16,6), (10,6), (6,8).
- Note: (17,6) is labeled WALL in XML. Verification required to see if it ever toggles.

## Verified Shutter States (S3, S2, S1)
- (0,0,0): (2,6), (3,6), (10,6), (16,6), (6,8), (12,8) are all CLOSED (WALL). (Verified Turn 10400).
- Toggle Log:
  - S3 (2,1) toggles (2,6), (2,7), (3,6), (3,7).
  - S1 (16,1) toggles (12,8), (12,9).
- Current Status: S1 ON, S2 OFF, S3 OFF (1,0,0). Mapping S1.
- S1 (16,1) Toggles: (16,6), (17,6), (12,8), (12,9). (Verified Turn 10408)
- Observed Shutter Changes (0,0,0 -> 1,0,0):
  - (16,6): WALL -> FLOOR
  - (17,6): WALL -> FLOOR (Confirmed: (17,6) is a shutter!)
  - (12,8): WALL -> FLOOR
- Next: Check (10,6) and (6,8) for S1 toggles. Then reset S1.

# Area Notes
- Warehouse Entrance: Southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).

# Lessons Learned
- **Sequence Reset:** Always reset all switches to OFF before starting a sequence puzzle.
- **Visual Verification:** Don't rely on stale mental map data for shutters; verify visually after toggles.
- **Toggle Logic:** Shutter states depend on the combination of active switches. Mapping individual switch effects from (0,0,0) is essential.