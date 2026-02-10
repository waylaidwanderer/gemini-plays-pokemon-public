# Team Rocket HQ - Murkrow Puzzle

## Active Attempt: "The Pin & Flank"
**Current State**: P(28, 12). M(22, 11) (Hypothesized).
**Goal**: Pin M at Door (22, 14) and converge X.

## The Plan
1. **Pin Y (Door)**:
   - Move Up 3 to P(28, 9).
   - M moves Down 3. Expectation: M(22, 11) -> M(22, 14).
   - *Note*: If (22, 14) is a wall to M, M stops at (22, 13).
2. **Converge X**:
   - Move Left 6 to P(22, 9).
   - **Hypothesis**: M is pinned West by Wall(21, 14) if at (22, 14).
   - If M moves Left (was at 13), M ends at (16, 13).
3. **Verify**:
   - Look Down at (22, 9).
   - If M is at (22, 14), **SUCCESS**. Approach and Interact.
   - If M is missing (moved West), we must re-sync X using the East wall.