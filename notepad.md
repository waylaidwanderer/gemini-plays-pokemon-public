### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 (Confirmed Closed) |
| OFF | OFF | ON | OPEN | Closed | ? | 0-0-1 (Checking Gate 3) |
| ON | OFF | OFF | OPEN | Closed | ? | 1-0-0 (Checking Gate 3) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 (Inner 2,10 Closed) |

### Strategy: Test 0-1-0 (Gate 3)
- **Current:** 1-0-0 (Sw1 ON).
- **Step 1:** Go to Sw1 (16,1) -> Turn OFF (-> 0-0-0).
- **Step 2:** Go to Sw2 (10,1) -> Turn ON (-> 0-1-0).
- **Step 3:** Check Gate 3.
- **Reason:** 0-1-0 is the last reasonable guess for Gate 3.