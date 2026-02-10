# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "JED SANDWICH 5.0"
**Strategy**: Double Ratchet (X then Y) -> Jed Lock.
**Goal**: Open Boss Door at (22, 14).

## Step 1: Ratchet X (Current)
1. **Vertical Offset**: Up 1 -> P(9,1), M(9,3).
2. **Horizontal Ratchet**: Right 16.
   - P blocked at (24,1) Statue. Stops (23,1).
   - M moves to (25,3).
   - *Result*: M is +2 X relative to P.
3. **Realign Y**: Down 1 -> P(23,2), M(25,2).

## Step 2: Vertical Ratchet & Descent
4. **Move to Col 4**: Left 19.
   - P(4,2). M(6,2).
5. **Invert Y (Col 4 Gap)**: Down 14 (Batch: Down 6 to Row 8).
   - P goes down Col 4.
   - M blocked Up by Statue (6,1). M stays (6,2).

## Step 3: The Resync & Lock
6. **Move to Col 19**: Right 15. P(19,16), M(21,2).
7. **Position**: Up 11. P(19,5), M(21,13).
8. **Resync X**: Right 2. M blocked (23,13). P(21,5).
9. **Align Jed**: Left 3. P(18,5), M(18,13).
10. **Lock**: Down 11. M blocked by Jed. P(18,16), M(18,13).