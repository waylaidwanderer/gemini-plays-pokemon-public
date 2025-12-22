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
- Switch 1 (16,1): Toggles (16,6), (17,6).
- Switch 2 (10,1): TBD.
- Switch 3 (2,1): Toggles (2,6), (3,6), (12,8).

## Toggle Log
- Turn 10435: (1,1,0) state in progress.
- Turn 10434: (1,0,0) verified. (2,6), (3,6), (2,7), (3,7) are OPEN. (12,8) is OPEN. (10,6), (6,8) are CLOSED.
- Turn 10432: S3 toggled ON. (2,6/7), (3,6/7) and (12,8) opened.
- Turn 10415: (0,0,1) verified visually. (16,6), (17,6) are OPEN. (10,6), (6,8) are CLOSED. (12,8) is OPEN.
- Turn 10400: (0,0,0) verified visually. (10,6), (6,8), (16,6), (17,6) are CLOSED. (12,8) is OPEN.
- Observation: Logic may be conditional (e.g., S1 toggles (12,8) only if S3 is ON). Systematic mapping from (0,0,0) will isolate primary effects.

## Systematic Mapping Plan Steps
1. Establish (0,0,0) baseline visually. (Done)
2. Toggle S1 ON. Verify all shutters. (Done)
3. Reset S1 OFF. Verify (0,0,0) again. (Done)
4. Toggle S3 ON (Sequence Step 1). (In Progress)
5. Toggle S2 ON (Sequence Step 2).
6. Toggle S1 ON (Sequence Step 3).
7. Verify path to Warehouse Entrance.

# Area Notes
- Warehouse Entrance: Southeast quadrant (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Ladders: (23,3) To Switch Room Entrance, (21,25) To North, (5,25) To South.

# Lessons Learned
- Standardize switch states as (S3, S2, S1).
- Visual confirmation is required after every toggle.
- Deductions are not verifications.
- Reset to (0,0,0) before mapping or sequence attempts.

# Shutter Sequence Solution
- Hint from Grunt (11,2): 'The switch on the end is the one to press first.'
- Verified Sequence from Summary: 3-2-1 (Switch 3 -> Switch 2 -> Switch 1).
- Current Plan: Reset all to OFF (0,0,0), then execute 3-2-1.