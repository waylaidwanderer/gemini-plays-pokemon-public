# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: Interaction Sweep
- **Goal**: Trigger Door or Murkrow.
- **Hypothesis 1 (Visuals)**: P(21, 14), M(22, 13). `Right` -> P(22, 14). M Stuck.
  - Action: Face Right (Door) -> Interact. Face Up (M) -> Interact.
- **Hypothesis 2 (Collision)**: P(22, 13), M(22, 14). `Right` -> P Stuck. M Stuck/Turns.
  - Action: Face Right (Wall) -> Interact. Face Down (M) -> Interact.
- **Combined Plan**: `Right`, `A`, `Down`, `A`, `Up`, `A`.
- **Note**: `Up` at end might move P, but risk is acceptable to hit M in Hyp 1.
- **Action**: Execute Sweep.