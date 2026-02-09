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

## Strategy: The Side-Slide Test
- **Goal**: Verify if Murkrow moves when Player is blocked laterally.
- **Current**: P(21, 13), M(21, 12).
- **Setup**:
  1. `Right` -> P(22, 13), M(22, 12).
  2. `Down` -> P(22, 14), M(22, 13).
- **Test**:
  3. `Left` -> P blocked by Grunt (21, 14). M targets (21, 13) [Open].
  4. If M moves to (21, 13), we can slide!
- **Action**: Execute `Right`, `Down`.