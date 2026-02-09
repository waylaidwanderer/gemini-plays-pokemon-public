# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The "Shimmy" Climb
- **Problem**: Pushing Up fails (Collision/No-Push). Talking in place failed (Unknown reason). Leading Down requires interaction I haven't mastered.
- **Solution**: "Pull" the Murkrow North using lateral movement.
- **Algorithm**: `Left` -> `Up` -> `Right`.
  - `Left`: Me(21,13), Bird(21,12). (Lateral Mimicry).
  - `Up`: Me(21,12), Bird(21,11). (Pulling works).
  - `Right`: Me(22,12), Bird(22,11). (Pulling works).
- **Result**: We shift Up by 1 tile. Repeat until pinned against Grunt at (22,9). Then Talk.
- **Action**: Execute Shimmy Step 1.