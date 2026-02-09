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

## Strategy: The Wall-Scrape
- **Goal**: Align P(22, 12), M(23, 12).
- **Execution**:
  1. `Right` x4 -> P(26, 13), M(26, 12).
  2. `Up` -> P(26, 12), M(26, 11).
  3. `Left` x3 -> P(23, 12), M(24, 11). (M scraped off at 23, 11).
  4. `Down` -> P(23, 13), M(24, 12).
  5. `Left` x2 -> P(21, 13), M(22, 12).
  6. `Right` -> P(22, 13), M(23, 12).
  7. `Up` -> P(22, 12), M(23, 12). (M scraped off at 23, 11).
  8. Interact Right.