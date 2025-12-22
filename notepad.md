# Tile Mechanics
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN. Toggled by switches.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to southeast Warehouse Entrance (Map 3_55).

## Shutter Toggle Mapping (S3, S2, S1)
| State | (2,6) | (3,6) | (10,6) | (12,8) | (16,6) | (17,6) | (6,8) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (0,0,0) | CLOSED | CLOSED | CLOSED | OPEN | CLOSED | CLOSED | CLOSED |
| (0,0,1) | CLOSED | CLOSED | CLOSED | OPEN | OPEN | OPEN | CLOSED |
| (0,1,0) | ? | ? | ? | ? | ? | ? | ? |
| (1,0,0) | ? | ? | ? | ? | ? | ? | ? |

## Verified Toggle Logic (From 0,0,0 baseline)
- Switch 1 (16,1): Toggles (16,6), (17,6). Does NOT toggle (10,6), (6,8), (12,8) when S3,S2 are OFF.
- Switch 2 (10,1): TBD.
- Switch 3 (2,1): TBD.

## Toggle Log
- Turn 10415: (0,0,1) verified visually. (16,6), (17,6) are OPEN. (10,6), (6,8) are CLOSED. (12,8) is OPEN.
- Turn 10400: (0,0,0) verified visually. (10,6), (6,8), (16,6), (17,6) are CLOSED. (12,8) is OPEN.
- Observation: Logic may be conditional (e.g., S1 toggles (12,8) only if S3 is ON). Systematic mapping from (0,0,0) will isolate primary effects.

## Systematic Mapping Plan Steps
1. Establish (0,0,0) baseline visually. (Done)
2. Toggle S1 ON. Verify all shutters. (Done)
3. Reset S1 OFF. Verify (0,0,0) again. (Next)
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
- Standardize switch states as (S3, S2, S1).
- Visual confirmation is required after every toggle.
- Deductions are not verifications.
- Reset to (0,0,0) before mapping or sequence attempts.