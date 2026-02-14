# Warehouse Switch Puzzle - Internal Exploration
- **Status:** Inside the corridor (Row 8).
- **Position:** (12, 8).
- **Situation:** (9, 10) is a wall. (12, 7) appears to be closed behind me (One-way?).
- **Hypothesis:** Verify if Shutter (6, 8) is OPEN from the inside.
- **Goal:** Reach (6, 8) and check path South.
- **Contingency:** If (6, 8) is closed and (12, 7) is closed, I am trapped. Must use Trap (12, 9) to reset.

## Plan
1. Move West to (6, 8).
2. If Open, go South to (6, 12) -> Director.
3. If Closed, verify (12, 7) is closed.
4. If trapped, step on (12, 9).