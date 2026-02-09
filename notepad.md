# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics
- **Mimicry**: Murkrow COPIES input.
- **Switches**: B1F Statues/Computers *should* open B2F shutters.
- **Hypothesis**: Defeating Grunts near the switches activates them or provides the key.

## Current State
- Map: B1F (3_50).
- Player: (6, 13).
- Status: Solving Murkrow Puzzle (Phase 1 - Execution).
- Action: Moving Player to (4, 10) manually to desync Murkrow.
- Sequence: Right (to Col 4), Down x8 (to Row 10).
- Expected State: Player (4, 10), Murkrow (7, 8).
- Logic: Murkrow hits wall at (7, 9), gets stuck at Y=8. Player continues to Y=10.
- Next: Move East to align Murkrow with Fake Wall at (10, 9).