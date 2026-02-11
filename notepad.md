# Team Rocket HQ - Murkrow Puzzle (Solution Found)

## STATUS: RESETTING FOR SOLUTION
**Goal**: Open Boss Door at (22, 14).
**Requires**: Murkrow ON the door tile (22, 14) while P interacts from (22, 13).
**Current State**: Synced (Failed). Must Reset.

## The "Statue Shimmy" Solution
1. **Reset**:
   - Go to (3, 14) -> B1F -> B2F.
   - **Start State**: P(7, 2), M(7, 1). (X synced, Y offset -1).
2. **Create X Offset (P Left of M)**:
   - Move Left to (6, 2).
   - P -> (6, 2). M -> (6, 1) (Blocked by Statue).
   - **State**: P(6, 2), M(7, 1). (X_M = X_P + 1).
3. **Align for Y Shimmy**:
   - Move Right to (23, 2).
   - **State**: P(23, 2), M(24, 1).
4. **Sync Y (Top Wall)**:
   - Move Up to (23, 1). P(23, 1). M(24, 0) Blocked.
   - **State**: P(23, 1), M(24, 1).
5. **Position for Shimmy**:
   - Move Down to (23, 2).
   - **State**: P(23, 2), M(24, 2).
6. **Execute Y Shimmy (Create M South Offset)**:
   - Move Up to (23, 1).
   - P -> (23, 1). M -> (24, 1) (Blocked by Statue).
   - **State**: P(23, 1), M(24, 2). (Y_M = Y_P + 1).
7. **Remove X Offset**:
   - Move Right to (28, 1).
   - P -> (28, 1). M -> (29, 2) (Blocked by Wall).
   - **State**: P(28, 1), M(28, 2). (X Synced, Y Offset +1).
8. **Deliver**:
   - Move Left to (22, 1).
   - Move Down to (22, 13).
   - **State**: P(22, 13), M(22, 14).
   - Interact.

## Immediate Action
- Navigate to (3, 14) to Reset.