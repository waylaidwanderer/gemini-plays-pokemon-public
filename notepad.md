# Game Mechanics & Rules
- **Battle-Warps:** A tile at Mt. Moon B2F (29, 9) can trigger a wild battle that also warps the player to B1F (21, 12). This is unreliable.
- **Confusion:** Wears off after battle.
- **Item-Gated NPCs:** Some NPCs block paths and require a specific item to pass. Ex: Rocket at Mt. Moon B2F (30, 12) requires a fossil.

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

# Critical Lessons Learned
- **LESSON 1:** In complex, multi-level dungeons like Mt. Moon, use the `pathfinding_agent` proactively to plan routes *before* moving, not just reactively after getting lost.
- **LESSON 2:** Do not assume NPCs are impassable walls. Always check for open paths around them before concluding a route is blocked.
- **LESSON 3:** Do not mark paths as 'dead ends' until all connecting branches are fully explored.
- **LESSON 4:** Defeated trainers can become impassable obstacles, completely blocking paths (e.g., Rocket at Mt. Moon B2F (16, 23)).
- **LESSON 5:** Trust the `pathfinding_agent`. A `path_found: false` result is definitive proof that the target is unreachable from the current location and indicates the map is sectioned off.
- **LESSON 6:** Avoid training low-level Pokémon in high-risk areas. Use the `optimal_training_spot_agent` for efficiency.
- **LESSON 7:** If a specific action fails repeatedly (e.g., using a warp), test alternative hypotheses immediately. Do not get stuck in a loop.
- **LESSON 8:** Immediately and accurately document all map connections in the World Knowledge Graph. A single missing edge can invalidate pathfinding.
- **LESSON 9:** My navigation in Mt. Moon has been extremely inefficient due to a failure to understand and respect elevation changes. I must mentally check agent paths for invalid elevation transitions before moving.
- **LESSON 10:** My World Knowledge Graph management is a critical weakness. I must be diligent in adding nodes AND edges for every single map transition to maintain data integrity.
- **LESSON 11:** I have been fixating on incorrect hypotheses for too long. I need to abandon failing strategies much faster and be more flexible in my approach.
- **LESSON 12:** The ladder at B1F(26,10) leads UP to 1F. The ladder at B1F(18,12) leads DOWN to the B2F eastern dead-end loop. Do not use the B1F(18,12) ladder.
- **LESSON 13:** The `pathfinding_agent` is only reliable if its prompt is extremely specific. It must be explicitly told to treat all `<Object>` tags (except Pikachu) as walls and to respect elevation rules (`ground` vs `elevated_ground` requires `steps`).
- **LESSON 14:** Prioritize direct game state information and personal observation over external guides or preconceived notions.
- **LESSON 15:** The elevated platform in the eastern part of Mt. Moon B2F, accessed via the steps at (29,8), is a confirmed dead end.
- **LESSON 16:** I must review my notes for a specific area *before* entering it to avoid repeating colossal wastes of time, like re-entering the B2F eastern dead-end loop.