Current State: S1=0, S2=1, S3=0 (Moving to Reset).
Previous: S1=0, S2=1, S3=1 (Verified G1 Closed).

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 0  | 1  | 1  | Closed   | Closed    | OPEN      | Closed   | Verified G1 Closed. |
| 0  | 1  | 0  | Closed   | OPEN      | OPEN      | OPEN     | Verified G1 Closed. |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed (Assumed). |
| 0  | 0  | 1  | Closed   | ?         | OPEN      | ?        | Verified G1 Closed. |
| 1  | 1  | 1  | Closed   | OPEN      | Closed    | OPEN     | G2, Sec. Door Open. (11,10) Closed. |
| 1  | 0  | 1  | Closed?  | OPEN      | OPEN      | OPEN     | Gate 2, 3, Sec. Door Open. (11,10) Closed. |
| 0  | 1  | 0  | Open     | Closed    | Closed    | Closed   | G1 Open (Wait, did I verify this? No, it says Closed above). |

Plan:
1. Turn S3 OFF (State 0-1-0).
2. Turn S2 OFF (State 0-0-0).
3. Turn S1 ON (State 1-0-0).
4. Check Gates.