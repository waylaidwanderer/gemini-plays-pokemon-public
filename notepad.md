### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 (Confirmed Closed) |
| ON | ON | OFF | OPEN | OPEN | Closed | 1-1-0 (11,10 is CLOSED - Failed) |
| OFF | ON | OFF | Closed | OPEN | Closed | 0-1-0 (11,10 is CLOSED) |
| ON | OFF | OFF | OPEN | Closed | ? | 1-0-0 (11,6 CLOSED - Sw2 controls door) |
| OFF | OFF | ON | OPEN | Closed | ? | 0-0-1 (Checking Gate 3) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 (Inner 2,10 Closed) |

### Strategy: Reach 1-0-0
- **Current:** 1-0-1 (Sw1 ON, Sw2 OFF, Sw3 ON).
- **Goal:** 1-0-0 (Sw1 ON, Sw2 OFF, Sw3 OFF).
- **Step 1:** Turn Sw1 ON (Realized it was OFF).
- **Step 2:** Go to Sw3 (2,1) -> Turn OFF.
- **Step 3:** Check Gate 3 (16,6).
- **Hypothesis:** Sw1 might open Gate 3.
- **Status:** Turning Sw1 ON, then moving to Sw3.