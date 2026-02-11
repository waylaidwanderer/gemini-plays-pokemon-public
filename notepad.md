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
- P(5, 1). M(6, 2) [Calculated].
- **Status**: Double Shimmy Complete. X=+1, Y=+1.
- **Action**: Syncing X at Right Wall.

## The Plan (Finish)
5. **Sync X (Right Wall)**:
   - Move Right to (28, 1).
   - P -> (28, 1).
   - M(6, 2) -> (28, 2) -> (29, 2) [Blocked by Wall].
   - **State**: P(28, 1), M(28, 2). (Synced X, Y+1).
6. **Deliver**:
   - Move Left to (22, 1).
   - Move Down to (22, 13).
   - Interact.

## Immediate Action
- Move Right to (28, 1).