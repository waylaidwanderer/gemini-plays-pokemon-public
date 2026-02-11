# Murkrow Puzzle Strategy: The "Sidekick" Approach

## Hypothesis
- Overlapping M on the door failed.
- The door likely requires M to be **adjacent** to the player or door, or interacted with directly.
- **Target State**: P at Door (22, 13). M at Left (21, 13).

## Execution Plan
1. **Reset**:
   - Go to Stairs (3, 14) -> B1F -> B2F.
   - **Start**: P(7, 2), M(7, 1).
2. **Create X Offset (P Right of M)**:
   - Move Right to (23, 2).
     - M(7->23) blocked by Statue(24, 1) at step 23.
     - M stops at (23, 1). P at (23, 2).
   - Move Right to (24, 2).
     - P -> (24, 2).
     - M(23, 1) -> (24, 1) [Blocked by Statue].
     - **State**: P(24, 2), M(23, 1). (P is Right +1).
3. **Sync Y**:
   - Move Down to (24, 3). M(23, 2).
   - Move Left to (21, 3). M(20, 2).
   - Move Up to (21, 1). M(20, 0) [Blocked] -> M(20, 1).
   - **State**: P(21, 1), M(20, 1). (Y Synced).
4. **Deliver**:
   - Move Down to (21, 13). M(20, 13).
   - Move Right to (22, 13). M(21, 13).
   - **Result**: P(22, 13), M(21, 13).
   - Interact with Murkrow (Face Left) or Door (Face Down).

## Immediate Action
- Navigate to Stairs (3, 14) to Reset.