# Mt. Moon Exploration Plan

**Core Strategy:** No more chaotic wandering. I will explore Mt. Moon systematically using manual map-reading for all navigation.

**Methodology:**
1.  **Identify POIs:** Use the `dungeon_path_analyzer_agent` ONLY to get the coordinates of Points of Interest (trainers, items, warps).
2.  **DO NOT TRUST AGENT PATHING:** The agent's path descriptions are unreliable and must be ignored.
3.  **Systematic Clearing:** Pick a single, visually verifiable path from my current location towards a POI.
4.  **Explore to Completion:** Follow that chosen path to its absolute end (a wall, a warp, or a battle).
5.  **Backtrack and Repeat:** After completing one path, backtrack to the last junction and explore the next branching path. This prevents getting lost in loops.

# Agent Improvement Plan
- **`dungeon_path_analyzer_agent`:** This agent is fundamentally broken for navigation. Its system prompt needs a complete overhaul to force it to run a proper pathfinding script (like A* or BFS) that correctly parses all obstacles from the `map_xml_string`. Until it's fixed, it is **only for identifying POI coordinates**.

# Battle Learnings
- **Type Matchups:**
  - Electric is ineffective vs. Ground (Geodude, Sandshrew).
  - Grass is 4x effective vs. Rock/Ground (Geodude).
  - Electric is NOT very effective vs. Bug/Grass (Paras).
  - Electric is NOT very effective vs. Grass/Poison (Oddish, Bellsprout).
- **Risk Management:** Do not switch in low-level, non-resistant Pokémon to weaken wild encounters.

# Dungeon Mechanics
- **Defeated Trainers:** Defeated trainers in Mt. Moon and on Route 3 act as impassable obstacles.
- **Trap Ladder:** The ladder at (26, 16) on 1F is a one-way trap that leads back to 1F. Do not use.