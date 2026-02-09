# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Chase Murkrow from (7, 2) to the Boss Door.

## Map Knowledge
- **B2F Layout**:
  - **West Wing**: Current location (Murkrow here).
  - **East Wing**: Target location (Boss Door).
  - **Connections**:
    - Gap at B2F (15, 13) (South).
    - Fake Computer Passage at B2F (19, 10) (North).
- **Stairs**:
  - NW: B2F (3, 2) <-> B1F (3, 2).
  - NE: B2F (27, 2) <-> B1F (27, 2).
  - SE: B2F (27, 14) <-> B1F (27, 14).
- **Secrets**:
  - Fake Wall at B1F (6, 1) connects West/East wings on B1F.
  - Switch on Persian Statue at B1F (24, 6) disables traps.

## Current Task
- **Murkrow Chase**:
  - Status: LOST.
  - Mistake: Mental Map XML does NOT track live sprites. Visual sweep is mandatory.
  - Search Plan:
    1. Sweep Fake Computer Room (19, 4).
    2. Sweep NE Corner (27, 2).
    3. Re-check the "Exit" stairs at (27, 2) just in case.
  - Note: Grunt at (2, 4) is not Murkrow.