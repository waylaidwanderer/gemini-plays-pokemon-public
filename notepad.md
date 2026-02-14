# Warehouse Switch Puzzle - Truth Table
| Sw3 | Sw2 | Sw1 | (3,6) | (6,6) | (6,8) | (12,8) | Notes |
|-----|-----|-----|-------|-------|-------|--------|-------|
| ON  | ON  | ON  | Closed| Closed| Closed| Closed | Tested 42152 |
| ON  | OFF | ON  | Closed| Closed| Open  | Open   | Tested 42135, 42153 |
| OFF | OFF | ON  | Closed| Closed| Open  | Open   | Tested 42154 |
| OFF | ON  | ON  | Closed| Closed| Open  | Open   | Tested 42156 |
| OFF | ON  | OFF | Closed| Closed| Open  | Closed | Tested 42161 (Current) |

# Deduction
- (6, 6) remains Closed.
- (6, 8) is Open with Sw1 OFF! (New finding).
- So Sw1 ON is NOT required for (6, 8) to be Open.
- Sw2 ON seems to keep (6, 6) Closed?
- Strategy: Turn Sw2 OFF.
- New State: [Sw3 OFF, Sw2 OFF, Sw1 OFF] (All OFF).
- If that fails, Turn Sw3 ON -> [Sw3 ON, Sw2 OFF, Sw1 OFF].
- Clue: "Switch on the end first" -> Start with Sw3 ON.

# Plan
1. Turn Switch 2 OFF.
2. Check (6, 6).
3. If Closed, Go to Switch 3 and Turn ON.