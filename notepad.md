# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN. (2,6), (3,6), (10,6), (16,6), (17,6), (6,8), (12,8).
- Switch: Background object at (2,1), (10,1), (16,1). Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Hint from Rocket Grunt: "the switch on the end is the one to press first."
- Confirmed Order: Switch 3 -> Switch 2 -> Switch 1.

# Shutter Logic (Verified Observations)
- Baseline (OFF, OFF, OFF): (12,8) is OPEN, all others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (12,8)

# Puzzle Solving Log
- Attempt 2: 3-2-1 Sequence.
  - S3 ON (Turn 10763).
  - S2 ON (Turn 10767).
  - S1 ON (Turn 10774).
  - Result: (2,6), (3,6), (12,8) are OPEN. (10,6), (6,8), (16,6), (17,6) are CLOSED.
  - Theory: Checking switch states via menu might reset the sequence or count as an interaction. 

# Current Strategy: Full Reset and Execution
1. Turn S1 OFF (Current position: (16,2)).
2. Turn S2 OFF.
3. Turn S3 OFF.
4. Execute 3-2-1 (S3 -> S2 -> S1) without interruption.
5. Enter Warehouse.

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).

# Lessons Learned
- Verify shutter states visually or via tool.
- NPCs and Items block paths like WALLs.
- 3-2-1 sequence may require a specific starting state or reset.
- Don't check switch states after flipping them; it may break the sequence.
- Trust the shutter report tool for state verification.
- Talking to a switch you just turned ON and seeing the "It's ON. Turn it OFF?" message DOES NOT reset the sequence, but it's best to avoid it to be safe.
- (16,7) and (17,7) are likely static walls, not shutters.