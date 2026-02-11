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
- P(22, 13), M(22, 12).
- **Observation**: Trapped in South-East pocket. M blocks North. Walls block East/South.
- **Solution**: "Scientist Desync".
  - Use Scientist at (18, 12) to block Murkrow's Left movement.
  - P moves Left to (17, 13). M blocked at (19, 12).
  - P moves Up to (17, 12). M moves Down to (19, 13).
  - P escapes North.

## Execution Plan
1. **Desync**:
   - Left x5 to (17, 13).
   - Up x1 to (17, 12).
2. **Reset**:
   - Move to Exit (27, 2).
   - Re-enter map to reset Murkrow.
3. **Execute Ratchet**:
   - Retry "Col 26 Ratchet" from clean slate.

## Immediate Action
- Move Left x5, Up x1.