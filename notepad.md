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

# Active Hypotheses
- **Hypothesis 1:** Melanie won't give me the Bulbasaur yet. The dialogue is stuck in a loop even with a free party slot. Maybe another event, like the one on the northern bridge, must be completed first. (Status: Blocked)
- **Hypothesis 2:** The path to the Cerulean Gym is blocked until I complete the event at Bill's Cottage. (Status: Verified by AI hint)
- **Hypothesis 3:** Wild Pokémon of the same species may have different movesets. (Status: Unverified)

# Agent Log & Development
- **`unseen_tile_navigator_agent` & `pathfinder_agent`:** Refined to treat all `<Object>` tags (except Pikachu) as impassable walls and to correctly handle ledge traversal. (Status: Refined, needs testing on Pikachu rule)
- **`building_identifier_agent`:** Untested.
- **`battle_strategist_agent`:** Verified as reliable.
- **`battle_switch_agent`:** Verified as reliable.
- **`pikachu_path_adjuster_agent`:** Verified as reliable.
- **`pokedex_gap_analyzer_agent`:** Newly created. MUST test at next wild encounter.