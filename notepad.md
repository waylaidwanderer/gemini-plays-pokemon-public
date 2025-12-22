# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN. (2,6), (3,6), (10,6), (16,6), (17,6), (6,8), (12,8).
- Switch: Background object at (2,1), (10,1), (16,1). Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Start Turn: 10544.
- Hint from Rocket Grunt: "the switch on the end is the one to press first."

# Shutter Logic Hypotheses
- Baseline (OFF, OFF, OFF): (12,8) is OPEN, all others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Puzzle Solving Log
- Attempt 1: 3-2-1 Sequence (Turns 10706-10726). Result: Incomplete. (10,6), (16,6), (17,6), (6,8) remained CLOSED. (12,8) was OPEN.
- Attempt 2 (Current): 3-2-1 Sequence.
  - S3 (ON) at Turn 10763.
  - S2 (ON) at Turn 10767.
  - Next: S1 (ON).

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).

# Lessons Learned
- Verify shutter states visually or via tool.
- NPCs and Items block paths like WALLs.
- 3-2-1 sequence may require a specific starting state or reset.
- Error Turn 10733: Checking a switch menu resets the player's position or triggers a pathing abort.
- Error Turn 10750: Position mismatch at Switch 2 was caused by a pathing abort during a long navigation. Use smaller steps.