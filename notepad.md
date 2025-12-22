# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Solution: 3-2-1 sequence (Switch 3 -> Switch 2 -> Switch 1) from (0,0,0) baseline.

# Current Plan: Systematic Shutter Mapping
1. Reset to (0,0,0) baseline (All OFF).
   - S1: OFF (Turn 10578)
   - S2: OFF (Turn 10582)
   - S3: ON (Moving to reset)
2. Verify (0,0,0) state with report.
3. Test S1 ONLY (1,0,0): Toggle S1, Report, Toggle S1 back.
4. Test S2 ONLY (0,1,0): Toggle S2, Report, Toggle S2 back.
5. Test S3 ONLY (0,0,1): Toggle S3, Report, Toggle S3 back.
6. Analyze results to find combination for Warehouse (SE quadrant).

## Primary Effects (Mapping in progress)
- S3 (2,1): Toggles (2,6), (3,6).
- S2 (10,1): ?
- S1 (16,1): ?
- Baseline (0,0,0): (2,6) CLOSED, (3,6) CLOSED, (10,6) CLOSED, (16,6) CLOSED, (6,8) CLOSED, (12,8) OPEN, (17,6) CLOSED, (17,7) CLOSED. (Verified Turn 10561)

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use.

# Lessons Learned
- Start from (0,0,0) baseline before any sequence.
- (21, 29) is an exit, not the goal.
- 3-2-1 sequence requires starting from all switches OFF.
- Verification requires physically walking to the shutters.
- Do not repeat failed states; analyze data instead.
- Recording start turn: 10544.