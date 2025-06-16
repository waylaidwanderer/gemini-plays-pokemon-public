# Game Mechanics & Rules
- **Confusion:** Wears off after battle.
- **Defeated Trainers:** Act as impassable obstacles.

# Battle Notes
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras) or Grass/Poison (Oddish, Bellsprout).
- Flying is 4x effective vs. Bug/Grass (Paras).

# Team Strategy
- **SPIKE (Nidoran♂):** Evolve at Lv. 16 for an early power spike with Nidoking.

# Agent & Tool Notes
- The `dungeon_navigator_agent` is preferred for complex, multi-floor dungeons. It requires a complete World Knowledge Graph.
- The `dungeon_pathfinder_agent` is essential for creating safe, short-range paths within a single map.
- The `battle_escape_agent` is my primary tool for running from non-essential wild battles.

# Mt. Moon Navigation
- **Goal:** Find the Super Nerd with the fossils to exit to Route 4.
- **Ladders:**
  - (18, 12) on 1F: Leads to the main B1F/B2F areas. Requires stepping on (18, 11) then back on the ladder to activate.
  - (6, 6) on 1F: Leads to the northwest section of B1F. This is my current exploration target.
  - (26, 16) on 1F: A trap ladder leading to a small, isolated loop on B1F.
- **Key NPCs & Obstacles:**
  - Super Nerd at (25, 32) on 1F is a **non-battling NPC**. The path to him is a dead end for progression.
  - Rocket at (30, 12) on B2F blocks a path and mentions fossils, but can be bypassed.
  - A non-battling Rocket is at (28, 18) on B2F.
- **Discoveries:**
  - An elevated platform in the eastern part of Mt. Moon B2F, accessed via steps at (29,8), is a confirmed dead end.

# Strategic Principles
- **Principle 1: Trust and Maintain Your Tools.** Use pathfinding agents proactively *before* long journeys. A `path_found: false` result likely means the World Knowledge Graph is incomplete, not that the agent is broken. Always keep the WKG updated.
- **Principle 2: Explore Thoroughly.** Do not mark paths as dead ends until all connecting branches and warps are fully explored.
- **Principle 3: Adapt Quickly.** Do not fixate on incorrect hypotheses. If a plan isn't working, abandon it and form a new one based on evidence. The Super Nerd at (25, 32) was a lesson in this.