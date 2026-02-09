# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Validated Slide
- **Goal**: Place M at (22, 14) using Grunt (21, 14) and Computer (21, 10).
- **Current**: P(22, 13), M(22, 12).
- **Phase 1: Setup**
  1. `Left` -> P(21, 13), M(21, 12).
  2. `Up` -> P(21, 12), M(21, 11).
  3. `Right` -> P(22, 12), M(22, 11).
  4. `Up` -> P(22, 11), M(22, 10).
- **Phase 2: Desync**
  5. `Left` -> P(21, 11). M Blocked by Computer (21, 10). M Stays (22, 10).
- **Phase 3: Slide**
  6. `Down` x4 -> M moves to (22, 14). P stops at (21, 13) due to Grunt.
  7. `Right` -> P(22, 13). M Stays (22, 14).
  8. Face Down, Interact.
- **Action**: Execute Phase 1 (Left, Up, Right, Up).