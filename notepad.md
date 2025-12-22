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
- Current State (Post-Action): S3=ON, S2=ON, S1=ON. (Sequence Complete).

# Shutter Logic (Verified)
- Baseline (OFF, OFF, OFF): (12,8) OPEN. All others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6), (2,7), (3,7)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Current Strategy: Enter Warehouse
1. Sequence 3-2-1 complete. Path at (2, 6) and (6, 8) is OPEN.
2. Navigate south via (2, 6) to explore the southern area.
3. Look for a gap or shutter in the wall at row 10/11.
4. Locate the warp to Map 3_55.

# Lessons Learned
- Toggling S1 and S2 both affects shutter (12, 8). If both are ON, it returns to OPEN.
- (12, 6), (12, 7), (12, 9) are permanent WALL tiles.
- (2, 7) and (3, 7) are shutters toggled by S3 (verified Turn 10908).
- Row 10 is a major wall; must find a way through to reach the southern warps.
- Always check cursor position in menus to avoid turning switches OFF by mistake.
- Scientific Method: Observe, Hypothesize, Test, Conclude. Test one variable at a time. Actively try to falsify confirmed hypotheses.

# Shutter Observation (Turn 10949)
- Row 6/7 at x=2,3: OPEN (S3=ON).
- Row 10/11 at x=2,3: CLOSED (WALL).
- (6, 9) changed to FLOOR (Turn 10947). Likely a shutter opened by S1 or S2.
- (6, 13) changed to WALL (Turn 10948). Likely a shutter closed by S1 or S2.
- Hypothesis: Row 10/11 contains shutters that are also toggled by the switches.
- Goal: Map the Row 10/11 shutters to the switches.