Current State: S1=0, S2=1, S3=1 (Testing).
Previous: S1=0, S2=1, S3=0.

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 1  | 0  | 1  | Closed   | Closed    | OPEN      | Closed   | Right Part explored. (11,10) Closed. |
| 0  | 0  | 1  | Closed | Closed    | OPEN      | Closed   | Gate 3 Open. Trap (16,8) Safe. Checking (11,10). |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed. |
| 0  | 1  | 0  | Open     | Closed    | Closed    | Closed   | G1 Open. |
| 1  | 1  | 1  | Closed   | Closed    | Closed    | Closed   | All Closed. |
| 1  | 1  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed. |
| 1  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed. |

Plan:
1. Verify 0-1-1 (Check Gate 1).
2. Go to Switch 2, Toggle OFF -> 0-0-1.
3. Check 0-0-1.
4. Go to Switch 1, Toggle ON -> 1-0-1.
5. Go through Gate 3 and check Wall (11, 10).