# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "NORTH RATCHET (STATUE DODGE VARIANT)"
**Goal**: Open Boss Door at (22, 14) from North.
**Strategy**: Sync X Left, Invert Y on Col 4, Statue Dodge to Resync X Right, Loop North, Ratchet.

## Step 1: Sync X (Left Wall) [DONE]
- P(1, 2), M(1, 1).

## Step 2: Invert Y (Col 4) [IN PROGRESS]
- **Current**: P(1, 2).
- **Action**:
  - Right to (4, 2). M to (4, 1).
  - Down to (4, 16).
    - M blocked at (4, 1) (Top Wall).
  - *Expect*: Battles on Col 4.
  - *Target State*: P(4, 16), M(4, 1).

## Step 3: Statue Dodge
- **Action**:
  - Right to (6, 16).
    - M Right to (5, 1) -> Blocked by Statue (6, 1).
  - *State*: P(6, 16), M(5, 1).

## Step 4: Resync X (Right Wall)
- **Action**:
  - Right to (29, 16).
    - M Right to (29, 1). Sync restored.
  - *State*: P(29, 16), M(29, 1).

## Step 5: Loop to North & Ratchet
- **Action**:
  - Up to (29, 2). M Down to (29, 16).
  - Left to (22, 2). M Left to (22, 16).
  - Down to (22, 11). M Up to (22, 7).
  - Push UP (22, 10) x6. M Down (7 -> 13).
  - Down to (22, 12). Collision Squeeze.
  - Interact Down.