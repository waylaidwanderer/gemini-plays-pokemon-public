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
- **Status**: Surrounded (Up: M, Down: Wall, Left: Grunt, Right: Door).

## Strategy: The Grunt Slide Test
- **Hypothesis**: If Player blocked by Grunt, Murkrow still mimics.
- **Plan**:
  1. Press `Left`. (Player Blocked by Grunt).
  2. Check if Murkrow moves `Left` to (21, 13).
  3. If yes, Murkrow is now at (21, 13).
  4. If no, Murkrow is fixed.
- **Action**: Press `Left`.