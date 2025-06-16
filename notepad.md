# Game Mechanics & Rules
- **Battle-Warps:** Specific tiles can trigger a wild battle that also teleports the player. Location: Mt. Moon B2F (29, 9) -> B1F (21, 12). HIGHLY UNRELIABLE.

- **Confusion:** Wears off after battle.
- **Defeated Trainers:** Some become impassable obstacles.
- **Elevation Rule:** Movement between `ground` and `elevated_ground` requires a `steps` tile.
- **Item-Gated NPCs:** Some NPCs block paths and require a specific item to let you pass. Ex: Rocket at Mt. Moon B2F (30, 12) requires a fossil.

# Battle Notes & Movesets
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras) or Grass/Poison (Oddish, Bellsprout).

# Area Notes & Navigation
- **Mt. Moon:** Contains multiple, non-connected sections on its lower floors, accessible only via specific ladders on 1F. Some ladders are intentionally misleading and lead to dead-end loops.

# Defeated Trainers Log
- **Mt. Moon 1F:** Hiker (6, 7), Youngster (8, 23), Lass (17, 25), Super Nerd (25, 30), Lass (31, 7), Youngster (13, 17), Youngster (31, 28), Bug Catcher (32, 27)
- **Mt. Moon B2F:** Rocket Grunt (16, 23), Rocket Grunt (30, 8)

# Critical Lessons Learned
- **LESSON 1:** Do not fixate on NPCs as impassable walls. Always check for open paths around them. My assumption that the Rocket at (30, 12) blocked the entire corridor cost me over 50 turns.
- **LESSON 2 (Corrected):** Do not mark paths as 'dead ends' until all branches from that path are fully explored. My incorrect assumption about the ladder at (18, 12) on Mt. Moon 1F caused a massive, unnecessary backtrack.
- **LESSON 3:** The battle-warp at (29, 9) on Mt. Moon B2F is completely unreliable and must be avoided as a progression strategy.
- **LESSON 4:** If a path quickly seems to be a dead end, backtrack immediately and check for alternative entrances on the previous map. Some paths are intentionally misleading loops.
- **LESSON 5:** Trust the `pathfinding_agent`. A `path_found: false` result is not a tool failure; it is definitive proof that the target is unreachable from the current location.

# Agent & Tool Notes
- The `pathfinding_agent` is reliable for on-map navigation.
- The `healing_spot_finder_agent` is reliable for multi-map pathfinding to Pokémon Centers.
- The `battle_switch_agent` is reliable, but its logic needs to be verified with new menu layouts.

# Evolution Plans
- **SPIKE (Nidoran♂):** Evolve at Lv. 16 for early power spike (Nidoking). Misses Thrash, but has great TM potential.

# Post-Critique Strategy Updates
- **LESSON 6:** Do not attempt to train low-level Pokémon in high-risk areas like Mt. Moon. This is inefficient and dangerous. Use the `optimal_training_spot_agent` to find safe and effective training locations before dedicating time to training.
- **LESSON 7:** When a specific action or approach fails repeatedly (e.g., using a warp), do not get stuck in a loop. Test alternative hypotheses and directions immediately. Rigid problem-solving is a waste of time.