### Puzzle Logic Matrix (Verified)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | W(11,10) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| ON | ON | ON | ? | ? | OPEN | Closed | 1-1-1 |
| OFF | OFF | ON | Closed | OPEN | Closed | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | Closed | 1-0-0 |
| OFF | ON | OFF | OPEN | Closed | Closed | Closed | 0-1-0 |
| OFF | ON | ON | OPEN | Closed | Closed | Closed | 0-1-1 |
| ON | OFF | ON | OPEN | Closed | Closed | Closed | 1-0-1 |

### Analysis of 1-0-1 (ON OFF ON)
- Gate 1 (2,6) is OPEN.
- Gate 2 & 3 are CLOSED.
- Wall (11,10) is CLOSED.
- **CRITICAL CHECK:** Is Gate (2,10) Open?
  - In 1-0-0, Gate 1 was Open but (2,10) was Closed.
  - In 1-0-1, maybe (2,10) opens?

### Plan
1. Check (2,10) status via code.
2. If Open -> Go to (2,10).
3. If Closed -> Panic/Re-think.