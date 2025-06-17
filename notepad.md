# Strategic Principles
- Trust The Game State: The game state data (especially `reachable` flags) is the ultimate source of truth. A path always exists to a reachable tile.
- Systematic Navigation: When agents or long paths fail, use methodical, short, verifiable movements.
- NPCs are Walls: NPCs are impassable obstacles.
- Two-Strikes Rule: If a path or interaction fails twice, re-evaluate assumptions before trying a third time.

# Game Mechanics & Battle Intel
- **Type Matchups:**
    - Grass is 4x effective vs. Rock/Ground (e.g., Geodude).
    - Electric-type moves are not very effective against Electric-type Pokémon (e.g., Pikachu vs. Voltorb).
- **Status Effects:**
    - Confusion wears off after battle.
    - Poison-type Pokémon appear to be immune to being poisoned (Verified: 1, Paras's Poison Powder failed on Zubat).
- **EXP Share:** Only Pokémon in the party when the final opponent faints receive EXP.

# Campaign Log & Hypotheses
- **Hypothesis:** Wild Pokémon of the same species may have different movesets. (Status: Unverified)

# Navigation Insights & Failures
- **Mt. Moon B2F West Platform:** I was stuck at (18, 18) for dozens of turns, repeatedly failing to navigate. I wrongly assumed I could move through walls and made multiple invalid path plans. Lesson learned: When stuck, stop and analyze the map carefully. Use short, verifiable moves instead of long, error-prone ones.
- **BFS Pathfinding Failure:** My `run_code` attempt at a BFS pathfinder failed because the code did not correctly parse the map's traversable areas and account for isolated platforms.

# Agent Development
- **`maze_solver_agent`:** Benched. Fundamentally broken.
- **`fossil_choice_advisor_agent`:** Verified as reliable.
- **`pikachu_path_adjuster_agent`:** Created to handle Pikachu's movement. Must be tested on simple paths first.
- **`unseen_tile_navigator_agent`:** Created to find paths to the nearest unseen tile, aiding systematic exploration.

- **Type Matchups (New Finding):** Electric-type moves (THUNDERPUNCH) are 'not very effective' against Paras (Bug/Grass). This suggests a change in the type chart.