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
- P(16, 2). M(Unknown).
- **Observation**: Murkrow NOT at (17, 2) (Disproves Mirror X from 8).
- **Status**: Murkrow is missing or off-screen.
- **Action**: Search pattern. Check Left Corner (1, 2), then Right Corner.

## Search & Solve Plan
1. **Search Left**:
   - Go to (1, 2).
   - Check if M is pinned at (1, 2).
2. **Search Right**:
   - If not at (1, 2), go to (27, 2).
3. **Re-Evaluate**:
   - Once M is found, deduce X-axis logic (Mimic vs Mirror) and Offset.
   - Execute "Ratchet" strategy based on confirmed location.

## Immediate Action
- Move Left to (1, 2).