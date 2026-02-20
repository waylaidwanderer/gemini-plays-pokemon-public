### Puzzle Logic Matrix (Physical Verification Only)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | ? | Closed | Closed | 1-1-1 |
| OFF | OFF | ON | Closed | OPEN | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 |
| OFF | ON | ON | ? | ? | ? | **CURRENT TEST (0-1-1)** |

### Strategy: Test 0-1-1 (OFF-ON-ON)
- **Status:** Sw1=OFF, Sw2=ON, Sw3=ON.
- **Plan:**
  1. Check Gate 3 (16,6).
  2. If Open, enter.
  3. If Closed, check Gate 2 (10,6) and Gate 1 (2,6).
  4. If all closed, try 0-1-0 (Sw3 OFF).