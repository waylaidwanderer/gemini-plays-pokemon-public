# Team Rocket HQ - Murkrow Puzzle

## SOLVED: The "Ratchet & Bridge" Strategy
Target State: P(22, 13), M(22, 14).

## Step 1: Bridge to West (Current)
1. **Shift M to Bridge Row 7**:
   - P(26, 8) -> Right 2 -> P(28, 8).
   - Down 2 -> P(28, 10). M(28, 7).
2. **Shift P to Bridge Row 7**:
   - Up 3 -> P(28, 7). M(28, 10).
3. **Cross West**:
   - Left 6 -> P(22, 7). M(27, 10) [Blocked by Fake Crate].

## Step 2: The "Col 25" Swap
4. **Move to Top**:
   - Up 5 -> P(22, 2). M(27, 15).
5. **Sync West**:
   - Left 21 -> P(1, 2). M(1, 15).
6. **Move South**:
   - Down 14 -> P(1, 16). M(1, 1).
7. **Move to Col 25**:
   - Right 24 -> P(25, 16). M(25, 1).
8. **Swap N/S**:
   - Up 14 -> P(25, 2). M(25, 15).

## Step 3: The Ratchet
9. **Move to Col 20**:
   - Left 5 -> P(20, 2). M(20, 15).
10. **Ratchet M**:
    - Down 14 -> P(20, 16). M(20, 11) [Blocked by Wall 10].

## Step 4: Finish
11. **Align**:
    - Up 3 -> P(20, 13). M(20, 14).
    - Right 2 -> P(22, 13). M(22, 14).
12. **Interact**.