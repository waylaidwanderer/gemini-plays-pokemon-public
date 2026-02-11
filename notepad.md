# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "JED BLOCK & SWITCH RATCHET"
**Goal**: Open Boss Door at (22, 14).
**Target State**: P(22, 13), M(22, 12).

## Step 1: Jed Block (Desync X)
- **Current**: P(21, 2), M(20, 15).
- **Action**:
  - Left 1 to (20, 2). M to (19, 15).
  - Down 3 to (20, 5). M Up to (19, 12).
  - Left 3 to (17, 5).
    - M Left 3 to (16, 12).
    - *Correction*: Jed is at (18, 12). M blocked at (19, 12)?
    - Check Jed: Map says (18, 12) `TYPE_3fe2` with Marker `Scientist Jed`.
    - So M blocked at (19, 12) moving Left.
  - *State*: P(17, 5), M(19, 12).

## Step 2: Switch Ratchet (Desync Y)
- **Action**:
  - Down 8 to (17, 13).
    - M Up 8. Blocked at (19, 9) by Wall (19, 8).
  - Right 2 to (19, 13). M Right 2 to (21, 9).
  - Up 1 to (19, 12). M Down 1 to (21, 10).
  - Push UP (19, 11) x3.
    - P blocked. M Down (10 -> 13).
  - *State*: P(19, 12), M(21, 13).

## Step 3: Solve
- **Action**:
  - Down 1 to (19, 13). M Up 1 to (21, 12).
  - Right to (28, 13). M to (28, 12). (Sync X).
  - Left to (22, 13). M to (22, 12).
  - Interact Up.