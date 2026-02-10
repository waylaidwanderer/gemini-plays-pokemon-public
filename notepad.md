# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Mechanics (Verified)
- **Mimicry**: Intended behavior is mimicry.
- **Observation**: Side-pull failed. Tether likely requires range <= 2.
- **Current State**: Player (7, 4) -> Moving to (7, 3). Murkrow at (7, 2).

## Plan: Gap 1 Compression
1. **Current**: Move **Up** to (7, 3).
   - If M moves to (7, 1) -> Tether Active. Gap 2. Proceed to step 2.
   - If M stays at (7, 2) -> Tether Inactive. Gap 1. Interact to wake.
2. If Gap 2 (P at 7, 3; M at 7, 1):
   - Move **Up** to (7, 2).
   - M tries (7, 0) -> Blocked by Wall. Stays at (7, 1).
   - Result: P(7, 2), M(7, 1). **Gap 1**.
3. Execute "Gap 1 Bottom Run" (Down to Row 13).

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (6, 2) Wall.
  - (15, 13) Gap.