# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Solution: 3-2-1 sequence (Switch 3 -> Switch 2 -> Switch 1) from (0,0,0) baseline.

# Current Plan: Reset and Map
1. Reset all switches to OFF (0,0,0).
   - S3: OFF (Done)
   - S2: OFF (Next)
   - S1: OFF
2. Verify all shutters are CLOSED at (0,0,0).
3. Map Primary Effects of each switch individually.
4. Execute 3-2-1 and verify path.

## Primary Effects (to be verified from 0,0,0)
- S3 (2,1): Toggles (2,6), (3,6), (12,8).
- S2 (10,1): Toggles (10,6), (6,8).
- S1 (16,1): Toggles (16,6).

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use.

# Lessons Learned
- Start from (0,0,0) baseline before any sequence.
- (21, 29) is an exit, not the goal.
- 3-2-1 sequence is the standard solution but requires proper sync.
- Verification requires physically walking to the shutters.