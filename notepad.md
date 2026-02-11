# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "NORTH APPROACH"
**Goal**: Open Boss Door at (22, 14) from (22, 13).
**Strategy**: Swap Y (P Top, M Bottom), Traverse, Ratchet M to (22, 12).

## Step 1: Reach (1, 1) (Detour)
- **Problem**: Warp/Pushback at (1, 4) -> (1, 6).
- **Action**: Detour via Col 3.
  - Right to (3, 6). Up to (3, 2).
  - Left to (1, 2). Up to (1, 1).
  - *State*: P(1, 1), M(1, 16).

## Step 2: Traverse & Align
- **Action**:
  - Right to (22, 1). M Right to (22, 16).
  - Down to (22, 13). M Up to (22, 4).
  - *State*: P(22, 13), M(22, 4).

## Step 3: Ratchet & Solve
- **Action**:
  - Push UP against Door (22, 14) x8.
    - P blocked. M moves Down (4 -> 12).
  - *State*: P(22, 13), M(22, 12).
  - Interact Down (Door).