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

## Current Goal: Test S1=OFF, S2=ON, S3=OFF
- **Theory:**
  - S1=ON closes (10, 6), blocking the north entrance.
  - S2=ON opens (10, 6) and (12, 8).
  - S3=OFF opens (10, 6) and (2, 6).
  - Therefore, S1=OFF, S2=ON, S3=OFF should have BOTH (10, 6) and (12, 8) open, creating a path through the middle.
- **Plan:**
  1. Turn S2 ON (Done).
  2. Turn S1 OFF (Done).
  3. Enter (10, 6) -> (12, 8) -> Emergency Switch (Moving now).

## Pathfinding
- (20, 6) is the key chokepoint.
- Emergency Switch is at (20, 11).
- Door at (22, 10) is likely the Director's room.