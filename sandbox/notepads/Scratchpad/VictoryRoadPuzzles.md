# Victory Road Puzzle Mechanics & Master Log

## Floor 1F Puzzle System (SOLVED)
- Boulder at (5, 15) pushed via lower highway (row 16) to eastern corridor (14, 14) -> (16, 12) -> (17, 12) -> onto Switch (17, 13).
- Lowers shutters at (5, 13) and (7, 7), unlocking access to 2F Ladder at (1, 1).

## Floor 2F Master Solution (Systematic Protocol & Testing Plan)

### Two-Boulder Master Protocol:
1. **Phase 1 (Boulder 2 -> Switch 1 @ (1, 16))**:
   - Initial position: Boulder 2 at (4, 14).
   - Push sequence: (4, 14) -> (3, 14) -> (3, 15) -> (3, 16) -> (2, 16) -> (1, 16) [Switch Plate 1].
   - **Result**: Shutter 1 at (5, 10) OPENS permanently for the session.

2. **Phase 2 (Boulder 1 -> Switch 2 @ (9, 11))**:
   - Initial position: Boulder 1 at (5, 5) on Terrace.
   - Push sequence:
     a. Stand at (5, 4) or (4, 5) -> push Boulder 1 South to (5, 7).
     b. Stand at (6, 7) -> push Boulder 1 West to (3, 7).
     c. Stand at (3, 6) -> push Boulder 1 South to (3, 11) [Lower Highway].
     d. Stand at (2, 11) -> push Boulder 1 East to (5, 11).
     e. Stand at (5, 12) -> push Boulder 1 North through opened Shutter 1 (5, 10) to (5, 8) [Central Corridor].
     f. Stand at (4, 8) -> push Boulder 1 East along Central Corridor to (14, 8).
     g. Stand at (14, 7) -> push Boulder 1 South down Column 14 to (14, 11).
     h. Stand at (15, 11) -> push Boulder 1 West along Row 11 to (9, 11) [Switch Plate 2]!
   - **Result**: Shutters at (15, 15) and (21, 15) OPEN!

3. **Phase 3 (Ascend to 3F)**:
   - Walk south through opened Shutter (15, 15) / (21, 15) along row 16 directly onto SE platform.
   - Take SE Ladder at (25, 14) up to Victory Road 3F!

## Battle Escape Protocol (Standardized)
- Turn 1: Dismiss intro text with `['A', 'B']`.
- Turn 2: Select RUN from battle menu with `['Down', 'Right', 'A']`.
- Turn 3: Clear "Got away safely!" textbox with `['A']`.