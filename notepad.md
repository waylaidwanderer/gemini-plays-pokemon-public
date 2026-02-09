# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision**: 
  - If Player is blocked, Murkrow [UNK]. (Testing this now).
  - If Murkrow is blocked, Murkrow stays.
  - Murkrow and Player cannot overlap.

## Current State
- **Player**: (22, 14).
- **Murkrow**: (22, 13) (Visual Confirmation).
- **Door**: (23, 14).

## Strategy: Interaction & Test
1. Interact `Up` with Murkrow.
2. If no success, Test Blocked Movement:
   - Move `Left`. (Player blocked by Grunt at 21, 14).
   - Observe if Murkrow moves from (22, 13) to (21, 13).