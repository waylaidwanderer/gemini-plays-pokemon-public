# Murkrow Puzzle: Verified Overlap Strategy

## Current State
- P(21, 1). M(20, 1) [Calculated].
- **Action**: Syncing X/Y at Top-Left Corner (1, 1).

## Execution Plan
1. **Sync X/Y**:
   - Move Left to (1, 1).
   - M moves Left. Hits Left Wall at (0, 1). Stops at (1, 1).
   - **Result**: P(1, 1), M(1, 1). [Overlapped].
2. **Transport to Bottom**:
   - Move Down to (1, 15).
   - Path Col 1 has Warp Trap at (1, 4)?
   - **CRITICAL CHECK**: (1, 4) is marked "Warp Trap".
   - If I step on (1, 4), I warp.
   - **Alternative**: Use Col 2.
     - Move Right to (2, 1).
     - Move Down to (2, 15).
     - (2, 4) is Passive Grunt. (2, 10/11/12) are Traps (Battle).
     - Tank the battles.
3. **Transport to Door**:
   - At (2, 15), Move Right to (22, 15).
   - Move Up to (22, 13).
   - Interact.

## Immediate Action
- Move Left to (1, 1). Then Right to (2, 1). Then Down.