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
   - Move Down to (2, 15).
   - *Hazards*: Grunt at (2, 4), Traps at (2, 10-12). Tank them.
3. **Approach Door**:
   - Right to (22, 15). (Avoid 5, 15 Warp).
   - Up to (22, 13).
   - **Try 1**: Interact Overlapped.
   - **Try 2**: If fails, desync to Sidekick using local walls.

## Immediate Action
- Move Left to (1, 1).