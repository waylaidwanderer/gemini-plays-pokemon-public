# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch: Background object. Interact from adjacent tile (e.g., row 2 facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Hint: "the switch on the end is the one to press first." (S3 or S1).
- Target Sequence: 3 (ON) -> 2 (ON) -> 1 (ON).

# Shutter Logic (Verified from 10832 report)
- Baseline (OFF, OFF, OFF): (12,8) is OPEN. All others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Puzzle Strategy (Attempt 5: Clean Reset)
- Step 1: Turn all switches OFF.
  - S3: Currently OFF (🔴). (Turned OFF at 10885)
  - S2: Currently OFF (🔴). (Turned OFF at 10881)
  - S1: Currently ON (🟢). (Heading to (16, 2))
- Step 2: Turn S3 ON.
- Step 3: Turn S2 ON.
- Step 4: Turn S1 ON.
- Step 5: Enter Warehouse.

# Lessons Learned
- Toggling S1 and S2 both affects shutter (12, 8).
- Shutter status report tool only updates for tiles currently in the Mental Map (seen).
- Always verify switch state via text before concluding sequence step.