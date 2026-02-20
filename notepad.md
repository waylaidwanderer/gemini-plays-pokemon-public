### Puzzle Logic Matrix (Verified via Tool/Obs)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | W(11,10) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| ON | ON | ON | Closed | Closed | OPEN | Closed | 1-1-1 |
| OFF | OFF | ON | Closed | OPEN | Closed | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | Closed | 1-0-0 |
| ON | OFF | ON | Closed | Closed | Closed | Closed | 1-0-1 (Hint?) |
| OFF | ON | OFF | ? | ? | ? | ? | **TESTING** |

### Plan: 0-1-0 (OFF-ON-OFF)
1. Turn Sw2 ON (currently OFF).
2. Check States.
3. Turn Sw1 OFF (currently ON).
4. Check States.
5. If fail, try other combos using `check_gate_states`.

### Items/Objects
- Burglar Duncan (9,12)
- Director (South Room)