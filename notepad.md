# Game Mechanics & Rules
- **Battle-Warps:** A tile at Mt. Moon B2F (29, 9) can trigger a wild battle that also warps the player to B1F (21, 12). This is unreliable.
- **Confusion:** Wears off after battle.
- **Item-Gated NPCs:** Some NPCs block paths and require a specific item to pass. Ex: Rocket at Mt. Moon B2F (30, 12) requires a fossil.

# Battle Notes & Movesets
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras) or Grass/Poison (Oddish, Bellsprout).
- Flying is 4x effective vs. Bug/Grass (Paras).

# Critical Lessons Learned
- **LESSON 1:** In complex, multi-level dungeons like Mt. Moon, use the `pathfinding_agent` proactively to plan routes *before* moving, not just reactively after getting lost. Always double-check agent output for logical errors (like ignoring elevation) before committing.
- **LESSON 2:** Do not assume NPCs are impassable walls. Always check for open paths around them before concluding a route is blocked (e.g., Rocket at Mt. Moon B2F (30, 12)).
- **LESSON 3:** Do not mark paths as 'dead ends' until all connecting branches are fully explored. Some paths in dungeons are intentionally misleading loops.
- **LESSON 4:** Defeated trainers can become impassable obstacles, completely blocking paths (e.g., Rocket at Mt. Moon B2F (16, 23)).
- **LESSON 5:** Trust the `pathfinding_agent`. A `path_found: false` result is definitive proof that the target is unreachable from the current location and indicates the map is sectioned off.
- **LESSON 6:** Avoid training low-level Pokémon in high-risk areas. Use the `optimal_training_spot_agent` for efficiency.
- **LESSON 7:** If a specific action fails repeatedly (e.g., using a warp), test alternative hypotheses immediately. Do not get stuck in a loop.
- **LESSON 8:** Immediately and accurately document all map connections in the World Knowledge Graph. A single missing edge can invalidate pathfinding.

# Agent & Tool Notes
- The `pathfinding_agent` is reliable for on-map navigation but must be given clear instructions regarding elevation. Its prompt needs refinement.
- The `healing_spot_finder_agent` is reliable for multi-map pathfinding to Pokémon Centers.
- The `battle_switch_agent` is reliable for calculating switch sequences.
- The `exploration_planner_agent` has proven unreliable and needs refinement before use.

# Evolution Plans
- **SPIKE (Nidoran♂):** Evolve at Lv. 16 for an early power spike with Nidoking. This misses out on Thrash, but provides great TM potential.