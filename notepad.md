### Puzzle Logic Matrix (Hard Facts - Physical Bumps)
| Sw1(R) | Sw2(M) | Sw3(L) | G1(2,6) | G2(10,6) | G3(16,6) | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ON | ON | ON | Closed | Closed | Closed | 1-1-1 (Confirmed Closed) |
| OFF | OFF | ON | OPEN | Closed | ? | 0-0-1 (Checking Gate 3) |
| ON | OFF | OFF | OPEN | Closed | Closed | 1-0-0 (Inner 2,10 Closed) |
| ON | OFF | ON | Closed | Closed | Closed | 1-0-1 (Confirmed Closed) |

### Strategy: Test 1-0-0
- **Current:** 1-0-1.
- **Action:** Go to Sw3 (2,2) -> Turn OFF.
- **Goal:** Reach state 1-0-0 (Only Sw1 ON).
- **Hypothesis:** Symmetry. Sw1 -> Gate 3?
- **Step 1:** Move to (2,5) via Row 5 (Safe).
- **Step 2:** Move Up to Sw3 (Check Safe 2,4).