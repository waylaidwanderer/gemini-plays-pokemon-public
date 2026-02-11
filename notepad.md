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
- P(6, 2). M(Unknown, calculated 6,1 or 18,1).
- **Action**: Positioning for Y-Shimmy (or Y-Sync).

## Step-by-Step Execution
3. **Position for Y-Shimmy**:
   - **Action**: Move Down to (6, 3).
   - **Expected**: P(6, 3). M moves Down (to Row 2).
   - **Action**: Move Left to (5, 3).
   - **Expected**: P(5, 3). M moves Left.
4. **Y-Shimmy (Create Y+1 Offset)**:
   - **Action**: Move Up to (5, 1).
   - **Expected**:
     - If M was at (7, 1): Hits Statue (6, 1). Ends at Y=2. (Offset +1).
     - If M was at (19, 1): Hits Wall (Row 0). Ends at Y=1. (Synced).
5. **Sync X**:
   - Move Right to Right Wall.
6. **Deliver**:
   - Navigate to Door.

## Immediate Action
- Move Down, then Left.