# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "LEFT-SIDE DOOR RATCHET"
**Goal**: Open Boss Door at (22, 14).
**Target State**: P(22, 15), M(22, 13).

## Step 1: Sync X (Col 1) [COMPLETED]
- P synced at X=1.

## Step 2: Invert Y (Battle Path) [IN PROGRESS]
- **Current**: P(3, 12). M(3, 1) (Estimated).
- **Action**: Move Left to (1, 12), then Down to (1, 16).
  - *Expect*: Battles.
  - *Result*: P(1, 16), M(1, 1).

## Step 3: The "Statue Dodge" Traverse
1. **Pass Warp**: Right to (5, 16). P(5, 16), M(5, 1).
2. **Desync on Statue**: Right to (6, 16).
   - P moves to (6, 16).
   - M blocked by Statue (6, 1). M stays (5, 1).
   - *State*: P(6, 16), M(5, 1).
3. **Shift Lanes**: Up to (6, 15).
   - P(6, 15). M Down to (5, 2).
   - *State*: P(6, 15), M(5, 2).
4. **Cross Room**: Right to (29, 15).
   - P moves to Wall (29, 15).
   - M moves to Wall (29, 2). (Resyncs X).
   - *State*: P(29, 15), M(29, 2).
5. **Position**: Left to (22, 15). P(22, 15), M(22, 2).

## Step 4: The Door Ratchet
- Push UP against Boss Door (22, 14) x11.
- M moves Down to (22, 13).
- Interact (A).