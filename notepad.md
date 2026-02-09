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

## Strategy: The Pull-Down
- **Goal**: Place M at (22, 14). Interact from (22, 15).
- **Current**: P(19, 13). M presumed (19, 12).
- **Plan**:
  1. `Right` x3 -> P(22, 13), M(22, 12).
  2. `Down` x2 -> P(22, 15), M(22, 14).
  3. Face `Up`, Interact.
- **Action**: Execute Sequence.