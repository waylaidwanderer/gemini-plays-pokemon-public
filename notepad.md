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
- Player: (22, 13).
- Murkrow: (22, 12).
- Plan: "The Desync Circuit"
  1. Left x3 -> P(19, 13), M(21, 12). (Block M at 20, 12 twice).
  2. Up x2 -> P(19, 11), M(21, 11). (Block M at 21, 10).
  3. Right x2 -> P(21, 11), M(22, 11). (Block M at 23, 11).
  4. Down x3 -> P(21, 14), M(22, 14).
  5. Face Right, Interact.

## Strategy: The Desync Circuit
- **Goal**: Align P(21, 14), M(22, 14).
- **Execution**:
  - `Left`, `Left`, `Left`.