# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "LEFT WALL SYNC & NORTH RATCHET"
**Goal**: Open Boss Door at (22, 14) from (22, 13).
**Strategy**: Sync X Left, Invert Y, Traverse North, Ratchet M to (22, 12).

## Step 1: Sync X at (1, 2)
- **Current**: P(27, 2), M(7, 2).
- **Action**: Move Left to (1, 2).
  - *Note*: Passes Statue Alarm at (6, 1).
  - *State*: P(1, 2), M(1, 2).

## Step 2: Reach (1, 16) (Detour)
- **Route**:
  - Down to (1, 4). (Avoid Wall at 1, 5).
  - Right to (3, 4).
  - Down to (3, 12). (Avoid Stairs at 3, 14).
  - Left to (1, 12).
  - Down to (1, 16).
  - *State*: P(1, 16), M(1, 16).

## Step 3: Invert Y
- **Action**: Up to (1, 1).
  - P(1, 1). M(1, 16) (Mirrored).

## Step 4: Traverse & Ratchet
- **Action**:
  - Right to (22, 1). M to (22, 16).
  - Down to (22, 11). M to (22, 6).
  - Push UP (22, 10). M Down to (22, 12/13).
  - Solve.