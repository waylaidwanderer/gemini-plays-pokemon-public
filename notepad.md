# Warehouse Switch Puzzle - Scientific Log
- Objective: Open path to Director (9, 12).
- Shutters to Monitor: (3, 6), (6, 8), (12, 8) and Row 10 Walls.

## Current State
- Switch 3 (2, 1): ON (Verified).
- Switch 2 (10, 1): OFF (Verified).
- Switch 1 (16, 1): ON (Verified).

## Switch Effects Table
| Switch | State | (3,6) | (6,8) | (12,8) | Other |
|--------|-------|-------|-------|--------|-------|
| All    | OFF   | Closed | Closed | Closed | (16, 7) Closed |
| 1      | ON    | Closed | Closed | Open   | (16, 7) Open |
| 3      | ON    | Closed | Open   | Open   | (6, 8) Confirmed by XML |
| 2      | ON    | ?     | ?     | ?      | ? |

## Plan
1. Reset Complete (All OFF) - Done.
2. Baseline Established - Done.
3. Switch 1 ON - Done.
4. Switch 3 ON - Done.
5. Inspect Row 9 and Row 10 barriers (Executing).
6. Toggle Switch 2.