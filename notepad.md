# Strategic Principles
- Trust The Game State: The game state data (especially `reachable` flags) is the ultimate source of truth.
- Systematic Navigation: Use agents for complex paths; use short, verifiable moves for simple repositions.
- NPCs are Walls: NPCs are impassable obstacles.
- Two-Strikes Rule: If a path or interaction fails twice, re-evaluate assumptions before trying a third time.

# Game Mechanics & Battle Intel
- **Type Matchups (Verified):**
    - Grass is 4x effective vs. Rock/Ground (e.g., Geodude).
    - Electric-type moves are 'not very effective' against Electric-type Pokémon (e.g., Pikachu vs. Voltorb).
    - Electric-type moves (THUNDERPUNCH) are 'not very effective' against Paras (Bug/Grass).
- **Status Effects:**
    - Confusion wears off after battle.
    - Poison-type Pokémon appear to be immune to being poisoned.
- **EXP Share:** Only Pokémon in the party when the final opponent faints receive EXP.
- **Level Cap EXP Gain:** Confirmed that Pokémon at the level cap do not gain EXP, even if the message appears.

# Battle Strategy Insights
- **Paralysis Strategy:** When a lead Pokémon is paralyzed, its Speed is severely reduced. Attempting to run is highly likely to fail and wastes turns. It is more efficient to fight immediately. (Insight from AI critique, T11016)

# Campaign Log & Hypotheses
- **Hypothesis:** Wild Pokémon of the same species may have different movesets. (Status: Unverified)

# Agent Development & Testing
- **`maze_solver_agent`:** Deleted. Fundamentally broken.
- **`fossil_choice_advisor_agent`:** Verified as reliable.
- **`unseen_tile_navigator_agent`:** Verified as reliable for pathfinding to unseen tiles.
- **`battle_strategist_agent`:** Verified as reliable for single-opponent battles.
- **`battle_switch_agent`:** Verified as reliable.
- **`pikachu_path_adjuster_agent`:** Created to handle Pikachu's movement. **Status: Untested.** Must be tested on a simple path soon.