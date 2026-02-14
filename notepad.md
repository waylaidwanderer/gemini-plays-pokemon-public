# Warehouse Switch Puzzle - Truth Table
| Sw3 | Sw2 | Sw1 | (3,6) | (6,6) | (6,8) | (12,8) | Notes |
|-----|-----|-----|-------|-------|-------|--------|-------|
| ON  | ON  | ON  | Closed| Closed| Closed| Closed | Tested 42152 |
| ON  | OFF | ON  | Closed| Closed| Open  | Open   | Tested 42135, 42153 |
| OFF | OFF | ON  | Closed| Closed| Open  | Open   | Tested 42154 |
| OFF | ON  | ON  | Closed| Closed| Open  | Open   | Tested 42156 |
| OFF | ON  | OFF | ?     | ?     | ?     | ?      | Testing NOW |

# Deduction
- Sw1 ON definitely opens (6, 8) and (12, 8).
- (6, 6) has NEVER been open with Sw1 ON.
- Hypothesis: Sw1 ON closes (6, 6).
- Therefore, Sw1 must be OFF to open (6, 6).
- **Target State:** [Sw3 OFF, Sw2 ON, Sw1 OFF].

# Plan
1. Toggle Switch 1 OFF.
2. Check (12, 8) (Should close).
3. Check (6, 6) and (6, 8).