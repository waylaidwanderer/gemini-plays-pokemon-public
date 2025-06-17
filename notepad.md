# Strategic Principles
- Trust The Game State: The game state data (`reachable` flags, etc.) is the ultimate source of truth.
- Systematic Navigation: Use agents for complex paths; use short, verifiable moves for simple repositions.
- NPCs are Walls: Treat all non-player sprites (except Pikachu) as impassable obstacles.
- Two-Strikes Rule: If a path or interaction fails twice, re-evaluate assumptions before trying a third time.
- Mark Defeated Trainers: Immediately mark any defeated trainer with a '☠️' emoji to avoid re-engaging.

# Game Mechanics & Battle Intel
- **Type Matchups (Verified):**
    - Grass is 4x effective vs. Rock/Ground (e.g., Geodude).
    - Electric-type moves are 'not very effective' against Electric-type Pokémon.
    - Electric-type moves are 'not very effective' against Paras (Bug/Grass).
- **Status Effects:**
    - Confusion wears off after battle.
    - Poison-type Pokémon are immune to being poisoned.
- **EXP Share:** Only Pokémon in the party when the final opponent faints receive EXP.
- **Level Cap EXP Gain:** Pokémon at the level cap do not gain EXP, even if the message appears.

# Current Hypotheses
- **Hypothesis 1:** A full party is preventing me from receiving the Bulbasaur from Melanie. (Status: Testing)
- **Hypothesis 2:** The path to the Cerulean Gym is blocked until I complete an event on a bridge to the north. (Status: Unverified, from AI hint)
- **Hypothesis 3:** Wild Pokémon of the same species may have different movesets. (Status: Unverified)

# Agent Development & Testing
- **`pathfinder_agent`:** Refined to treat all `<Object>` tags (except Pikachu) as impassable walls. This should improve its accuracy in cluttered areas. (Status: Refined, needs testing)
- **`building_identifier_agent`:** Newly created to find key buildings in cities. (Status: Untested)
- **`unseen_tile_navigator_agent`:** Verified as reliable.
- **`battle_strategist_agent`:** Verified as reliable.
- **`battle_switch_agent`:** Verified as reliable.
- **`pikachu_path_adjuster_agent`:** Verified as reliable.

# Agent Ideas
- `pokedex_gap_analyzer_agent`: Could analyze my current roster and suggest high-value Pokémon to catch in a new area to improve type coverage.