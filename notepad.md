# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Grunt Slide
- **Goal**: Slide M to (22, 13) using the Grunt at (21, 14) to block Player.
- **Current**: P(20, 14), M(20, 13).
- **Plan**:
  1. `Right` -> P Blocked at (20, 14). M moves to (21, 13).
  2. `Right` -> P Blocked at (20, 14). M moves to (22, 13).
  3. `Down` -> P(20, 15). M(22, 14).
  4. `Right` x2 -> P(22, 15). M(22, 14) (Blocked by Door).
  5. Interact Up.
- **Action**: Execute Step 1 (Right).