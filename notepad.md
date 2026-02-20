### Puzzle Logic Matrix (Physical Verification Only)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | ? | ? | OPEN | 1-1-1 (Previous) |
| OFF | OFF | ON | Closed | OPEN | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 (Current) |

### Strategy: Test 1-1-1 (ON-ON-ON)
- **Current:** 1-0-1.
- **Action:** Turn Sw2 ON -> 1-1-1.
- **Expectation:** Gate 3 (16,6) opens.
- **Plan:**
  1. Go to Sw2 (10,1). Toggle ON.
  2. Check Gate 2 (10,6).
  3. Go to Gate 3 (16,6). Check/Enter.
  4. If in, check Wall (11,10) and Wall (6,9).
- **Goal:** Find a path to the Director.