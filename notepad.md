# Current Strategy: Post-Game
- **Timestamp:** Turn 25602 (Jan 6, 2026)
- **Primary Goal:** Challenge Red at Mt. Silver.
- **Immediate Task:** Reach the Northwest area of Silver Cave Outside.
- **Current Location:** Silver Cave Outside (39, 31).
- **Issue:** Map Width Mismatch. XML says 40, but visual shows path extending East to at least x=44.
- **Action:** Exploring East beyond x=39.
- **Plan:**
    1. Walk East to investigate the "hidden" area.
    2. Try to jump the ledge (Row 32) at a different coordinate (e.g., x=41).
    3. Navigate to Pokemon Center.
- **Hypothesis:** The ledge at (39, 32) failed, but maybe (41, 32) works, or there is a gap further East.

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