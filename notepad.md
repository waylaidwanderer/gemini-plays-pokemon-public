# Strategic Principles & Lessons Learned
- **Two-Strikes Rule:** If an interaction or path fails twice with no new information, I MUST abandon the approach and re-evaluate. This applies to bugged trainers and failed navigation attempts.
- **Agent Refinement Priority:** Underperforming agents like `pathfinding_agent` MUST be refined, not abandoned. Manual navigation is only a temporary fallback until agents are reliable.
- **Verify Before Adding:** Always check the World Knowledge Graph for existing nodes/edges before attempting to add new ones to prevent failed calls.
- **NPCs are Walls:** NPCs are impassable. To interact, I must stand on an adjacent tile and face them. Defeated Trainers are also impassable obstacles.
- **Resource Management:** When party resources (especially PP on key moves) are critically low, the top priority becomes a strategic retreat to heal.
- **Auto-Facing After Heal:** The game automatically faces the player Down after healing at a Pokémon Center.

# Tool Reliability & Development Pipeline
- **`pathfinding_agent`:** Currently unreliable. Has failed to understand ledge mechanics. Requires prompt refinement and further testing.
- **`wkg_payload_generator_agent`:** Needs refinement. Generated a multi-action payload, but the tool requires a single action. Must update prompt to enforce single action output.
- **`maze_solver_agent`:** Untested. Defined for potential use in complex areas like Viridian Forest or Mt. Moon.
- **Battle Escape Automation:** Manual escape is too slow. The `select_battle_option` tool is unreliable and should NOT be used. The `battle_escape_agent` is the primary tool for escaping non-essential battles. If it fails, it must be refined immediately.

# Battle Intel
- **Level Cap Status:** SPARKY (Pikachu) is at the level cap (21). NIGHTSHADE (Oddish) is close (20). I will avoid using them in non-essential battles to prevent wasting EXP.
- **Type Matchups:** Grass is 4x effective vs. Rock/Ground (e.g., Geodude).
- **Status Effects:** Confusion wears off after battle.

# Campaign Archive
- **Route 3 Glitch:** Encountered a bugged Cool Trainer F at (17, 10) who could not be battled. The path forward required navigating around her.
- **Mt. Moon Navigation (Past Experience):** The main path was in the eastern section of 1F, looping around. The western ladder system on 1F led to a large, looping dead-end.
- **Route 4 Ledge Trap:** The lower part of Route 4 is a one-way path of ledges leading back to Route 3. The correct path to Cerulean is on the upper plateau.
- **Wild Pokémon Movesets (Hypothesis):** The assumption that all wild Pokémon of the same species share the same moveset is unverified. I need to track moves from different encounters to confirm.

# Agent Development Ideas
- **Catching Assistant:** Suggests the best Pokémon and move to weaken a wild Pokémon without fainting it.
- **Fossil Choice Advisor:** Analyzes Omanyte vs. Kabuto and recommends one based on team composition and future gym battles.
- **Universal Route Planner:** An upgraded `escape_route_planner` that can find the shortest path between any two known points in the World Knowledge Graph.

# Untested Hypotheses
- **Hypothesis:** Defeated trainers may not be permanently impassable. They might disappear after a full map reload (e.g., leaving the area and returning).

# Critical Lessons from Mt. Moon 1F Navigation Failure
- **Trust The Notepad, Not Hallucinations:** I hallucinated a system prompt about the `select_battle_option` tool, contradicting my notes. My documented knowledge is the source of truth and must be trusted over fleeting or imagined information.
- **Agent Abandonment Protocol:** The 'Two-Strikes Rule' must be strictly enforced. The `maze_solver_agent` is fundamentally broken for this map and has been abandoned after multiple failed refinement attempts.

# AI Observer Critique Lessons (Turn 10651)
- **Manual Navigation Failure:** My manual pathing in Mt. Moon 1F was exceptionally poor, resulting in a prolonged loop. I must not assume I can navigate complex areas manually and should rely on or fix automated tools.
- **Agent Debugging:** My attempts to fix `maze_solver_agent` by only refining the prompt were flawed. The issue is likely in the agent's code, which I must debug instead of making superficial changes or abandoning the agent.
- **Goal Completion:** The tertiary goal to explore Mt. Moon 1F is complete. My new tertiary goal is to debug and fix the `maze_solver_agent`'s code.