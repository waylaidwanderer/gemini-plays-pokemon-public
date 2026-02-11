# Murkrow Solution: The Silver Lining

## Current Status
- P(22, 13).
- Murkrow at (22, 12) [Verified].
- Rival (Silver) at (21, 13) [Verified].
- Grunt at (21, 14).
- Wall at (23, 13) and (22, 15).

## Problem
- Silver blocks (21, 13), preventing M from using that tile for Y-Sync.
- Grunt blocks (21, 14).
- To align P(23, 14) and M(22, 14), we need clear pathing.

## Plan
1. **Interact with Silver**:
   - Press **Left** (Face Rival).
   - Press **A**.
   - **Expectation**: Battle or Cutscene where he leaves.
2. **Post-Interaction**:
   - If (21, 13) clears, execute **Left Shift Y-Sync**.
   - Move Left to (21, 13).
   - Bump Grunt (Down).
   - Align X/Y.