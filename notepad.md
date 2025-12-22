# Tile Mechanics
- FLOOR: Traversable. Always verify.
- WALL: Impassable. Always verify.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN. Toggled by switches.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP).
- LADDER: Warp point to another map.
- WARP_CARPET_DOWN: Warp point to another map.

# Puzzle: Goldenrod Underground Switch Room
- Switch Puzzle Start: Turn 10284
- Switch Puzzle Start: Turn 10284. Phase: Executing 3-2-1.
- Time Tracking: Started Turn 10284. Currently Turn 10366.
- Sequence Step: 2 of 3 (S2). In progress.

## Strategy: 3-2-1 Sequence Execution (Attempt 3)
- Goal: Open path to the Warehouse Entrance in the southeast.
- Progress:
  - 1. S3 ON: Done (Turn 10357).
  - 2. S2 ON: In progress (Turn 10366).
  - 3. S1 ON: Next.
- Verification: Test (17,6) traversability when S1 is ON.
- Switch Puzzle Start: Turn 10284. Phase: Step 2 Complete. Moving to S1.
- Warehouse Entrance: Southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).

# Lessons Learned
- **Sequence Reset:** Always reset all switches to OFF before starting a sequence puzzle.
- **Visual Verification:** Don't rely on stale mental map data for shutters; verify visually after toggles.