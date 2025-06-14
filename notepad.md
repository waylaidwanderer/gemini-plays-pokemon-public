# Game Mechanics & Lessons

## Route 3 Ledge Puzzle & One-Way Progression
The primary lesson from the Route 3 disaster is to **trust game state data over visual perception and assumptions.**

- **Contradiction:** The game state insisted Pewter City was `Reachable: Yes`, which I misinterpreted as reachable from *anywhere* on the map. After jumping down a ledge, I became trapped in a one-way section. The `Reachable` status likely applies to the map as a whole, not my specific isolated position.
- **Solution:** The path forward was east, towards the remaining unseen tiles, not west. Jumping down ledges can commit you to a path, making retreat impossible. This is a critical mechanic to remember.
- **Core Principle:** Analyze all available data (`Reachable` status, `Reachable Unseen Tiles`, map layout) before committing to a path, especially one involving ledges. Do not assume retreat is always possible.

## Agent Development
- The `npc_aware_pathfinder_agent` was unreliable. It has been replaced with `ledge_aware_pathfinder_agent`, which has more specific instructions for handling complex terrain like one-way ledges.