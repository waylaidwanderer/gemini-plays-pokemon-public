# Warehouse Switch Puzzle - Strategy
- Clue: "The switch on the end is the one to press first." -> Start with Switch 3.
- Current State: Switch 3 ON, Switch 2 ON, Switch 1 OFF.
- Observations: 
  - (3, 6) Closed (was open?).
  - (10, 2) Closed (blocking South access to Switch 2).
  - (12, 8) Closed (Trap path).
- Hypothesis: Switch 1 was keeping (10, 2) and (3, 6) open.
- Goal: Test [Switch 3 ON, Switch 2 OFF, Switch 1 OFF].

## Plan
1. Approach Switch 2 (10, 1) via Row 1 (since Row 2 is blocked).
2. Turn Switch 2 OFF.
3. Check for open paths (Column 3 or 6).
4. Watch out for traps at (3, 9) if symmetric to (12, 9).