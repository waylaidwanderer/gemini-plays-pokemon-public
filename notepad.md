# Game Mechanics & Lessons

## Route 3 Ledge Puzzle & One-Way Progression
The primary lesson from the Route 3 disaster is to **trust game state data over visual perception and assumptions.**

- **Contradiction:** The game state insisted Pewter City was `Reachable: Yes`, which I misinterpreted as reachable from *anywhere* on the map. After jumping down a ledge, I became trapped in a one-way section. The `Reachable` status likely applies to the map as a whole, not my specific isolated position.
- **Solution:** The path forward was east, towards the remaining unseen tiles, not west. Jumping down ledges can commit you to a path, making retreat impossible. This is a critical mechanic to remember.
- **Core Principle:** Analyze all available data (`Reachable` status, `Reachable Unseen Tiles`, map layout) before committing to a path, especially one involving ledges. Do not assume retreat is always possible.

## Agent Development
- The `npc_aware_pathfinder_agent` was unreliable. It has been replaced with `ledge_aware_pathfinder_agent`, which has more specific instructions for handling complex terrain like one-way ledges.

## Goal Setting & Progression
- The AI critique highlighted a major flaw: setting goals that are geographically impossible (e.g., targeting Misty from Route 3). Future goals must be based on the immediate next step in progression, like reaching the next town or clearing the current dungeon.

## Hypothesis & Failure Log
- A place to track failed strategies to avoid repeating them.

## Route 3 Ledge Puzzle & One-Way Progression
- The `ledge_aware_pathfinder_agent` failed, trying to route me through an impassable wall at x=24. This confirms I am on a one-way path after jumping down a ledge earlier.
- I cannot retreat to Pewter City. The only way forward is east, towards Mt. Moon, despite having fainted Pokémon. This is a high-risk situation.
- Lesson: Ledges can create points of no return. Always check the map thoroughly before committing.