# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Murkrow Master Plan
- **Goal**: P(22, 13), M(22, 14).
- **Current**: P(20, 14), M(20, 13).
- **Phase 1: Align**
  1. `Up` -> P(20, 13), M(20, 12).
  2. `Right` x2 -> P(22, 13), M(22, 12).
- **Phase 2: X-Scrape (Computer)**
  3. `Up` x2 -> P(22, 11), M(22, 10).
  4. `Left` -> P(21, 11). M Blocked by Computer (21, 10). Stays (22, 10).
- **Phase 3: Y-Slide (Grunt)**
  5. `Down` x2 -> P(21, 13), M(22, 12).
  6. `Down` (P Blocked by Grunt) -> P(21, 13). M moves (22, 13).
  7. `Down` (P Blocked by Grunt) -> P(21, 13). M moves (22, 14).
- **Phase 4: Finish**
  8. `Right` -> P(22, 13). M Blocked by Door. Stays (22, 14).
  9. Interact Down.
- **Action**: Execute Phase 1 (Up, Right, Right).