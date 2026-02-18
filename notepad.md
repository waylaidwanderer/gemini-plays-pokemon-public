Location: Warehouse (10, 2) - At Switch 2.
Objective: Open Gate 2 (10, 6) or find path to Director (6, 8).

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 1  | 0  | 1  | Closed   | Closed    | OPEN      | Closed   | Right Part explored. (11,10) Closed. Dead end? |
| 0  | 0  | 1  | OPEN     | Closed    | Closed    | Closed   | G1 Opens. |
| 0  | 0  | 0  | Open     | Closed    | Closed    | Closed   | G1 stays Open. |
| 0  | 1  | 0  | Open     | Closed    | Closed    | Closed   | G1 stays Open. |
| 0  | 1  | 1  | Open     | Closed    | Closed    | Closed   | G1 stays Open. |
| 1  | 1  | 1  | Closed   | Closed    | Closed    | Closed   | All Closed. |
| 1  | 1  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed. Warp at (10,4)? |
| 1  | 0  | 0  | Closed   | Closed    | Closed    | ?        | CURRENT TEST. All Closed. Confirmed. |

Hypothesis:
- S1 OFF = Gate 1 Open? (Consistent in 0xx)
- S1 ON + S3 ON = Gate 3 Open? (Saw in 1-0-1)
- S2 might be the key for Gate 2. Maybe 1-0-0?
- Or maybe there is a specific order, not just state?
- Trap (10, 4) is active in some states.

Plan:
1. Check Gate 2 (10, 6) in State 1-0-0.
2. If Closed, check Gate 3 (16, 6).
3. If Closed, check Gate 1 (2, 6).