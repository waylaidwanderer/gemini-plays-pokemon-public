# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision Rules**:
  - P Blocked: Murkrow Stays.
  - Chase Blocked: P cannot move into M's tile even if M moves away.

## Current State
- Player: (20, 14).
- Murkrow: Unknown (Not visible at 20,13 / 21,13).
- Status: Text Box Open (Grunt).

## Strategy: Recovery
- **Goal**: Close text and locate Murkrow.
- **Execution**:
  1. `B` -> Close Text.
  2. `Up` -> Move to (20, 13).
  3. Verify Murkrow position.