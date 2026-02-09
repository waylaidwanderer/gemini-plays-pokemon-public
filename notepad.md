# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision Rules**:
  - P Blocked: Murkrow Stays (High Confidence).
  - M Blocked: Murkrow Stays (Verified).
  - Stack/Swap: To be tested.

## Current State
- **Player**: (22, 14).
- **Murkrow**: (22, 13) (Visual Confirmation).
- **Door**: (23, 14).
- **Status**: Trapped. Needs to move Up to escape.

## Strategy: The Slide Test (Step 1)
- **Goal**: Move to (21, 13) and verify Murkrow position.
- **Current**: P(21, 11). M presumed at (22, 10).
- **Hypothesis**: After `Down` x2, M should be at (22, 12).
- **Plan**:
  1. `Down` x2 -> P(21, 13).
  2. Verify M at (22, 12).
  3. If verified, proceed with "Bump Test".
- **Action**: Execute `Down` x2.