### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 |
| OFF | OFF | ON | Closed | Closed | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 (Inner 2,10 Closed) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 |
| OFF | ON | ON | Closed | Closed | Closed | 0-1-1 |
| OFF | ON | OFF | Closed | OPEN | ? | **CURRENT TEST (0-1-0)** |
| OFF | OFF | OFF | ? | ? | ? | 0-0-0 (Untested) |
| ON | ON | OFF | ? | ? | ? | 1-1-0 (Untested) |

### Strategy: Test 0-1-0 (OFF-ON-OFF)
- **Status:** Sw1=OFF, Sw2=ON, Sw3=OFF.
- **Observation:** Gate 2 (10,6) is OPEN.
- **Action:** Walking South to check Wall (11,10).
- **Risk:** Tiles (10,9) and (11,9) might be traps.
- **Contingency:** If I warp, 0-1-0 is a dead end or trap path. Next try 0-0-0.