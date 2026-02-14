# Warehouse Switch Puzzle - Truth Table
| Sw3 | Sw2 | Sw1 | (3,6) | (6,6) | (6,8) | (12,8) | Notes |
|-----|-----|-----|-------|-------|-------|--------|-------|
| ON  | ON  | ON  | Closed| Closed| Closed| Closed | Tested 42152 (Current) |
| ON  | OFF | ON  | Closed| ?     | ?     | Open   | Tested 42135 |
| ON  | ON  | OFF | ?     | Closed| Open  | ?      | Tested 42118-42122 |
| ON  | OFF | OFF | ?     | Closed| ?     | ?      | Tested 42126 |
| OFF | OFF | ON  | Closed| ?     | ?     | Open   | Tested 42140 |

# Hypothesis
- Sw2 ON opens (6, 8).
- Sw1 ON opens (6, 6) or (12, 8).
- Sw3 ON might be closing (6, 6).
- **Target State:** [Sw3 OFF, Sw2 ON, Sw1 ON].

# Plan
1. Turn Sw3 OFF (Currently at Sw3).
2. Check (6, 6) and (6, 8).
3. If fails, try [Sw3 OFF, Sw2 OFF, Sw1 ON] (Turn Sw2 OFF).