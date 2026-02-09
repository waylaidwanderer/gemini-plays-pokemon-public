# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Left Hook
- **Goal**: P(22, 15), M(22, 14).
- **Current**: P(20, 14), M(20, 13).
- **Hypothesis**: Murkrow moves even if Player is blocked.
- **Plan**:
  1. `Right` (Player Blocked). Check if M moves to (21, 13).
  2. `Right` (Player Blocked). Check if M moves to (22, 13).
  3. `Down` -> P(20, 15), M(22, 14).
  4. `Right` x2 -> P(22, 15).
  5. Face Up, Interact.
- **Action**: Execute Step 1 (Right).