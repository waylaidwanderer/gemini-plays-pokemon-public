# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision Rules**:
  - P Blocked: Murkrow Stays.
  - M Blocked: Murkrow Stays.
  - No Overlap.

## Current State
- **Player**: (22, 13). (Confirmed by Game State).
- **Murkrow**: Unknown. Likely (22, 12) or (21, 13) or (23, 13).
- **Goal**: Find Murkrow and Open Door.

## Strategy: Position Verification
- **Action**: Move `Left` to (21, 13).
- **Reason**: To verify movement and look for Murkrow.
- **Follow-up**: If at (21, 13), proceed with Alignment (`Up`, `Right`, `Up`).