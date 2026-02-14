# Warehouse Switch Puzzle - The Actual Solution
- **Discovery:** The path to the Director is via **Column 3**.
- **Route:** Enter (12, 8) -> West to (6, 8) -> West to (3, 8) -> South to (3, 12) -> East to Director.
- **Requirement:** Shutter (6, 8) MUST be OPEN. Shutter (12, 8) MUST be OPEN.
- **Winning Combo:** [Sw3 OFF, Sw2 ON, Sw1 ON].
  - Tested in Turn 42156: (6, 8) was OPEN. (12, 8) was OPEN.
- **Current State:** [Sw3 ON, Sw2 OFF, Sw1 ON]. (6, 8) is Closed.

## Plan
1. **Reset:** Step on Trap (12, 9) to warp back to Main Hall (12, 5).
2. **Adjust:** Turn Switch 3 OFF. Turn Switch 2 ON. (Keep Sw1 ON).
3. **Execute:** Enter (12, 8), go West to (3, 8), go South.