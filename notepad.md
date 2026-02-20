### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 |
| OFF | OFF | ON | Closed | Closed | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 (Inner 2,10 Closed) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 |
| OFF | ON | ON | Closed | Closed | Closed | 0-1-1 |
| OFF | ON | OFF | Closed | OPEN | Closed | 0-1-0 (Wall 11,10 Closed) |
| OFF | OFF | OFF | ? | ? | Closed | 0-0-0 (Testing...) |
| ON | ON | OFF | ? | OPEN | Closed | 1-1-0 (Wall 11,10 Closed) |

### Strategy: Test 0-0-0 (All OFF)
- **Current:** 0-0-0.
- **Plan:** Check Gate 2 (10,6) then Gate 1 (2,6).
- **Goal:** Establish "Reset" state.
- **Hypothesis:** 0-0-0 closes everything.
- **Next:** If all closed, try "Order" sequence (Start with Sw3?).
- **Conflict:** Summary says 1-0-1 or 1-1-1 might open Gate 3. Re-test if needed.