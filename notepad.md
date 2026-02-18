Current State: S1=0, S2=1, S3=0 (Testing).
Previous: S1=0, S2=0, S3=0.

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 0  | 1  | 0  | ?        | ?         | ?         | ?        | Testing 0-1-0. |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed (Assumed). |
| 0  | 0  | 1  | Closed   | ?         | OPEN      | ?        | Verified G1 Closed. |
| 0  | 1  | 1  | Closed   | Closed    | OPEN      | Closed   | Verified: 0-1-1 G1 Closed. |
| 1  | 1  | 1  | Closed   | OPEN      | Closed    | OPEN     | G2, Sec. Door Open. (11,10) Closed. |
| 1  | 0  | 1  | Closed?  | OPEN      | OPEN      | OPEN     | Gate 2, 3, Sec. Door Open. (11,10) Closed. |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed. |
| 0  | 1  | 0  | Open     | Closed    | Closed    | Closed   | G1 Open. |
| 1  | 1  | 1  | Closed   | Closed    | Closed    | Closed   | All Closed. |
| 1  | 1  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed. |
| 1  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed. |

Plan:
1. Turn Switch 2 ON (State 0-1-0).
2. Check Gate 1.
3. If Closed, Turn Switch 3 ON (State 0-1-1).
4. Check Gate 1.
5. If Closed, maybe the key is S3=1 ONLY (0-0-1)? But I tested that.
6. Maybe S1 needs to be involved?