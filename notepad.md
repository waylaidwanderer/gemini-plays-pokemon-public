# Strategic Principles
- Trust The Game State: The game state data (especially `reachable` flags) is the ultimate source of truth, even if it contradicts visual map memory.
- Systematic Navigation: Use wall-following or planned routes when agents fail.
- NPCs are Walls: NPCs are impassable obstacles.
- Two-Strikes Rule: If a path or interaction fails twice, re-evaluate.
- Resource Management: Strategic retreat to heal is a top priority when PP is critical.

# Game Mechanics & Battle Intel
- **Type Matchups:**
    - Grass is 4x effective vs. Rock/Ground (e.g., Geodude).
    - Electric-type moves are not very effective against Electric-type Pokémon (e.g., Pikachu vs. Voltorb).
- **Status Effects:** Confusion wears off after battle.
- **EXP Share:** Only Pokémon in the party when the final opponent faints receive EXP.

# Campaign Log & Hypotheses
- **Mt. Moon B2F East:** Blocked by a Rocket Grunt at (30, 12). Path is now clear after obtaining a fossil.
- **Hypothesis:** Defeated trainers may not be permanently impassable. (Status: Unverified)
- **Hypothesis:** Wild Pokémon of the same species may have different movesets. (Status: Unverified)

# Navigation Insights
- **Mt. Moon B2F West Platform:** I was stuck at (18, 18), believing a wall at (19, 18) was impassable. The game state's `reachable` flag was correct. The path forward is to move Down to (18, 19) and then Right. Trust the game state data over visual perception.

# Agent Development
- **`maze_solver_agent`:** This agent is fundamentally broken and unreliable for navigation after numerous failed refinements. It is officially benched. DO NOT USE until a completely new approach is developed.
- **`fossil_choice_advisor_agent`:** Verified as reliable.
- **Ideas:**
    - Universal Route Planner: Agent to find the shortest path between any two known points.
    - Catching Assistant: Agent to help weaken wild Pokémon for capture.