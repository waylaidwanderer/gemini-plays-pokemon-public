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
- **Result:** FAILED. (20, 6) is CLOSED.

## New Goal: Test Switch 1
- **Hypothesis:** Switch 1 might control (20, 6).
- **Plan:**
    1. Turn Switch 1 ON (Current State: OFF).
    2. Check (20, 6).
    3. If Closed, try combinations with S2/S3.

## Pathfinding
- (20, 6) is the key chokepoint.
- Emergency Switch is at (20, 11).
- Door at (22, 10) is likely the Director's room.