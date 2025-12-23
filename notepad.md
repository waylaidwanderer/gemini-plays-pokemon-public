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

## Test Result: S1=ON, S2=OFF, S3=OFF
- **Result:** (20, 6) CLOSED. (12, 8) OPEN (Observed).
- **Insight:** Switch 1 affects (12, 8) when S2 is OFF.

- **Switch 2 (10, 1):** Turned ON.
    - State: ON.
    - Context: S1=ON, S3=OFF.

## Test Result: S1=ON, S2=ON, S3=OFF
- **Result:** (20, 6) CLOSED.

- **Switch 1 (16, 1):** Turned ON.
    - State: ON.
    - Context: S2=ON, S3=OFF.

## Current Goal: Retest S1=ON, S2=OFF, S3=OFF
- **Analysis:**
  - S2=OFF opens Outer (10, 6).
  - S1=ON opens Inner (12, 8).
  - If both are true simultaneously, the middle path is open.
- **Plan:**
  1. Turn S1 ON (Done).
  2. Turn S2 OFF (Navigating now).
  3. Enter (10, 6) -> (12, 8) -> Emergency Switch.

## Pathfinding
- (20, 6) is the key chokepoint.
- Emergency Switch is at (20, 11).
- Door at (22, 10) is likely the Director's room.