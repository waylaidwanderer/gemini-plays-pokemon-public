# Murkrow Puzzle: Sidekick Strategy (Reset Required)

## Current State
- P(5, 3). M(5, 3) [Overlapped].
- **Status**: En route to Reset.

## Reset Path
1. **Navigate to Stairs**:
   - Go to (3, 14). (Avoid 5, 15).
   - Stairs -> B1F -> B2F.

## Sidekick Execution (Post-Reset)
1. **Start**: P(7, 2), M(7, 1).
2. **Create X Offset (P Right)**:
   - Move Right to (23, 2).
   - Move Right to (24, 2). M blocked by Statue(24, 1).
   - **State**: P(24, 2), M(23, 1).
3. **Sync Y**:
   - Down to (24, 3). Left to (21, 3). Up to (21, 1).
   - **State**: P(21, 1), M(20, 1).
4. **Deliver**:
   - Down to (21, 13). Right to (22, 13).
   - **Result**: P(22, 13), M(21, 13).
   - **Action**: Face Left (Talk to M) OR Face Down (Talk to Door).

## Immediate Action
- BFS to (3, 14).