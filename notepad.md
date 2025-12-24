# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (14, 14).
- **Goal:** Reach B1 at (11, 7) to solve it.
- **Puzzle State:**
  - **B1:** At (11, 7). Target: Pit (11, 2).
  - **B2:** At (5, 6). Ready for final push.
  - **B3:** Solved (Gone).
  - **B4:** At (17, 7). Target: Pit (12, 13).

## Plan: Solve Boulder 1 (B1)
1. **Navigate:** Go West to (13, 14) -> North to (13, 12) -> West to (12, 12) -> North to (12, 8) -> Left to (11, 8).
2. **Push Up:** Push B1 from (11, 7) to (11, 5).
3. **Flank:** Go Left to (10, 5) -> Up to (10, 1) -> Right to (11, 1).
4. **Push Down:** Push B1 into Pit (11, 2).

## Plan: Finish Boulder 2 (B2)
1. **Navigate:** Go North to Row 1 -> West to (6, 6).
2. **Push:** Left to (4, 6) -> Down to Pit (4, 7).

## Plan: Solve Boulder 4 (B4)
1. **Navigate:** To (17, 7).
2. **Push:** Left to (12, 7) -> Up to (12, 2) -> Left to Pit (11, 2)? No, B1 goes there.
   - Wait, B4 target is Pit (12, 13).
   - Push Left to (16, 7). Then maneuver to push Down to (16, 12) -> Left into Pit (12, 13).

## Immediate Action
- Navigate to (11, 8).