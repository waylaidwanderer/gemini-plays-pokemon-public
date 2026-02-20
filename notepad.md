### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 |
| OFF | OFF | ON | OPEN | Closed | Closed | 0-0-1 (Confirmed) |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 (Inner 2,10 Closed) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 |
| OFF | ON | ON | Closed | Closed | Closed | 0-1-1 |
| OFF | ON | OFF | Closed | OPEN | Closed | 0-1-0 (Wall 11,10 Closed) |
| OFF | OFF | OFF | Closed | Closed | Closed | 0-0-0 (Confirmed Reset) |

### Strategy: Test Order 3-2-1
- **Current:** 0-0-0.
- **Hypothesis:** Order matters (Burglar Hint).
- **Sequence:**
  1. Turn Sw3 ON (-> 0-0-1). Check Gate 1.
  2. Turn Sw2 ON (-> 0-1-1). Check Gate 2.
  3. Turn Sw1 ON (-> 1-1-1). Check Gate 3.
- **Note:** Summary claims 1-1-1 opens back area. I previously found it closed. Maybe sequence fixes this?