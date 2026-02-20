### Puzzle Logic Matrix (Physical Verification Only)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | ? | Closed | Closed | 1-1-1 |
| OFF | OFF | ON | Closed | OPEN | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 |
| OFF | ON | ON | Closed | Closed | Closed | 0-1-1 |
| OFF | ON | OFF | ? | ? | ? | **CURRENT TEST (0-1-0)** |

### Strategy: Test 0-1-0 (OFF-ON-OFF)
- **Status:** Sw1=OFF, Sw2=ON, Sw3=OFF.
- **Hypothesis:** Maybe this combo opens Gate 1 and the inner door (2,10)?
- **Plan:**
  1. Check Gate 1 (2,6).
  2. If Open, check (2,10).
  3. If Closed, check Gate 2 (10,6) and Gate 3 (16,6).