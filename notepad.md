# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. (2,6), (3,6), (10,6), (16,6), (17,6), (16,7), (17,7), (6,8), (12,8).
- Switch: Background object. Interact from adjacent tile (e.g., row 2 facing UP).
- LADDER: Warp tile. Traversable.
- WARP_CARPET_DOWN: Warp tile.

# Underground Warehouse Puzzle
- Hint: "the switch on the end is the one to press first." (S3).
- Sequence: 3 (ON) -> 2 (ON) -> 1 (ON).
- Current State: S3=ON, S2=ON, S1=ON. (Sequence Complete).

# Shutter Logic (Verified)
- Baseline (OFF, OFF, OFF): (12,8) OPEN. All others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6), (2,7), (3,7)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Current Strategy: Enter Warehouse
1. Sequence 3-2-1 complete. Gaps opened at:
   - x=2,3 (Rows 6, 7)
   - x=6 (Row 8)
   - x=10,11 (Rows 10, 11)
2. Navigate through (10, 10) to reach the southern area.
3. Explore the southern section for the entrance to Map 3_55 (Warehouse).

# Lessons Learned
- Toggling S1 and S2 both affects shutter (12, 8). If both are ON, it returns to OPEN.
- (12, 6), (12, 7), (12, 9) are permanent WALL tiles.
- (2, 7) and (3, 7) are shutters toggled by S3 (verified Turn 10908).
- Row 10 gap (x=10,11) opened by 3-2-1 sequence (verified Turn 10952).
- Always check cursor position in menus to avoid turning switches OFF by mistake.
- Scientific Method: Observe, Hypothesize, Test, Conclude. Test one variable at a time. Actively try to falsify confirmed hypotheses.

# Shutter Observation (Turn 10952)
- Row 6/7 at x=2,3: OPEN.
- Row 10/11 at x=2,3: CLOSED.
- Row 10/11 at x=10,11: OPEN.
- (6, 9) is FLOOR.
- (6, 13) is WALL.
- Goal: Find the Warehouse entrance (Map 3_55) in the southern area.