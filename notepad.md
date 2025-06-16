# Game Mechanics & Rules
- **Battle-Warps:** A tile at Mt. Moon B2F (29, 9) can trigger a wild battle that also warps the player to B1F (21, 12). This is unreliable.
- **Confusion:** Wears off after battle.
- **Item-Gated NPCs:** Some NPCs block paths and require a specific item to pass. Ex: Rocket at Mt. Moon B2F (30, 12) requires a fossil.

# Battle Notes & Movesets
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras) or Grass/Poison (Oddish, Bellsprout).
- Flying is 4x effective vs. Bug/Grass (Paras).

# Agent & Tool Notes
- **LESSON 13 (REVISED):** The `pathfinding_agent` was unreliable because its initial logic failed to account for two critical obstacle types: 1) impassable `<Object>` tags (NPCs, items) and 2) elevation changes (`ground` vs. `elevated_ground` without `steps`). The prompt was refined to explicitly treat all objects (except Pikachu) as walls and to respect elevation rules, making it reliable for navigation.
- The `healing_spot_finder_agent` is reliable for multi-map pathfinding to Pokémon Centers.
- The `battle_switch_agent` is reliable for calculating switch sequences.
- The `exploration_planner_agent` has proven unreliable and needs refinement before use.
- **LESSON 13 (REVISED):** The `pathfinding_agent` was unreliable because its initial logic failed to account for two critical obstacle types: 1) impassable `<Object>` tags (NPCs, items) and 2) elevation changes (`ground` vs. `elevated_ground` without `steps`). The prompt was refined to explicitly treat all objects (except Pikachu) as walls and to respect elevation rules, making it reliable for navigation.

# Evolution Plans
- **SPIKE (Nidoran♂):** Evolve at Lv. 16 for an early power spike with Nidoking. This misses out on Thrash, but provides great TM potential.

# Critical Lessons Learned
- **LESSON 1:** In complex, multi-level dungeons like Mt. Moon, use the `pathfinding_agent` proactively to plan routes *before* moving, not just reactively after getting lost. Always double-check agent output for logical errors (like ignoring elevation) before committing.
- **LESSON 2:** Do not assume NPCs are impassable walls. Always check for open paths around them before concluding a route is blocked (e.g., Rocket at Mt. Moon B2F (30, 12)).
- **LESSON 3:** Do not mark paths as 'dead ends' until all connecting branches are fully explored. Some paths in dungeons are intentionally misleading loops.
- **LESSON 4:** Defeated trainers can become impassable obstacles, completely blocking paths (e.g., Rocket at Mt. Moon B2F (16, 23)).
- **LESSON 5:** Trust the `pathfinding_agent`. A `path_found: false` result is definitive proof that the target is unreachable from the current location and indicates the map is sectioned off.
- **LESSON 6:** Avoid training low-level Pokémon in high-risk areas. Use the `optimal_training_spot_agent` for efficiency.
- **LESSON 7:** If a specific action fails repeatedly (e.g., using a warp), test alternative hypotheses immediately. Do not get stuck in a loop.
- **LESSON 8:** Immediately and accurately document all map connections in the World Knowledge Graph. A single missing edge can invalidate pathfinding.
- **LESSON 9:** My navigation in Mt. Moon has been extremely inefficient due to a failure to understand and respect elevation changes. I must mentally check agent paths for invalid elevation transitions before moving.
- **LESSON 10:** My World Knowledge Graph management is a critical weakness. I must be diligent in adding nodes AND edges for every single map transition to maintain data integrity. The `world_knowledge_manager_agent` should help with this.
- **LESSON 11:** I have been fixating on incorrect hypotheses for too long. I need to abandon failing strategies much faster and be more flexible in my approach.
- **LESSON 12:** The ladder at B1F(26,10) leads UP to 1F. The ladder at B1F(18,12) leads DOWN to B2F(26,10). Taking the B2F(26,10) ladder back up results in an immediate, one-way warp back to B1F(18,12). The entire eastern section of B2F is a confirmed dead-end loop. Do not enter again.
- **LESSON 13 (REVISED):** The `pathfinding_agent` was unreliable because its initial logic failed to account for two critical obstacle types: 1) impassable `<Object>` tags (NPCs, items) and 2) elevation changes (`ground` vs. `elevated_ground` without `steps`). The prompt was refined to explicitly treat all objects (except Pikachu) as walls and to respect elevation rules, making it reliable for navigation.
- **LESSON 14:** Prioritize direct game state information and personal observation over external guides or preconceived notions. The Super Nerd at Mt. Moon 1F (25, 32) was a non-battling NPC, despite my assumption he was a mandatory fight.

- **LESSON 15:** The elevated platform in the eastern part of Mt. Moon B2F, accessed via the steps at (29,8), is a confirmed dead end. The path forward is not there.