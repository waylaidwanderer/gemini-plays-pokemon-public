# Ice Path Strategy

## Goal
- **Primary:** Earn the Rising Badge from Clair in Blackthorn City.
- **Secondary:** Find HM07 Waterfall.
- **Current Task:** Explore B1F South-East Ice area to find path to HM07 or Blackthorn City.

## Map Data & Observations

### B3F (3_65)
- **Ladder to B2F:** `(3, 5)` (Main Path).
- **Ladder to B2F (East):** `(15, 5)` (Leads to isolated B2F area).
- **Item:** `(5, 7)` (Unreachable directly).
- **Rock:** `(6, 6)`.

### B2F (3_64)
- **Main Area:** Access via B1F/B3F.
- **Isolated Area (Blackthorn Side):** Access via B3F `(15,5)`.
    - **Loop:** Sliding Right from `(3, 14)` loops back to start.
    - **Dead End:** Left Ledge at `(4, 8)` loops back to start.
    - **Ladder:** `(3, 15)` leads down to B1F South.
    - **Item at (8, 16):** Isolated. Likely requires drop from B1F.

### B1F South (3_62)
- **Access:** Via B2F Ladder `(3, 15)` -> Arrive at `(11, 27)`.
- **Layout:** Ledges at Row 24 block North. Must explore South-East Ice.
- **Ice Entry:** `(17, 28)`.

## Current Status
- **Location:** B1F South `(14, 26)`.
- **Immediate Plan:** Navigate East to `(17, 27)` to enter the ice at `(17, 28)`. The direct path South was blocked by a wall.
## Tile Mechanics
- **ICE:** Sliding movement. Continues until blocked by WALL, OBJECT, or non-ICE tile.
- **FLOOR:** Normal walkable terrain.
- **WALL:** Impassable.
- **PIT:** Falls to the floor below.
- **LADDER:** Transitions between floors.
- **FLOOR_UP_WALL:** Observed on B2F. Acts as a ledge (one-way).
- **South-East Ice Room (B1F):**
    - Entry: `(17, 28)`.
    - Slide Left to `(14, 29)`, then Down to `(14, 33)`.
    - **South Landing:** `(11, 33)` (Floor). Accessible from `(14, 33)` via Left slide.
    - **North Landing:** `(11, 30)` (Floor). Path: `(14, 33) -> R(15, 33) -> U(15, 29) -> R(19, 29) -> D(19, 33) -> L(17, 33) -> U(17, 31) -> L(13, 31) -> U(13, 30) -> L(11, 30)`.
- **Item Path Solution (B1F):** [Completed: Found Iron]
- **Current Navigation:**
    - **Goal:** Reach North Landing `(11, 30)`.
    - **Sequence:** `(11, 33)` -> Right to `(15, 33)` -> Up to `(15, 29)` -> Right to `(19, 29)` -> Down to `(19, 33)` -> Left to `(17, 33)` -> Up to `(17, 31)` -> Left to `(13, 31)` -> Up to `(13, 30)` -> Left to `(11, 30)`.
    - **Status:** At `(19, 33)`, Sliding Left to `(17, 33)`.
- **Return & Progress Plan:**
    - **Escape:** From `(5, 35)` -> Slide R to `(8, 35)` -> Slide U to `(8, 34)` -> Slide R to `(9, 34)` (Land on `9, 33`).
    - **Transition:** Walk R to `(11, 33)` (South Landing).
    - **North Path:** Executing above sequence.