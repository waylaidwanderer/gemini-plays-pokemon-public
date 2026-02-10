# Team Rocket HQ - Murkrow Puzzle

## Active Attempt: "Locate & Align"
**Current State**: P(26, 12). M(20, 11) (Hypothesized).
**Goal**: Bring Murkrow into view at Col 22.

## The Plan
1. **Search East**:
   - Move Right 2 -> P(28, 12).
   - If M is at (20, 11), M moves Right 2 -> M(22, 11).
   - **CHECK**: Is M visible at (22, 11)?
2. **If Visible (Success)**:
   - Calculate path to pin M at (22, 14).
   - P(28, 12) -> Up 3 -> P(28, 9). M(22, 11) -> Down 3 -> M(22, 14).
   - P(28, 9) -> Left 6 -> P(22, 9). M(22, 14) -> Left (Blocked) -> M(22, 14).
   - Approach & Interact.
3. **If Not Visible**:
   - M is likely at Row 2 or further West.
   - Initiate Reset Protocol.