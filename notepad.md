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
- **Verification:**
  - I am standing at (10, 6), so (10, 6) is **OPEN**.
  - S2 must be **OFF** (since S1 is ON and S1+S2(ON) closes (10, 6)).
  - Previous observation: S1(ON)+S2(OFF) opens (12, 8).
  - **Conclusion:** Path to Emergency Switch should be open.

## Dead End Confirmed
- Reached (17, 8) but hit a wall at x=18.
- The path (10, 6) -> (12, 8) leads to the Middle Section (Burglar area), but NOT the East Section (Director/Emergency Switch).
- **Conclusion:** I MUST open the shutter at (20, 6) to access the East Section.

## New Goal: Open Shutter (20, 6)
- **Current State:** S1=ON, S2=OFF, S3=OFF. (20, 6) is CLOSED.
- **Untested Combinations:**
    1. S1=ON, S2=OFF, S3=ON.
    2. S1=OFF, S2=OFF, S3=ON.
- **Plan:**
    1. Return to Switch 3.
    2. Turn Switch 3 ON (Testing Combination 1).
    3. Check (20, 6).
    4. If Closed, Turn Switch 1 OFF (Testing Combination 2).