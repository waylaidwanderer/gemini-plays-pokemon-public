### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 (Confirmed Closed) |
| ON | ON | OFF | OPEN | OPEN | Closed | 1-1-0 (11,10 is CLOSED - Failed) |
| OFF | ON | OFF | Closed | OPEN | Closed | 0-1-0 (Try this next for 11,10) |
| ON | OFF | OFF | OPEN | Closed | ? | 1-0-0 (11,6 CLOSED - Sw2 controls door) |
| OFF | OFF | ON | OPEN | Closed | ? | 0-0-1 (Checking Gate 3) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 (Inner 2,10 Closed) |

### Strategy: Test 0-1-0 (Inner Wall 11,10)
- **Current:** 1-1-0 (Sw1 ON, Sw2 ON).
- **Step 1:** Go to Sw1 (16,1) -> Turn OFF.
- **Result:** 0-1-0 (Sw1 OFF, Sw2 ON).
- **Step 2:** Check Inner Wall at (11,10).
- **Reason:** Sw2 keeps (11,6) open. Sw1 might toggle (11,10).