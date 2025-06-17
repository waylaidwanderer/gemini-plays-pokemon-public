# Strategic Principles
- Trust The Game State: The game state data (especially `reachable` flags) is the ultimate source of truth, even if it contradicts visual map memory or my own perception. A path always exists to a reachable tile.
- Systematic Navigation: When agents fail, use methodical manual navigation. Test all adjacent tiles if seemingly blocked.
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
- **Mt. Moon B2F East:** Path is blocked by a Rocket Grunt at (30, 12) who is an item gate for a fossil. Now that I have the Dome Fossil, he should let me pass.
- **Hypothesis:** Wild Pokémon of the same species may have different movesets. (Status: Unverified)

# Navigation Insights
- **Mt. Moon B2F West Platform:** I was stuck at (18, 18), believing a wall at (19, 18) was impassable because I failed to check the tile below me. The game state's `reachable` flag was correct. The path forward was to move Down to (18, 19) and then Right. Lesson learned: trust the game state data and explore all adjacent tiles before concluding I'm trapped.

# Agent Development
- **`maze_solver_agent`:** This agent is fundamentally broken and has been officially benched. It repeatedly failed to generate valid paths, especially around Pikachu, even after multiple hyper-specific refinements. DO NOT USE for navigation until a completely new development approach is considered.
- **`fossil_choice_advisor_agent`:** Verified as reliable.
- **Agent Ideas:**
    - Universal Route Planner: Agent to find the shortest path between any two known points across multiple maps.
    - Catching Assistant: Agent to help weaken wild Pokémon for capture.
    - `pikachu_path_adjuster_agent`: A modular agent that takes a generated path and inserts the correct extra button presses needed to navigate around Pikachu. This might be more reliable than one monolithic agent.