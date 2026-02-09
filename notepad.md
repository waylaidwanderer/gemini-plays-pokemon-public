# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Under Test)
- **Mimicry**: Confirmed.
- **Collision**:
  - **Test**: If P is blocked by an NPC (Grunt), does M still move into an open tile?
  - **Current Theory**: M *should* move.

## Current State
- **Player**: (21, 13).
- **Murkrow**: (21, 12).
- **Grunt**: (21, 14) (South of Player).

## Strategy: The Lateral Slide Test
- **Goal**: Verify mechanic.
- **Plan**:
  1. `Left` -> P(20, 13), M(20, 12).
  2. `Down` -> P(20, 14), M(20, 13).
  3. `Right` -> P Blocked by Grunt (21, 14).
     - **Observation**: Does M move to (21, 13) (Empty)?
     - **Success**: M ends at (21, 13).
     - **Failure**: M stays at (20, 13).
- **Action**: Execute `Left`, `Down`, `Right`.