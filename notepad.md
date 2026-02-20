### Puzzle Logic Matrix (Physical Verification Only)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | ? | ? | OPEN | 1-1-1 |
| OFF | OFF | ON | Closed | OPEN | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 |
| ON | OFF | ON | Closed | ? | Closed | 1-0-1 |

### Strategy: Verify 1-0-1 (ON-OFF-ON)
- **Status:** Sw1=ON, Sw2=OFF, Sw3=ON.
- **Observation:** Gate 1 (2,6) is CLOSED.
- **Observation:** Gate 3 (16,6) is CLOSED.
- **Next Step:** Check Gate 2 (10,6).
- **Hypothesis:** If Gate 2 is also closed, 1-0-1 is a lockdown state.
- **Contingency:** If 1-0-1 fails, try 0-1-0 (OFF-ON-OFF).