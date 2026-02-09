# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Scrape Solution
- **Goal**: Place Murkrow at (22, 14) for interaction.
- **Method**: X-Axis Scrape on Computer at (21, 10).
- **Plan**:
  1. `Up` x2 -> P(22, 11), M(22, 10).
  2. `Left` -> P(21, 11). M(22, 10) (Blocked by Computer 21, 10).
  3. `Down` x4 -> P(21, 15), M(22, 14).
  4. `Right` -> P(22, 15). M(22, 14) (Blocked by Door).
  5. Interact Up.
- **Action**: Execute Step 1 (Up x2).