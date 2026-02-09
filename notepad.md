# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision Rules**:
  - P Blocked: Murkrow Stays.
  - Chase Blocked: P cannot move into M's tile even if M moves away.

## Current State
- Player: (22, 13) (GameState) / (21, 13) (Screen).
- Murkrow: (22, 12).
- Grunt: (21, 14) Facing Left (Safe).

## Strategy: Open Door
- **Goal**: Position Murkrow at (22, 13) and Player at (22, 14).
- **Execution**:
  1. `Right` (Align P/M).
  2. `Down` (Move P to 22,14, M to 22,13).
  3. `Right` (Face Door).
  4. `A` (Open).