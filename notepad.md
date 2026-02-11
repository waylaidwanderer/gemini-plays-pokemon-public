# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING COL 26 STRATEGY
**Goal**: Open Boss Door at (22, 14) from (22, 13).
**Condition**: M must be at (22, 15) when P is at (22, 13).

## Step 1: Navigate to Bottom Right
- **Current**: (3, 2).
- **Route**:
  1. Right to (26, 2).
  2. Down to (26, 9) (Blocked).
  3. Left to (22, 9).
  4. Down to (22, 16).
  5. Right to (26, 16).

## Puzzle Status: RESET DETECTED
- **Event**: Warped to (24, 10) after attempting to interact with door/approaching (22, 16).
- **Hypothesis**: (22, 16) is a Warp Trap OR Incorrect Door Interaction warps player.
- **Next Step**: Check (7, 2) for Murkrow. If there, restart.

## Plan: "Statue Shimmy & Crate Flank" (Verified)

1. **Sync X & Top Ratchet**:
   - Go Right to (28, 2) + Bump Wall -> M at (28, 2).
   - Go Left to (24, 2) -> M at (24, 2).
   - Down to (24, 9) -> M hits Statue (24, 1), stays (24, 2).
     - *State*: P(24, 9), M(24, 2).

2. **Middle Ratchet**:
   - Up to (24, 2) -> M Down to (24, 9).
   - Down to (24, 9) -> M Up to (24, 6) (Blocked by Statue 24,5).
     - *State*: P(24, 9), M(24, 6).

3. **Deep Dive**:
   - Up to (24, 2) -> M Down to (24, 13).
     - *State*: P(24, 2), M(24, 13).

4. **Flank & Bottom Ratchet**:
   - Right to (26, 2) -> M Right to (26, 13).
   - Down to (26, 9) -> M Up to (26, 12) (Blocked by Obstacle 26,11).
     - *State*: P(26, 9), M(26, 12).
   - Up to (26, 6) -> M Down to (26, 15).
     - *State*: P(26, 6), M(26, 15).

5. **Unlock**:
   - Left to (22, 6) -> M Left to (22, 15).
   - Down to (22, 13) -> M blocked by Door (22, 14), stays (22, 15).
   - Interact.