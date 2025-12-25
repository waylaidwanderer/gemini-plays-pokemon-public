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
- **Item Path Solution (B1F/1F):** [Completed: Found Iron (B1F). Protein (1F) skipped - Bag Full]
    - **Conclusion:** The path starting from B3F East Ladder `(15, 5)` is a bonus item loop.
    - **Action:** Backtrack to B3F Main Area.
- **HM07 Strategy:**
    - **Location:** B3F `(5, 7)`.
    - **Obstacle:** Rock at `(6, 6)` (Likely Rock Smash).
    - **Plan:** Navigate to `(6, 5)` -> Use Rock Smash on `(6, 6)` -> Get Item.
- **Current Navigation:**
    - **Goal:** Nickname Sneasel, then use Rock Smash on `(6, 6)` to get Item (Likely HM07).
    - **Status:** Finished nicknaming. Preparing to smash rock at `(6, 6)`.
    - **Note:** Sneasel sent to Box 1.
- **Backtrack Log (Completed):** Successfully navigated B1F/B2F loop to return to B3F. The side path was an item loop.