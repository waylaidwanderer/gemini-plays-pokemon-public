# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "COL 26 RATCHET & DOOR SYNC"
**Goal**: P(22, 2), M(22, 14).
**Logic**: Ratchet at Col 26 to align Y, then position for Door Drop.

## The Plan
1. **Navigate to Ratchet Point**:
   - Start: P(19, 12), M(19, 1).
   - **Step 1**: Up to (19, 7). M -> (19, 6).
   - **Step 2**: Right to (26, 7). M -> (26, 6).
2. **Execute Ratchet**:
   - **Step 3**: Down to (26, 15). 
     - M moves Up 8: (26, 6) -> (26, -2) -> Stuck at (26, 1).
   - *State*: P(26, 15), M(26, 1).
3. **Align for Drop**:
   - **Step 4**: Up to (26, 13). M -> (26, 3).
   - **Step 5**: Left to (22, 13). M -> (22, 3).
   - **Step 6**: Up to (22, 3). M -> (22, 13).
     - *State*: P(22, 3), M(22, 13).
4. **Trigger Door**:
   - **Step 7**: Up to (22, 2). M -> (22, 14).
   - *Result*: M lands on Boss Door. Door opens?
5. **Enter**:
   - Walk to door.

## Current State
- P(3, 14) -> Moving to (7, 2).
- **Goal**: Verify Murkrow spawn at (7, 1) or (19, 1).

## Execution Plan
1. **Navigate**: Go Up to Row 2, then Right to Col 7.
2. **Verify**: Spot Murkrow at (7, 1).
3. **Test**:
   - Move **Right** to (8, 2).
   - **Mirror X**: M moves Left to (6, 1)? Or Right?
     - If P(7->8) is Right, Mirror M(7->6) is Left.
   - **Mimic X**: M moves Right to (8, 1).

## Immediate Action
- Move to (7, 2).