# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "ROW 12 TRAVERSE"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Traverse Row 12 to bypass Machine/Statues, then Ratchet on Col 22.

## Step 1: Reach (1, 16) & Invert Y [IN PROGRESS]
- **Action**:
  - Left to (3, 1). Down to (3, 6). Left to (1, 6). Down to (1, 16).
  - *Avoids*: Warp (1, 4), Wall (1, 5).
  - *Result*: P(1, 16), M(1, 1).

## Step 2: Position for Row 12
- **Action**:
  - Up to (1, 12). M Down to (1, 5).
  - *State*: P(1, 12), M(1, 5).

## Step 3: Traverse & Dodge Jed
- **Action**:
  - Right to (17, 12). M Right to (17, 5).
  - Down to (17, 13). M Up to (17, 4).
  - Right to (19, 13). M Right to (19, 4).
  - Up to (19, 12). M Down to (19, 5).
  - Right to (22, 12). M Right to (22, 5).
  - *State*: P(22, 12), M(22, 5).

## Step 4: Ratchet & Solve
- **Action**:
  - Push UP (22, 11) -> (22, 10 Wall) x7.
    - P at (22, 11). M moves Down (5 -> 6 -> ... -> 13).
  - *State*: P(22, 11), M(22, 13).
  - Down 1 to (22, 12). M blocked/pushed.
  - Interact Down.