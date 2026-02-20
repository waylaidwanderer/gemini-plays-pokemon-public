### Objectives
- [ ] Get Card Key from Director (Current Loc: 3_53, (18,30))
- [ ] Return to Radio Tower 3F
- [ ] Open Shutters and Defeat Team Rocket

### Warehouse Puzzle Solution
- **Goal:** Reach Silver at (4, 8) and/or open path to Director.
- **Hint:** "Change the order of switching."
- **Current Strategy:** Warehouse Switch Puzzle.
  - Switches: Sw1 (16,1), Sw2 (10,1), Sw3 (2,1).
  - Gates: G1 (2,6), G2 (10,6), G3 (16,6).
  - Traps: (10,5), (2,4)?, (10,4)?, others?
- **Current State:** 1-1-1 (Need to verify).
- **Plan:**
  1. Test Trap at (2, 4).
  2. If safe, go to Silver via Gate 1.
  3. If trap, toggle switches to change state (Target: 1-0-1 or 0-1-1).

### Key Locations
- Director: Map 3_53 (18, 29) - Unresponsive.
- Silver: Map 3_54 (4, 8).
- Grunt (Hint): Map 3_54 (3, 2).
- Gate 1 (2, 6) is CLOSED in state 1-1-0 (Sw3 OFF).
- Plan: Toggle Switch 1 (16, 1) to OFF.
- New State Target: 0-1-0.
- Hypothesis: Maybe Switch 1 controls the master lock or something.
- Path: Traverse from Left (Sw3) to Right (Sw1).
- Risk: Crossing the middle column (x=10) traps.
- Known Traps: (10, 5) [Warp], (10, 2) [Suspected].
- Strategy: Try Row 3 or 4.
- Current State: 0-1-0 (Sw1 OFF, Sw2 ON, Sw3 OFF).
- Action: Toggled Sw1 OFF.
- Checking gate states.
- Risk: Gate 3 (16, 6) might be CLOSED.
- Gate 1 (2, 6) status unknown.
- Goal: Open Gate 1 to reach Silver.
- If Gate 3 Closed and Gate 1 Closed: Must revert Sw1 to ON to escape.
- Next Test: If 0-1-0 fails, try 0-0-0 (Turn Sw2 OFF). But need to reach Sw2 first.