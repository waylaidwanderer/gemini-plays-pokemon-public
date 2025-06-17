# Strategic Principles & Lessons Learned
- **Trust The Notepad:** My documented knowledge (notepad, markers) is the source of truth and must be trusted over fleeting or imagined information, like hallucinated system prompts.
- **Systematic Navigation:** When automated tools fail, I must adopt a systematic approach (e.g., wall-following) and perform careful, long-range planning. Haphazard manual navigation leads to loops.
- **Separate Development from Progression:** Agent debugging is a strategic task for safe locations (like a Pokémon Center), not to be prioritized while lost in a hostile area.
- **NPCs are Walls:** NPCs, including defeated Trainers, are impassable. To interact, stand on an adjacent tile and face them.
- **Two-Strikes Rule:** If a path or interaction fails twice with no new info, abandon the approach and re-evaluate.
- **Resource Management:** When party resources (PP) are critically low, the top priority is a strategic retreat to heal.

# Tool & Agent Development
- **`select_battle_option` Tool:** Verified as 100% reliable for battle actions like 'RUN'. This is now the primary method for escaping non-essential encounters.
- **`maze_solver_agent`:** Now reliable after extensive debugging. Its debugging protocol (printing the map grid on failure) was key to fixing it.
- **`battle_escape_agent`:** DEPRECATED. `select_battle_option` is superior.
- **Development Idea - Universal Route Planner:** An agent to find the shortest path between any two known points in the World Knowledge Graph. Would be a major upgrade to the `escape_route_planner_agent`.
- **Development Idea - Catching Assistant:** An agent to suggest the best Pokémon and move to weaken a wild Pokémon for capture without fainting it.
- **Development Idea - Fossil Choice Advisor:** An agent to analyze Omanyte vs. Kabuto and recommend one based on team composition and future gym battles. (Agent already defined).

# Battle Intel
- **Level Cap Status:** SPARKY (Pikachu) is at the level cap (21). NIGHTSHADE (Oddish) is close (20). Avoid using them in non-essential battles to prevent wasting EXP.
- **Type Matchups:** Grass is 4x effective vs. Rock/Ground (e.g., Geodude).
- **Status Effects:** Confusion wears off after battle.

# Campaign Archive & Untested Hypotheses
- **Route 3 Glitch:** A bugged Cool Trainer F at (17, 10) could not be battled.
- **Mt. Moon B2F East:** Blocked by a Rocket Grunt demanding a fossil. This area is a dead end until a fossil is acquired.
- **Hypothesis:** Defeated trainers may not be permanently impassable. They might disappear after a full map reload (e.g., leaving the area and returning).
- **Hypothesis:** The assumption that all wild Pokémon of the same species share the same moveset is unverified. I need to track moves from different encounters to confirm.