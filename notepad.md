# Warehouse Switch Puzzle - Truth Table
| Sw3 | Sw2 | Sw1 | (3,6) | (6,6) | (6,8) | (12,8) | Notes |
|-----|-----|-----|-------|-------|-------|--------|-------|
| ON  | ON  | ON  | Closed| Closed| Closed| Closed | Tested 42152 |
| ON  | OFF | ON  | Closed| Closed| Open  | Open   | Tested 42135, 42153 |
| OFF | OFF | ON  | Closed| Closed| Open  | Open   | Tested 42154 |
| OFF | ON  | ON  | Closed| Closed| Open  | Open   | Tested 42156 |
| OFF | ON  | OFF | ?     | Closed| Open  | Closed | Tested 42161 |
| OFF | OFF | OFF | Closed| ?     | ?     | ?      | Tested 42163 (Current) |

# Deduction
- With everything OFF, (3, 6) is Closed.
- "Switch on the end first" implies starting with Sw3 ON.
- **Target State:** [Sw3 ON, Sw2 OFF, Sw1 OFF].

# Plan
1. Move to Switch 3 (2, 1).
2. Turn Switch 3 ON.
3. Check (3, 6) and (6, 6).