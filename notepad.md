# Tile Mechanics
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN. Toggled by switches.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to southeast Warehouse Entrance (Map 3_55).
- Hint: "3-2-1" sequence (Left to Right).

## Shutter Toggle Mapping (S3, S2, S1)
| State | (2,6) | (3,6) | (10,6) | (12,8) | (16,6) | (17,6) | (6,8) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (0,0,0) | CLOSED | CLOSED | CLOSED | OPEN | CLOSED | CLOSED | CLOSED |
| (0,0,1) | ? | ? | CLOSED | ? | OPEN | OPEN | ? |
| (0,1,0) | ? | ? | ? | ? | ? | ? | ? |
| (1,0,0) | ? | ? | ? | ? | ? | ? | ? |

## Verified Toggle Logic (From 0,0,0 baseline)
- Switch 1 (16,1): Toggles (16,6), (17,6).
- Switch 2 (10,1): TBD.
- Switch 3 (2,1): Toggles (2,6), (3,6).

## Toggle Log
- Turn 10403: S1 ON. (16,6) and (17,6) seen OPEN.
- Turn 10411: (10,6) seen CLOSED in (0,0,1) state.
- Turn 10400: (0,0,0) state verified. (12,8) was OPEN in report 10398.

## Systematic Mapping Plan Steps
1. Establish (0,0,0) baseline visually. (Done)
2. Toggle S1 ON. Verify all shutters. (In progress)
3. Reset S1 OFF. Verify (0,0,0) again.
4. Toggle S2 ON. Verify all shutters.
5. Reset S2 OFF.
6. Toggle S3 ON. Verify all shutters.
7. Reset S3 OFF.
8. Combine switches based on results to find open path.

# Area Notes
- Warehouse Entrance: Southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Ladders: (23,3) To Switch Room Entrance, (21,25) To North, (5,25) To South.

# Lessons Learned
- Reset to (0,0,0) before starting sequence puzzles.
- Visual confirmation required for state verification.
- Inconsistent tuple notation leads to logic errors. Use (S3, S2, S1).
- Deductions are not verifications.