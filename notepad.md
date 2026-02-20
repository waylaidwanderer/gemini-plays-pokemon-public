### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 (Confirmed Closed) |
| OFF | OFF | ON | OPEN | Closed | Closed | 0-0-1 (Confirmed) |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 (Inner 2,10 Closed) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 (Confirmed Closed) |
| OFF | ON | ON | ? | ? | ? | 0-1-1 (Testing...) |
| OFF | ON | OFF | Closed | OPEN | Closed | 0-1-0 (Wall 11,10 Closed) |
| OFF | OFF | OFF | Closed | Closed | Closed | 0-0-0 (Confirmed Reset) |

### Strategy: Test 0-1-1
- **Current:** 0-1-1.
- **Action:** Check Gate 3 (16,6).
- **Goal:** Find Open Gate 3.
- **Next:** If 0-1-1 fails, try 0-0-1 or 1-0-0.