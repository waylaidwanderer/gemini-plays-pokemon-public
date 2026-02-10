# Team Rocket HQ - Murkrow Puzzle

## EXECUTION: "The Pinned Murkrow"
Target: M(22, 14).

## Current Status (Turn 36441)
- **Player**: (22, 16).
- **Murkrow**: (22, 2) (Estimated).

## Step 1: Inject M to Door
- **Action**: Pump Up 13 times.
- **Logic**:
  - P is blocked North by Statue (22, 15).
  - M moves Down (Mirror).
  - M(22, 2) -> ... -> M(22, 14).
  - If (22, 14) is walkable, M stays there (Pinned S, E, W).
  - If (22, 14) is blocked, M stops at (22, 13).

## Step 2: Flank to East
- **Action**: Right 4 to (26, 16).
- **Logic**:
  - If M is at (22, 14), it is blocked East by Wall (23, 14).
  - M stays at (22, 14).
  - P moves to (26, 16).

## Step 3: Observe
- Check M position.
- If M at 14: Proceed with Flank (Up 3, Left 4).
- If M at 13: Re-evaluate.