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

## Strategy: The Overtake
- **Goal**: Place M South of P (P at 22, 13, M at 22, 14).
- **Hypothesis**: Moving P into M's tile while M is blocked (by Grunt at 22, 9) will cause M to stay behind, flipping the Y-axis relative position.
- **Plan**:
  1. Escape: `B`, `Up` -> P(22, 13), M(22, 12).
  2. Setup: `Up` x2 -> P(22, 11), M(22, 10).
  3. Overtake: `Up` -> P(22, 10). M(22, 9) Blocked -> M(22, 11)?
  4. Pull: `Down` x3 -> P(22, 13), M(22, 14).
- **Action**: Escape Trap (`B`, `Up`).