### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 |
| OFF | OFF | ON | Closed | Closed | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 (Inner 2,10 Closed) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 |
| OFF | ON | ON | Closed | Closed | Closed | 0-1-1 |
| OFF | ON | OFF | Closed | OPEN | Closed | 0-1-0 (Wall 11,10 Closed) |
| OFF | OFF | OFF | ? | ? | ? | 0-0-0 (Untested) |
| ON | ON | OFF | ? | OPEN | Closed | 1-1-0 (Wall 11,10 Closed) |

### Strategy: Reset to 0-0-0
- **Current:** 1-1-0 (Wall 11,10 CLOSED).
- **Plan:** Go North through Gate 2.
- **Action 1:** Turn Sw2 OFF (-> 1-0-0).
- **Action 2:** Turn Sw1 OFF (-> 0-0-0).
- **Goal:** Test 0-0-0 state. Maybe it opens the middle wall?