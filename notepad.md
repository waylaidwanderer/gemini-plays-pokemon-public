# Warehouse Switch Puzzle - Scientific Log
- Objective: Open path to Director (9, 12).
- Shutters to Monitor: (3, 6), (6, 8), (12, 8).

## Current State
- Switch 3 (2, 1): ON (Executing).
- Switch 2 (10, 1): OFF (Verified).
- Switch 1 (16, 1): ON (Verified).

## Switch Effects Table
| Switch | State | (3,6) | (6,8) | (12,8) | Other |
|--------|-------|-------|-------|--------|-------|
| All    | OFF   | Closed | Closed | Closed | (16, 7) Closed |
| 1      | ON    | Closed | Closed | Open   | (16, 7) Open |
| 2      | ON    | ?     | ?     | ?      | ? |
| 3      | ON    | ?     | ?     | ?      | ? |

## Plan
1. Reset Complete (All OFF) - Done.
2. Baseline Established - Done.
3. Switch 1 ON - Done.
4. Test Switch 3 ON (with 1 ON) -> Inspect (Executing).
   - Turn Switch 3 ON.
   - Check (3, 6).
   - Check (6, 8).
5. If no change, Turn Switch 3 OFF and proceed to Switch 2.