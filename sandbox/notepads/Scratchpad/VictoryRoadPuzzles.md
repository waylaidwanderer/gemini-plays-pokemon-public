# Victory Road Puzzle Mechanics & Master Log

## Floor 1F Puzzle System (SOLVED)
- Boulder at (5, 15) pushed via lower highway (row 16) to eastern corridor (14, 14) -> (16, 12) -> (17, 12) -> onto Switch (17, 13).
- Lowers shutters at (5, 13) and (7, 7), unlocking access to 2F Ladder at (1, 1).

## Floor 2F Master Solution (Systematic Protocol & Testing Plan)

### Master Progression Route:
1. **Phase 1 (Boulder 2 -> Switch 1 @ (1, 16)) [SOLVED & VERIFIED Turn 23674-23676]**:
   - Initial position: Boulder 2 at (4, 14).
   - Verified Push Sequence: (4, 14) -> (3, 14) -> (3, 15) -> (3, 16) -> (2, 16) -> (1, 16) [Switch Plate 1].
   - **Result**: Shutter 1 at (5, 10) is OPEN (physically walked through at Turn 23676).

2. **Phase 2 (Boulder 1 onto row 3 @ (5, 3)) [SOLVED & VERIFIED Turn 23703-23704]**:
   - Initial position: Boulder 1 at (5, 5).
   - Push Sequence: Pushed North from (5, 6) -> (5, 4) -> (5, 3) on row 3!
   - **Result**: Boulder 1 is positioned at (5, 3) on the row 3 upper highway.

3. **Phase 3 (Circumvent via Eastern Ramp to row 3 @ (6, 3)) [IN PROGRESS]**:
   - Route: From (5, 4), walk south through Shutter 1 (5, 10) to (5, 8).
   - Walk east along Central Corridor (row 8) to (13, 8) -> south to (13, 12) -> east along row 12 to (19, 12).
   - Walk north up Eastern Ramp: (19, 11) -> (19, 8) -> (19, 3) onto upper highway!
   - Walk west along row 3: (19, 3) -> (9, 3) -> (6, 3).
   - Stand at (6, 3) facing West towards Boulder 1 at (5, 3).

4. **Phase 4 (Push Boulder 1 West to clear NW Ladder @ (1, 1))**:
   - From (6, 3), push Boulder 1 West: (5, 3) -> (4, 3) -> (3, 3) -> (2, 3) -> (1, 3).
   - Walk north: (1, 3) -> (1, 2) -> (1, 1) [Ladder up to Victory Road 3F!].

## Battle Escape Protocol (Standardized)
- Turn 1: Dismiss intro text with `['A', 'B']`.
- Turn 2: Select RUN from battle menu with `['Down', 'Right', 'A']`.
- Turn 3: Clear "Got away safely!" textbox with `['A']` or `['B']`.
