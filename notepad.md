# Warehouse Switch Puzzle - Truth Table
| Sw3 | Sw2 | Sw1 | (3,6) | (6,6) | (6,8) | (12,8) | Notes |
|-----|-----|-----|-------|-------|-------|--------|-------|
| ON  | ON  | ON  | Closed| Closed| Closed| Closed | Tested 42152 |
| ON  | OFF | ON  | Closed| Closed| Open  | Open   | Tested 42135, 42153 |
| OFF | OFF | ON  | Closed| Closed| Open  | Open   | Tested 42154 |
| OFF | ON  | ON  | Closed| Closed| Open  | Open   | Tested 42156 |
| OFF | ON  | OFF | ?     | Closed| Open  | Closed | Tested 42161 |
| ON  | ON  | OFF | Closed| Closed| Open  | Closed | Tested 42118 |
| ON  | OFF | OFF | ?     | Closed| ?     | Closed | Tested 42126 |

# Deduction
- (6, 6) has NEVER opened. It might be a fake path.
- (3, 6) is the likely path.
- Untested states for (3, 6): [OFF, OFF, OFF] and [ON, OFF, OFF].
- Clue "Start with End Switch" implies [ON, OFF, OFF].

# Plan
1. Turn Switch 2 OFF (Reach [OFF, OFF, OFF]).
2. Check (3, 6).
3. If Closed, Turn Switch 3 ON (Reach [ON, OFF, OFF]).
4. Check (3, 6).