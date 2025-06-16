# Game Mechanics & Rules
- **Confusion:** Wears off after battle.

# Battle Notes
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras) or Grass/Poison (Oddish, Bellsprout).
- Flying is 4x effective vs. Bug/Grass (Paras).

# Team Strategy
- **SPIKE (Nidoran♂):** Evolve at Lv. 16 for an early power spike with Nidoking. This misses out on Thrash, but provides great TM potential.

# Agent & Tool Notes
- The `healing_spot_finder_agent` is reliable for multi-map pathfinding to Pokémon Centers.
- The `battle_switch_agent` is reliable for calculating switch sequences.
- The `dungeon_navigator_agent` is the preferred tool for complex, multi-floor dungeons.
- The `dungeon_pathfinder_agent` is essential for creating safe, short-range paths within a single map.
- The `battle_escape_agent` is now my primary tool for running from non-essential wild battles.

# Navigation Puzzles & Solutions
- **Mt. Moon B2F - Steps:** A `steps` tile at (29, 8) allows access to an elevated platform.
- **Mt. Moon B2F - Non-battling Rocket:** A Rocket at (28, 18) does not battle and can be bypassed by walking around him to the north.
- **Mt. Moon B1F - One-way Ladder:** The ladder at (18, 12) is activated by first stepping off onto the adjacent elevated tile at (18, 11) and then stepping back onto the ladder.

# Critical Lessons Learned
- **LESSON 1:** In complex dungeons, use agents (`dungeon_navigator_agent`, `pathfinding_agent`) proactively to plan routes *before* moving, not just reactively after getting lost.
- **LESSON 2:** Do not mark paths as 'dead ends' until all connecting branches and warps are fully explored.
- **LESSON 3 (CORRECTED):** Trainer sprites are not physical barriers after defeat.
- **LESSON 4:** Trust agent output. A `path_found: false` result is definitive proof that a target is unreachable.
- **LESSON 5:** Avoid training low-level Pokémon in high-risk areas. Use the `optimal_training_spot_agent` for efficiency.
- **LESSON 6:** Immediately and accurately document all map connections in the World Knowledge Graph.
- **LESSON 7:** Do not fixate on incorrect hypotheses. Abandon failing strategies much faster.
- **LESSON 8 (CORRECTED):** The ladder at Mt. Moon B1F (18, 12) is the CORRECT path down to the main area of B2F.
- **LESSON 9:** The `pathfinding_agent` is only reliable if its prompt is extremely specific about obstacle rules.
- **LESSON 10:** Prioritize direct game state information over external guides.
- **LESSON 11:** The elevated platform in the eastern part of Mt. Moon B2F, accessed via the steps at (29,8), is a confirmed dead end.

# Discoveries & Oddities
- **Battle-Warps:** A tile at Mt. Moon B2F (29, 9) can trigger a wild battle that also warps the player to B1F (21, 12). This is unreliable.
- **Item-Gated NPCs:** Some NPCs block paths and require a specific item to pass. Ex: Rocket at Mt. Moon B2F (30, 12) requires a fossil.