# Warehouse Switch Puzzle - Scientific Log
- Objective: Open path to Director (9, 12).
- Shutters to Monitor: (3, 6), (6, 8), (12, 8).

## Current State
- Switch 3 (2, 1): OFF (Verified).
- Switch 2 (10, 1): OFF (Verified).
- Switch 1 (16, 1): OFF (Verified).

## Switch Effects Table
| Switch | State | (3,6) | (6,8) | (12,8) |
|--------|-------|-------|-------|--------|
| All    | OFF   | ?     | ?     | Closed |
| 1      | ON    | ?     | ?     | Open   |
| 2      | ON    | ?     | ?     | ?      |
| 3      | ON    | ?     | ?     | ?      |

## Plan
1. Reset Complete (All OFF).
2. Inspect ALL 3 shutters to establish Baseline (All OFF).
   - Check (12, 8) (Done: Closed).
   - Check (6, 8) (Next).
   - Check (3, 6).
3. Test Switch 1 ON -> Inspect.
4. Test Switch 2 ON -> Inspect.
5. Test Switch 3 ON -> Inspect.