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
- P(4, 2). M(1, 2) [Assumed Pinned].
- **Mystery**: Murkrow sprite not visible at (1, 2) in screenshot.
  - Possibility A: Glitch/Flicker.
  - Possibility B: Mirror Horizontal (M is at 29, 2).
  - Possibility C: M blocked earlier.
- **Action**: Move to (25, 2) to check if M appears at (22, 2).

## Plan: "Col 25-22 Ratchet"
1. **Sync Gap=3**: P(4, 2), M(1, 2). [Done]
2. **Position**: P(25, 2), M(22, 2).
   - *Check*: Look for M at (22, 2).
3. **Ratchet**: P(25, 15), M(22, 1).
4. **Pull**: P(25, 3), M(22, 13).
5. **Drop**: P(25, 2), M(22, 14).

## Immediate Action
- Navigate to (25, 2).