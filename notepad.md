# Current Strategy: Post-Game
- **Timestamp:** Turn 25602 (Jan 6, 2026)
- **Primary Goal:** Challenge Red at Mt. Silver.
- **Immediate Task:** Reach the Northwest area of Silver Cave Outside.
- **Current Location:** Route 28 (21, 15). Testing Ledge.
- **Objective:** Access the bottom path (Row 17) to reach the East Corridor.
- **Hypothesis:** `FLOOR_UP_WALL` tiles (e.g., 21, 16) are ledges jumpable South.
- **Plan:**
    1. Attempt to walk South from (21, 15).
    2. If successful, walk East along Row 17 to finding the hidden path North.
    3. If blocked, backtrack to Entrance (0, 13) and try jumping the ledge at (0, 14).

# Tile Mechanics & Observations
- **LEDGE_HOP_DOWN/LEFT/RIGHT:** Standard one-way jumpable tiles.
- **FLOOR_UP_WALL:** Inconsistent behavior observed.
    - **Confirmed Ledge:** (39, 32) allowed jumping South.
    - **Confirmed Wall:** (6, 30) and (28, 34) blocked movement South.
    - **Strategy:** Treat as WALL unless verified otherwise.
- **Navigation Notes:**
    - The "Central" area (x=5) connects to the West path via Row 22 (re-verified via Mental Map).
    - Row 30 acts as a hard barrier across most of the map, separating the North and South sections.

# Key Locations
- **Route 28 House:** (7, 3) [Unreachable]
- **Route 28 Gatehouse:** (33, 5) -> Leads to Viridian/Victory Road
- **Silver Cave Outside (Next Map):** Entrance at (0, 13) on Route 28.
- **Mt. Silver Cave Entrance:** (18, 11) [On Silver Cave Outside Map]
- **Pokemon Center:** (23, 19) [On Silver Cave Outside Map]