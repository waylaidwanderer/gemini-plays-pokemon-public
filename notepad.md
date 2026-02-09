# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Right-Column Slide
- **Goal**: Place M at (23, 13) or (22, 14).
- **Current**: P(22, 14), M(22, 13).
- **Sequence**:
  1. `A` (Interact Up).
  2. `Up` x3 -> P(22, 11), M(22, 10).
  3. `Left` -> P(21, 11). M(22, 10) (Blocked).
  4. `Right` -> P(22, 11). M(23, 10).
  5. `Down` x3 -> P(22, 14). M(23, 13).
- **Action**: Execute Sequence.