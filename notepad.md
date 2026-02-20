### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 (Confirmed Closed) |
| OFF | OFF | ON | OPEN | Closed | Closed | 0-0-1 (Confirmed) |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 (Inner 2,10 Closed) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 (Testing...) |
| OFF | ON | ON | Closed | Closed | Closed | 0-1-1 (Confirmed) |
| OFF | ON | OFF | Closed | OPEN | Closed | 0-1-0 (Wall 11,10 Closed) |
| OFF | OFF | OFF | Closed | Closed | Closed | 0-0-0 (Confirmed Reset) |

### Strategy: Test 1-0-1
- **Current:** 1-1-1.
- **Action:** Go to Sw2 (10,2), Turn OFF.
- **Goal:** Reach state 1-0-1.
- **Hypothesis:** Opens Gate 3.