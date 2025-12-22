# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Sequence Strategy: 3-2-1 (Switch 3 -> Switch 2 -> Switch 1).
- 3-2-1 is the verified solution from history.

# Puzzle Strategy
1. Complete 3-2-1 sequence (Currently: S3=ON, S2=ON, S1=ON).
2. Physically walk to shutters at (2,6), (6,8), and (16,6) to verify the open path.
3. Locate entrance to Map 3_55 (Underground Warehouse) in the southeast quadrant.

## Toggle Log
- Turn 10521: S1 confirmed ON. Sequence 3-2-1 complete. Heading south to verify path.
- Turn 10499: S3 toggled ON. (2,6), (3,6) verified OPEN.
- Turn 10490: (0,0,0) baseline reached. All switches OFF.

# Area Notes
- Warehouse Entrance: Likely southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use until Director is rescued.

# Lessons Learned
- Don't reset until the path is physically tested.
- (21, 29) is an exit, not the objective.
- 3-2-1 sequence clears the path to the southeast.