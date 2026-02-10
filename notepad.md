# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Plan: Murkrow Delivery (The Wall Pin Strat)
1. **Wake**: P(7, 3), M(7, 2). Interact.
2. **Lead**: `Down` x3 -> P(7, 6), M(7, 5).
   - *Check*: Path is clear.
3. **Cross**: `Right` x5 -> P(12, 6), M(12, 5).
   - *Check*: Row 5 and 6 are clear.
4. **Pin**: `Up` -> P(12, 5). M tries to go to (12, 4) but hits WALL.
   - *Result*: P(12, 5), M(12, 5) (Overlap).
5. **Deliver**: Walk to Shutter at (14, 10). M is carried.

## Trap Data
- Warp Traps: (26, 9), (26, 10), (24, 11), (25, 11).
- Murkrow Blockers: Row 2 (Desks), Row 9 (Walls).
- Safe Path: Col 11 via Row 6.
[Turn 36050] Executing Wall Pin Strat. Interact -> Down.
[Turn 36051] Murkrow failed to follow 'Down'. It remained at (7, 2).
Hypothesis: Direct 'Down' movement might be breaking the link or I moved too fast. Retrying with 'Right' (Buffer) move to see if diagonal tension helps.