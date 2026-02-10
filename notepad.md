# Team Rocket HQ - Murkrow Puzzle

## SOLVED: The "Double Ratchet" Strategy
Target State: P(22, 12), M(22, 13). Interact Down.

## Execution Path
1. **Setup**:
   - Start: P(26, 9), M(26, 8).
   - Up 1 -> P(26, 8), M(26, 9).
   - Left 4 -> P(22, 8), M(22, 9).
   - Up 3 -> P(22, 5), M(22, 12). (P Blocked Up at 5).

2. **Ratchet 1 (M Blocked Up at 5)**:
   - Down 11.
   - P 5->16.
   - M 12->5 (Stops at 5).
   - State: P(22, 16), M(22, 5).

3. **Ratchet 2 (P Blocked Down at 16)**:
   - Down 8.
   - P Stays 16.
   - M 5->13.
   - State: P(22, 16), M(22, 13).

4. **Convergence (M Blocked Down at 13)**:
   - Up 4.
   - P 16->12.
   - M 13->13 (Stops at 13, Blocked by Door).
   - State: P(22, 12), M(22, 13).

5. **Finish**:
   - Face Down. Press A.