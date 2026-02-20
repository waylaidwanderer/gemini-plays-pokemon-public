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
| ON | ON | OFF | ? | ? | ? | 1-1-0 (Untested) |

### Strategy: Test 1-1-0 (ON-ON-OFF)
- **Current:** 0-1-0. Wall at (11,10) is CLOSED.
- **Plan:** Go North through Gate 2, Turn Sw1 ON.
- **Goal:** Check if 1-1-0 opens Wall (11,10) or other gates.