# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Plan: Murkrow Delivery (The Overlap Strat)
1. **Reset**: From P(10, 4), M(9, 3).
2. **Block Up**: `Left` -> P(9, 4), M(8, 3). `Up` -> P(9, 3). (M blocked at 8, 2).
   - *Result*: P(9, 3), M(8, 3).
3. **Block Left**: `Left` -> P(8, 3), M(7, 3). `Left` -> P(7, 3). (M blocked at 6, 3).
   - *Result*: Overlap at (7, 3).
4. **Transport**:
   - `Right` x3 -> (10, 3).
   - `Down` x2 -> (10, 5).
   - `Right` -> (11, 5).
   - `Down` x5 -> (11, 10).
   - `Right` x3 -> (14, 10).

## Trap Data
- Warp Traps: (26, 9), (26, 10), (24, 11), (25, 11).
- Murkrow Blockers: Row 2 (Desks), Row 9 (Walls).
- Safe Path: Col 11 via Row 6.
[Turn 36029] Hit wall at (11, 4). M desynced. Switching to Overlap Strat to force perfect sync.
[Turn 36042] Restarting Murkrow interaction at (7, 2). Previous attempts failed due to desync or lack of movement.
Plan:
1. Interact (Confirm text).
2. Move Right (Buffer against desk).
3. Move Down (Pull to 7, 3).
4. Verify position visually.