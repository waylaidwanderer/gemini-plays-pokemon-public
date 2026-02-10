# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Mechanics Testing
- **Current State**: Player (7, 4), Murkrow (7, 2). Gap = 2.
- **Goal**: Establish a vertical gap of **1 tile** (Player directly below Murkrow) to fit through the passage at (15, 13).
- **Hypothesis**: Moving Up against the North Wall (7, 0) will block the Murkrow while allowing me to close the distance.

## Plan: Top Wall Compression
1. Move Up to (7, 3).
   - If M moves to (7, 1): Gap remains 2. Proceed to step 2.
   - If M stays at (7, 2): Gap becomes 1. Skip to step 3.
2. Move Up to (7, 2).
   - M tries to move to (7, 0) -> BLOCKED by Wall.
   - P moves to (7, 2).
   - Result: P(7, 2), M(7, 1). Gap = 1.
3. Verify Follow: Move Down 1 step. Check if M follows.
4. Execute "Gap 1 Bottom Run" (Down to Row 13, Right to x=15).

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Walls**: (7, 0) is a hard wall.
- **Passage**: (15, 13) is a gap, (15, 12) is floor. Perfect for P(Row 13)/M(Row 12).