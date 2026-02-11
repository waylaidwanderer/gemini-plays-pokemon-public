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
- P(7, 2). M(7, 1).
- **Status**: Executing "Double Shimmy" - Step 2.

## Step-by-Step Execution
1. **Reset**: [Done].
2. **X-Shimmy (Create X+1 Offset)**:
   - **Action**: Move Left to (6, 2).
   - **Expected**: P->(6, 2). M(7, 1)->(6, 1) [Blocked]. M stays (7, 1).
   - **Result State**: P(6, 2), M(7, 1).
3. **Position for Y-Shimmy**:
   - Move Down to (6, 3).
   - Move Left to (5, 3).
4. **Y-Shimmy (Create Y+1 Offset)**:
   - Move Up to (5, 1).
   - M blocked at (6, 1) again.
5. **Sync X**:
   - Move Right to Right Wall.
6. **Deliver**:
   - Navigate to Door.

## Immediate Action
- Move Left to (6, 2).