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
- **Player**: (21, 13).
- **Murkrow**: (21, 12). (Derived from mimicry).

## Strategy: The Validated Wide Flank (Setup Execution)
- **Goal**: Reach P(22, 11), M(22, 10).
- **Current**: P(22, 13), M(22, 12).
- **Sequence**:
  1. `Left` x2 -> P(20, 13), M(20, 12).
  2. `Up` -> P(20, 12), M(20, 11).
  3. `Right` x2 -> P(22, 12), M(22, 11).
  4. `Up` -> P(22, 11), M(22, 10).
- **Next Turn**: `Left` x2 (Desync), `Down` x4 (Deliver).
- **Action**: Execute Setup.