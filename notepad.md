# Murkrow Puzzle: Navigation via Overlap

## Current State
- P(21, 1). M(20, 1).
- **Strategy**: Overlap to navigate maze as single unit.
- **Previous Failure**: likely due to getting blocked by walls in Col 21, never reaching door.

## Execution Plan
1. **Overlap**:
   - Move Left to (1, 1).
   - M blocked at (0, 1), P catches up.
   - **Result**: P(1, 1), M(1, 1).
2. **Navigate Maze (Battle Route)**:
   - Move Right to (2, 1).
   - **Bypass Grunt at (2, 4)**:
     - Path: (2, 1) -> (2, 3) -> (3, 3) -> (3, 5) -> (2, 5).
     - *Reason*: (1, 4) is Warp Trap, (2, 4) is Grunt. (3, 4) is Clear.
   - **Tank Traps**:
     - Continue Down Col 2 to (2, 15).
     - Tank traps at (2, 10-12).
3. **Approach Door**:
   - Right to (22, 15). (Avoid 5, 15 Warp).
   - Up to (22, 13).
   - **Try 1**: Interact Overlapped.

## Immediate Action
- Move Right to (2, 1). Then Down to (2, 3).