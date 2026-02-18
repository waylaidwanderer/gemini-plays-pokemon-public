Current State: S1=1, S2=0, S3=0 (Testing).
Previous: S1=0, S2=0, S3=0 (Reset Complete).

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 1  | 0  | 0  | ?        | ?         | ?         | ?        | Testing 1-0-0. |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed (Reset). |
| 0  | 1  | 1  | Closed   | Closed    | OPEN      | Closed   | Verified G1 Closed. |
| 0  | 1  | 0  | Closed   | OPEN      | OPEN      | OPEN     | Verified G1 Closed. |
| 0  | 0  | 1  | Closed   | ?         | OPEN      | ?        | Verified G1 Closed. |
| 1  | 1  | 1  | Closed   | OPEN      | Closed    | OPEN     | G2, Sec. Door Open. (11,10) Closed. |
| 1  | 0  | 1  | Closed?  | OPEN      | OPEN      | OPEN     | Gate 2, 3, Sec. Door Open. (11,10) Closed. |