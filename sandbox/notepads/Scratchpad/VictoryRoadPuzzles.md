# Victory Road Puzzle Mechanics & Master Log

## Floor 1F Puzzle System (SOLVED)
- Boulder at (5, 15) pushed via lower highway (row 16) to eastern corridor (14, 14) -> (16, 12) -> (17, 12) -> onto Switch (17, 13).
- Lowers shutters at (5, 13) and (7, 7), unlocking access to 2F Ladder at (1, 1).

## Floor 2F Master Solution (Systematic Protocol & Testing Plan)

### Two-Boulder Master Protocol:
1. **Phase 1 (Boulder 2 -> Switch 1 @ (1, 16)) [SOLVED & VERIFIED Turn 23674-23676]**:
   - Initial position: Boulder 2 at (4, 14).
   - Verified Push Sequence: (4, 14) -> (3, 14) -> (3, 15) -> (3, 16) -> (2, 16) -> (1, 16) [Switch Plate 1].
   - **Result**: Shutter 1 at (5, 10) is OPEN (physically walked through at Turn 23676).

2. **Phase 2 (Boulder 1 -> Switch 2 @ (9, 11)) [IN PROGRESS]**:
   - Initial position: Boulder 1 at (5, 5) on Terrace.
   - Step 1: Walk to (5, 4) via column 0 and row 3.
   - Step 2: Push Boulder 1 South from (5, 5) -> (5, 6) -> (5, 7).
   - Step 3: Stand at (6, 7) -> push Boulder 1 West: (5, 7) -> (4, 7) -> (3, 7).
   - Step 4: Stand at (3, 6) -> push Boulder 1 South down West Corridor: (3, 7) -> (3, 8) -> (3, 9) -> (3, 10) -> (3, 11).
   - Step 5: Stand at (2, 11) -> push Boulder 1 East: (3, 11) -> (4, 11) -> (5, 11).
   - Step 6: Stand at (5, 12) -> push Boulder 1 North through opened Shutter 1 (5, 10): (5, 11) -> (5, 10) -> (5, 9) -> (5, 8).
   - Step 7: Stand at (4, 8) -> push Boulder 1 East along Central Corridor to (14, 8).
   - Step 8: Stand at (14, 7) -> push Boulder 1 South down Column 14 to (14, 11).
   - Step 9: Stand at (15, 11) -> push Boulder 1 West along Row 11 to (9, 11) [Switch Plate 2]!
   - **Result**: Shutters at (15, 15) and (21, 15) OPEN!

3. **Phase 3 (Ascend to 3F)**:
   - Walk south through opened Shutter (15, 15) / (21, 15) along row 16 directly onto SE platform.
   - Take SE Ladder at (25, 14) up to Victory Road 3F!

## Battle Escape Protocol (Standardized)
- Turn 1: Dismiss intro text with `['A', 'B']`.
- Turn 2: Select RUN from battle menu with `['Down', 'Right', 'A']`.
- Turn 3: Clear "Got away safely!" textbox with `['A']` or `['B']`.

## Core Traversal & Puzzle Principles
- **Empirical Traversal Rule**: Always test physical traversal directly into a gate/shutter tile before concluding whether a switch opened it.
- **Goal-Locking Policy**: Never transition between floors to re-survey an area mid-puzzle. Changing floors immediately resets dynamic boulder coordinates.
