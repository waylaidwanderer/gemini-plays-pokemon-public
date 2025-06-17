# Strategic Principles
- Trust The Notepad: My documented knowledge is the source of truth.
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

# Agent Development
- **`maze_solver_agent`:** Fixing this agent is my top priority. It fails to correctly implement the Pikachu movement rule. I need to refine its prompt to be more explicit about the required Python logic.
- **`fossil_choice_advisor_agent`:** Verified as reliable.
- **Ideas:**
    - Universal Route Planner: Agent to find the shortest path between any two known points.
    - Catching Assistant: Agent to help weaken wild Pokémon for capture.