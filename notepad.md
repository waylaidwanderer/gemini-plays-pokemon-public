# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "NORTH APPROACH"
**Goal**: Open Boss Door at (22, 14) from (22, 13).
**Strategy**: Swap Y (P Top, M Bottom), Traverse, Ratchet M to (22, 12).

## Step 1: Reach (1, 16) (Current)
- **Action**: Detour Col 3 to avoid wall at (1, 5) and Grunt at (2, 4).
  - Up to (1, 3). Right to (3, 3).
  - Down to (3, 12). Left to (1, 12).
  - Down to (1, 16).
  - *State*: P(1, 16), M(1, 1).

## Step 2: Swap Y (P Top, M Bottom)
- **Action**:
  - Up to (1, 1).
    - P moves to (1, 1).
    - M moves Down to (1, 16).
  - *State*: P(1, 1), M(1, 16).

## Step 3: Traverse & Align
- **Action**:
  - Right to (22, 1). M Right to (22, 16).
  - Down to (22, 13). M Up to (22, 4).
  - *State*: P(22, 13), M(22, 4).

## Step 4: Ratchet & Solve
- **Action**:
  - Push UP against Door (22, 14) x8.
    - P blocked. M moves Down (4 -> 12).
  - *State*: P(22, 13), M(22, 12).
  - Interact Down (Door) or Left (Murkrow).