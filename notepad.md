# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN. (2,6), (3,6), (10,6), (16,6), (17,6), (16,7), (17,7), (6,8), (12,8).
- Switch: Background object at (2,1), (10,1), (16,1). Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Hint from Rocket Grunt: "the switch on the end is the one to press first."
- Rumored Order: Switch 3 -> Switch 2 -> Switch 1.

# Shutter Logic (Verified Observations)
- Baseline (OFF, OFF, OFF): (12,8) is OPEN, all others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Puzzle Solving Log
- Attempt 1 & 2: Failed.
- Attempt 3 (Current): 3-2-1 Sequence.
  - S3 ON (Turn 10800).
  - S2 ON (Turn 10805).
  - S1 ON (Turn 10816).
  - RESULT: Path to Warehouse entrance (12, 13) is OPEN. (Verified by Shutter Report 10817: (2,6), (3,6), and (12,8) are OPEN).

# Current Strategy: Enter Warehouse
1. Navigate south through (12, 8).
2. Enter Warehouse at (12, 13).

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).

# Lessons Learned
- Verify shutter states visually or via tool.
- NPCs and Items block paths like WALLs.
- 3-2-1 sequence may require a specific starting state or reset.
- Don't check switch states after flipping them; it may break the sequence.
- Trust the shutter report tool for state verification.
- Talking to a switch you just turned ON and seeing the "It's ON. Turn it OFF?" message DOES NOT reset the sequence, but it's best to avoid it to be safe.