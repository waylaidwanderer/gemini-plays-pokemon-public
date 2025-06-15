# Agent Improvement Plan
- **`dungeon_path_analyzer_agent`:** This agent is unreliable because it suggests paths through walls. It needs a major overhaul to implement a proper pathfinding algorithm (like A* or BFS) that correctly parses the `map_xml_string` for all obstacles (impassable tiles, objects, ledges). I will refine its system prompt to enforce this.
- **`master_pathfinder_agent`:** This agent has been identified as fundamentally unreliable in complex dungeons. It has been deleted to prevent accidental use.

# Mt. Moon Navigation Strategy
- **Current Objective:** Find the correct ladder on Mt. Moon 1F that leads to the next floor.
- **Method:**
  1. Use my own map-reading skills for all short-term, tile-by-tile movement.
  2. - The `dungeon_path_analyzer_agent` is unreliable for path generation. Use it ONLY to identify the coordinates of points of interest (trainers, items, warps), then use manual map-reading to navigate.
  3. Select ONE identified path/POI and explore it systematically until its conclusion (dead end, warp, or trainer battle).
  4. Do not switch goals erratically. Fully explore one branch before starting another.

# Battle Learnings
- **Type Matchups:**
  - Electric is NOT very effective vs. Bug/Grass (Paras).
  - Electric is NOT very effective vs. Grass/Poison (Oddish, Bellsprout).
- **Risk Management:** Do not switch in low-level, non-resistant Pokémon to weaken wild encounters. It's too risky.

# Dungeon Mechanics
- **Defeated Trainers:** Defeated trainers in Mt. Moon and on Route 3 act as impassable obstacles.

# WKG To-Do
- Investigate how to properly log one-way, variable-source warps like Escape Rope in the World Knowledge Graph.