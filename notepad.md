# Murkrow Puzzle Strategy: The "Sidekick" Approach

## Hypothesis
- Overlapping M on the door failed.
- The door likely requires M to be **adjacent** to the player or door, or interacted with directly.
- **Target State**: P at Door (22, 13). M at Left (21, 13).

## Current State
- P(24, 2). M(23, 1) [Calculated].
- **Status**: X Offset Set (P is Right +1).
- **Action**: Syncing Y.

## Execution Plan
3. **Sync Y**:
   - Move to (21, 1).
   - Path: Left to (21, 2), Up to (21, 1).
   - M behavior:
     - Left to (20, 1).
     - Up to (20, 0) -> Blocked -> (20, 1).
   - **Result**: P(21, 1), M(20, 1). (Y Synced).
4. **Deliver**:
   - Move Down to (21, 13). M(20, 13).
   - Move Right to (22, 13). M(21, 13).
   - Interact.

## Immediate Action
- BFS to (21, 1).