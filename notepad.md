# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Verified Solution: 3-2-1 sequence (Switch 3 -> Switch 2 -> Switch 1).

# Current Plan: Physical Verification
1. Maintain (1,1,1) state. (Current: S1=ON, S2=ON, S3=ON).
2. Walk to (2,6) to confirm it is OPEN.
3. Walk to (6,8) to confirm its state.
4. Walk to (12,8) to confirm it is OPEN.
5. If blocked, use strategist with verified data. Do NOT reset prematurely.

## Shutter Status (1,1,1) - Last Seen
- (2,6): OPEN
- (3,6): OPEN
- (10,6): CLOSED
- (16,6): CLOSED
- (6,8): CLOSED
- (12,8): OPEN
- (17,6): CLOSED
- (17,7): CLOSED

# Area Notes
- Warehouse Entrance: Likely southeast quadrant (Map 3_55).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use.

# Lessons Learned
- Don't reset until the path is physically tested.
- (21, 29) is an exit, not the objective.
- 3-2-1 sequence is the standard solution.

## Final Sequence Execution
- Turn 10525: Selected YES to turn S1 ON. Sequence 3-2-1 (All ON) is active.
- Path Plan: (16,2) -> (16,4) -> (2,4) -> (2,6) -> (6,8) -> (12,8) -> Southeast quadrant.
- Shutter Check: (2,6) and (6,8) must be OPEN.