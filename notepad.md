# Team Rocket HQ - B2F Strategy

## Active Goal: The Switch Hunt
**Objective**: Reach and toggle the switch at (19, 11).
**Hypothesis**: This switch might open the Boss Door or clear obstacles for Murkrow.

## Current State
- **Player**: (25, 2) (Warp Landing).
- **Murkrow**: Position Unverified (Assume Reset to 7, 2 if I left map).

## Plan
1. **Navigate to Switch**: Use BFS to reach (19, 12) (South of Switch).
2. **Interact**: Face Up and press A.
3. **Verify**: Check for "Switch turned ON" message or map changes.
4. **Contingency**: If switch does nothing, reset Murkrow via Souvenir Shop exit (27, 2) and retry puzzle from scratch.

## Mechanics Log
- **Murkrow**: Mirrors Y, Parallels X.
- **Switch**: Located at (19, 11). Status: OFF.
- **Exit**: (27, 2) leads to Souvenir Shop.