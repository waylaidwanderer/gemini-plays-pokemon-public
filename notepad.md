# Warehouse Switch Puzzle - Scientific Log
- Objective: Open path to Director (9, 12).
- Shutters to Monitor: (3, 6), (6, 8), (12, 8).

## Current State
- Switch 3 (2, 1): OFF (Verified).
- Switch 2 (10, 1): OFF (Verified).
- Switch 1 (16, 1): ON (Executing).

## Switch Effects Table
| Switch | State | (3,6) | (6,8) | (12,8) |
|--------|-------|-------|-------|--------|
| All    | OFF   | Closed | Closed | Closed |
| 1      | ON    | ?     | ?     | ?      |
| 2      | ON    | ?     | ?     | ?      |
| 3      | ON    | ?     | ?     | ?      |

## Plan
1. Reset Complete (All OFF).
2. Inspect ALL 3 shutters to establish Baseline (All OFF) - Done.
3. Test Switch 1 ON -> Inspect (Executing).
   - Turn ON (Done).
   - Check (12, 8), (6, 8), (3, 6).
4. Test Switch 2 ON -> Inspect.
5. Test Switch 3 ON -> Inspect.