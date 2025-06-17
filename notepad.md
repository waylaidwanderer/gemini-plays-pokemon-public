# Strategic Principles & Lessons Learned
- **Two-Strikes Rule:** If an interaction or path fails twice with no new information, I MUST abandon the approach and re-evaluate. This applies to bugged trainers and failed navigation attempts.
- **Manual Navigation First:** My `pathfinding_agent` is broken. I will rely on careful manual map study for all navigation.
- **Verify Before Adding:** Always check the World Knowledge Graph for existing nodes/edges before attempting to add new ones to prevent failed calls.
- **NPCs are Walls:** NPCs are impassable. To interact, I must stand on an adjacent tile and face them. Defeated Trainers are also impassable obstacles.
- **Resource Management:** When party resources (especially PP on key moves) are critically low, the top priority becomes a strategic retreat to heal.
- **Auto-Facing After Heal:** The game automatically faces the player Down after healing at a Pokémon Center.

# Tool Reliability & Development Pipeline
- **`pathfinding_agent`:** CRITICALLY UNRELIABLE - DO NOT USE. It has repeatedly failed to understand basic ledge mechanics despite multiple prompt refinements. It is benched until a fundamental overhaul is possible.
- **`wkg_payload_generator_agent`:** Untested. Must be tested at the next *new* map transition.
- **`maze_solver_agent`:** Untested. Defined for potential use in complex areas like Viridian Forest or Mt. Moon.
- **`select_battle_option`:** Unreliable. Failed multiple times. Manual inputs are more consistent.

# Battle Intel
- **Level Cap Status:** SPARKY (Pikachu) is at the level cap (21). NIGHTSHADE (Oddish) is close (20). I will avoid using them in non-essential battles to prevent wasting EXP.
- **Type Matchups:** Grass is 4x effective vs. Rock/Ground (e.g., Geodude).
- **Status Effects:** Confusion wears off after battle.

# Campaign Archive
- **Route 3 Glitch:** Encountered a bugged Cool Trainer F at (17, 10) who could not be battled. The path forward required navigating around her.
- **Mt. Moon Navigation (Past Experience):** The main path was in the eastern section of 1F, looping around. The western ladder system on 1F led to a large, looping dead-end.
- **Route 4 Ledge Trap:** The lower part of Route 4 is a one-way path of ledges leading back to Route 3. The correct path to Cerulean is on the upper plateau.
- **Wild Pokémon Movesets (Hypothesis):** The assumption that all wild Pokémon of the same species share the same moveset is unverified. I need to track moves from different encounters to confirm.