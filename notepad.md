# Team Rocket HQ - Murkrow Puzzle

## STATUS: ENTERING HIDEOUT
**Goal**: Open Boss Door at (22, 14) from (22, 13).
**Current**: In Shop (2_7). Standing on Stairs (7, 5).

## Step 1: Re-enter B2F (Map 3_49)
- **Action**:
  - Interact/Move Down to enter B1F (3_48).
  - Navigate to B2F Entrance -> B2F (3_49) at (7, 2).

## Step 2: Execute "NORTH APPROACH REDUX"
- **Strategy**: Sync X Left, Invert Y on Col 1 (Detour), Swap Y, Ratchet M to (22, 12).
- **Route**:
  - From (7, 2), Left to (3, 2).
  - Down to (3, 12) (Avoid Warp 1,4 & Wall 1,5).
  - Left to (1, 12).
  - Down to (1, 16).
  - *Target State*: P(1, 16), M(1, 1).

## Step 3: Swap Y (P Top, M Bottom)
- **Action**:
  - Up to (1, 1).
    - P moves to (1, 1).
    - M moves Down to (1, 16).
  - *State*: P(1, 1), M(1, 16).

## Step 4: Traverse & Align
- **Action**:
  - Right to (22, 1). M Right to (22, 16).
  - Down to (22, 13). M Up to (22, 4).
  - *State*: P(22, 13), M(22, 4).

## Step 5: Ratchet & Solve
- **Action**:
  - Push UP against Door (22, 14) x8.
    - P blocked. M moves Down (4 -> 12).
  - *State*: P(22, 13), M(22, 12).
  - Interact Down.