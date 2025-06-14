# Gem's New Strategy (Post-Critique)

## 1. Core Principles
*   **Manual Navigation First:** Abandon pathfinding agents on complex maps like Route 3. Explore systematically: follow a path to its conclusion (dead end or transition), then backtrack to the last junction and try the next path. Trust my own eyes and the map data.
*   **Master the UI:** Actions require **selection (D-Pad) AND confirmation (A button)**. No more fumbling in menus.
*   **Proactive Strategy:** Use `type_chart_lookup_agent` *before* entering new areas or challenging strong trainers. Don't wait until I'm already in a bad matchup.
*   **Trust the Game State:** The `Reachable Unseen Tiles` list is the source of truth. If it says there's a path, a path exists. My assumptions are secondary.

## 2. Active Hypothesis & Plan
*   **Hypothesis:** The entrance to Mt. Moon is at the far eastern end of Route 3, past the small Pokémon Center building.
*   **Immediate Plan:**
    1.  Win this wild Mankey battle efficiently.
    2.  Systematically explore the area east and north of the Route 3 Pokémon Center building.
    3.  Find the exit to Mt. Moon.