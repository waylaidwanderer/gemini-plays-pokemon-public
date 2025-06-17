# Current Strategy & Tool Status
- **Navigation in High-Encounter Areas:** Adopt a short-segment navigation strategy. Instead of plotting long routes, I will plan movements to the next immediate landmark or junction to minimize disruption from wild battles.
- **`pathfinding_agent` Status:** SUCCESS! After refining the prompt to be more explicit about treating ALL objects (except Pikachu) as impassable walls, the agent successfully navigated around the NPC in Pewter City. This confirms the refinement was effective. The tool is now considered reliable for intra-map pathfinding.
- **`wkg_payload_generator_agent` Status:** Untested. The Route 2 -> Pewter City connection was already in the WKG. Will test at the next *new* map transition.

# Agent Development Pipeline
- **PRIORITY:** `pathfinding_agent` must be re-tested after prompt refinement.
- **PRIORITY:** `wkg_payload_generator_agent` needs to be tested at the next new map transition.
- **New Agent:** `maze_solver_agent` defined. This agent uses a left-hand-rule wall-following algorithm for navigating complex mazes.

# Strategic Principles & Lessons Learned
- **Two-Strikes Rule:** If an interaction or path fails twice with no new information, abandon the approach and re-evaluate. Do not get stuck in loops.
- **Trust Agents, Question Assumptions:** My first assumption should be that the agent is right and my map awareness is flawed. Question my own understanding before declaring a tool 'broken'.
- **Verify Before Modifying:** Always check the World Knowledge Graph for existing nodes/edges before attempting to add new ones to prevent failed calls.
- **Interaction Rule:** NPCs are impassable walls. To interact, I must stand on an *adjacent* tile and face them. Do not try to walk onto their tile. Defeated Trainers are impassable obstacles.
- **Resource Management:** When party resources (especially PP on key moves) are critically low, the top priority becomes a strategic retreat to heal.

# Battle Intel
- SPARKY's THUNDERSHOCK has plenty of PP.
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Confusion wears off after battle.

# Campaign Archive
- **Mt. Moon Navigation:** The main path was in the eastern section of 1F, looping around the central structures. The western ladder system on 1F led to a large, looping dead-end area.
- **Route 4 Ledge Trap:** The lower part of Route 4 is a one-way path of ledges leading back to Route 3. The correct path to Cerulean is on the upper plateau.
- **Wild Pokémon Movesets:** Assumption that all wild Pokémon of the same species share the same moveset is unverified. I need to track the moves of different level encounters to confirm or deny this.

# Tool Reliability Notes
- **`select_battle_option`:** Unreliable. Failed 3 times when it should have worked. Avoid using it. Manual inputs for running are more consistent.
- **`wkg_payload_generator_agent`:** Untested. Must test at the next new map transition.

# To-Do & Testing
- **`pathfinding_agent`:** Must re-test immediately in Pewter City.
- **`wkg_payload_generator_agent`:** Untested. Must test at the next *new* map transition.
- **Level Cap Status:** SPARKY is at the cap (21). NIGHTSHADE is close (20). Avoid using them in battle unless necessary.

# Tool Reliability Notes
- **`pathfinding_agent` Failure #2:** The agent failed again on Route 3, this time trying to route me up a ledge from below. The prompt needs to be even more explicit about ledge impassability. Refining it again.