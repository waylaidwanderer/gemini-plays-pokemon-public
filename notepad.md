### Puzzle Solution: Operation Rescue Director
- **Goal:** Find Real Director & Card Key.
- **Switch Logic Analysis:**
  - 0-0-1 (Sw3 ON): Gate 3 Open, Wall (16,10) Blocked.
  - 1-0-1 (Sw1+Sw3): Gate 3 Closed.
  - 1-0-0 (Sw1): Gate 3 Closed.
  - Need to reach East Room (Col 13+).
  - Paradox: Gate 3 needs Sw1 OFF? Wall (16,10) needs Sw1 ON?
- **Hypothesis:** Try 0-1-1 (Sw2 ON, Sw3 ON).
  - Maybe Sw2 opens Wall (16,10)?
- **Plan:**
  1. Exit West Room via (11,10).
  2. Turn Sw2 ON (State 0-1-1).
  3. Check Gate 3 & Wall (16,10).