### Puzzle Logic Matrix (Physical Verification Only)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | ? | Closed | Closed | 1-1-1 |
| OFF | OFF | ON | Closed | OPEN | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 |
| OFF | ON | ON | ? | ? | Closed | **CURRENT TEST (0-1-1)** |

### Strategy: Test 0-1-1 (OFF-ON-ON)
- **Status:** Sw1=OFF, Sw2=ON, Sw3=ON.
- **Observation:** Gate 3 (16,6) is CLOSED (Bumped).
- **Next Step:** Check Gate 2 (10,6).
- **Plan:**
  1. Go to Gate 2 (10,6).
  2. If Open, enter.
  3. If Closed, check Gate 1 (2,6).