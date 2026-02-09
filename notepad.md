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

## Strategy: The Test
- **Action**: `Left`.
- **Observation Needed**: Does Murkrow move to (21, 13)?
- **Implication**:
  - If YES: "Grunt Slide" works. Proceed to Setup.
  - If NO: "Grunt Slide" fails. Need new theory.
- **Action**: Execute `Left`.