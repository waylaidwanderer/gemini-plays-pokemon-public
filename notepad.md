# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics
- **Mimicry**: Murkrow COPIES input.
- **Switches**: B1F Statues/Computers *should* open B2F shutters.
  - West Statue (6, 0): No reaction.
  - East Computer (24, 0): No reaction.
- **Hypothesis**: Defeating Grunts near the switches activates them or provides the key.

## Current State
- Map: B2F (3_51).
- Player: (3, 2).
- Status: Navigating South on West Side.
- Objective: Check passability of Row 11 (Shutter/Wall).
- Constraint: AVOID WARP TILE AT (3, 6).
- Route:
  1. Move to (4, 2) -> (4, 10). (Bypassing (3, 6)).
  2. Check (3, 11) / (4, 11) for passage.
  3. If passable, reach Stairs at (3, 14).
  4. If blocked, return to B1F and check Gate at (3, 8).

## Murkrow Status
- Reset to (7, 2) on B2F (assumed).