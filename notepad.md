# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (unseen southeast area, Map 3_55).
- Sequence Strategy: 3-2-1 (Switch 3 -> Switch 2 -> Switch 1).
- Note: (21, 29) is the EXIT to Goldenrod City, NOT the Warehouse entrance.

## Toggle Log
- Turn 10509: S1 toggled ON. State is (1,1,1). Sequence 3-2-1 complete.
- Turn 10505: S2 toggled ON. State is (1,1,0).
- Turn 10499: S3 toggled ON. State is (1,0,0). (2,6), (3,6) verified OPEN.
- Turn 10490: (0,0,0) baseline reached. All switches OFF.

# Area Notes
- Warehouse Entrance: Likely behind the shutters in the southeast (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use until Director is rescued.

# Puzzle Strategy
- Committed to 3-2-1 sequence.
- Step 1: Switch 3 ON (Done).
- Step 2: Switch 2 ON (Done).
- Step 3: Switch 1 ON (Done).
- Step 4: Walk south to (2,6) -> (12,8) -> Southeast to find Map 3_55 entrance.
- Verification: Physically test the path. Do NOT reset until path is confirmed blocked.
## Final Sequence Execution
- Turn 10510: Selected NO to keep S1 ON. Sequence 3-2-1 (All ON) is active.
- Path Plan: (16,2) -> (16,4) -> (2,4) -> (2,6) -> (2,8) -> (12,8) -> Southeast.