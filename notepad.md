### Puzzle Logic Matrix (Verified)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | W(11,10) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| ON | ON | ON | ? | ? | OPEN | Closed | 1-1-1 |
| OFF | OFF | ON | Closed | OPEN | Closed | Closed | 0-0-1 |
| ON | OFF | OFF | OPEN | Closed | Closed | Closed | 1-0-0 |
| OFF | ON | OFF | OPEN | Closed | Closed | Closed | 0-1-0 |
| OFF | ON | ON | OPEN | Closed | Closed | Closed | 0-1-1 |
| ON | OFF | ON | ? | Closed | Closed | ? | **TARGET 1-0-1** |

### Plan: Execute "ON OFF ON" (1-0-1)
1. Current: 0-1-1.
2. Go to Sw2 (10,1), Turn OFF -> 0-0-1.
3. Go to Sw1 (16,1), Turn ON -> 1-0-1.
4. Check Gates & Walls.
5. If (2,10) or (11,10) Open, proceed.

### Status
- Sw1: OFF
- Sw2: ON
- Sw3: ON