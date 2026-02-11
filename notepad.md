# Team Rocket HQ - Murkrow Puzzle (REVISED SOLUTION)

## STATUS: RESETTING
**Goal**: Open Boss Door at (22, 14).
**Method**: "Double Shimmy" at Statue (6, 1).

## The Logic
- Statue at (6, 1) is CONFIRMED solid.
- We will use it to desync BOTH X and Y axes.

## Step-by-Step Plan
1. **Reset**:
   - Go to (3, 14) -> B1F -> B2F.
   - Navigate to (7, 2).
   - **Target State**: P(7, 2), M(7, 1).
2. **X-Shimmy (Create X+1 Offset)**:
   - Move Left to (6, 2).
   - P->(6, 2). M->(6, 1) [Blocked].
   - **State**: P(6, 2), M(7, 1).
3. **Position for Y-Shimmy**:
   - Move Down to (6, 3). P(6, 3), M(7, 2).
   - Move Left to (5, 3). P(5, 3), M(6, 2).
4. **Y-Shimmy (Create Y+1 Offset)**:
   - Move Up to (5, 1).
   - P->(5, 1). M(6, 2)->(6, 1) [Blocked by Statue].
   - **State**: P(5, 1), M(6, 2). (Offsets: X=+1, Y=+1).
## Current State
- P(15, 2). M(15, 3) [M is Y+1].
- **Status**: Moving to (25, 2).
- **Goal**: Reach (25, 2) to start Y-Sync.

## The "Right Side Weave" Plan
1. **Navigate to (25, 2)**:
   - Continue Right to (25, 2). (M -> 25, 3).
2. **Weave to Sync**:
   - Down to (25, 7). (M -> 25, 8 Wall -> Stays 25, 7). **Syncs Y**.
   - Right to (26, 7).
   - Down to (26, 9).
   - Left to (25, 9).
   - Down to (25, 13).
   - Left to (22, 13).
3. **Open Door**:
   - P & M at (22, 13). Interact.

## Immediate Action
- Right x 10.