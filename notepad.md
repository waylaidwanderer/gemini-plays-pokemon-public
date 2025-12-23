# Goldenrod Underground Switch Puzzle

## Switch Mechanics Log
- **Switch 1 (16, 1):** OFF.
    - Potential Control: (20, 6) or (12, 12).
- **Switch 2 (10, 1):** OFF.
    - Effect: Appears to be a modifier or "Master" switch.
    - Observation: Turning S2 OFF closed (6, 8) and (12, 8) automatically.
- **Switch 3 (2, 1):** OFF.
    - Effect: Controls South-West shutters.
    - Dependency: Behavior changes based on Switch 2.

## Current State: ALL OFF (S1=0, S2=0, S3=0)
- **Goal:** Check if this "Reset" state opens the main shutter at (20, 6).
- **Next Step:** Walk into (20, 6).
    - If Open: Proceed to Director.
    - If Closed: The solution is likely a specific combination, not just "All Off".
    - Next Hypothesis to test: S1 ON, S2 OFF, S3 OFF (since S2/S3 interaction is known, maybe S1 needs to be active).

## Pathfinding
- (20, 6) is the key chokepoint.
- Emergency Switch is at (20, 11).
- Door at (22, 10) is likely the Director's room.