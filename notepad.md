# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision**: 
  - If Player is blocked, Murkrow STAYS.
  - If Murkrow is blocked, Murkrow STAYS.
  - Murkrow and Player cannot overlap.

## Strategy: Interaction Check (Trap State)
- **Status**: Trapped at (22, 14) with M at (22, 13).
- **Plan**:
  1. `B` (Close Grunt text).
  2. `Up` (Face Murkrow).
  3. `A` (Talk to Murkrow).
  4. `Right` (Face Door).
  5. `A` (Check Door).
- **Contingency**: If this fails, use `Left` (Bump Grunt) to escape.
- **Action**: Execute Sequence.