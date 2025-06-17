# Current Strategy & Tool Status
- **Navigation in High-Encounter Areas:** Adopt a short-segment navigation strategy. Instead of plotting long routes, I will plan movements to the next immediate landmark or junction to minimize disruption from wild battles.
- **`pathfinding_agent` Status:** FAILED. The agent provided a path that goes directly through an NPC at (18, 26) in Pewter City, despite its prompt instructing it to treat NPCs as impassable walls. This is the second major failure. I am refining its prompt to be more explicit about handling objects. If it fails again, I will have to consider a more robust solution.
- **`wkg_payload_generator_agent`:** Untested. The Route 2 -> Pewter City connection was already in the WKG. Will test at the next *new* map transition.
- **`pathfinding_agent`:** Refined prompt. Must re-test immediately on Pewter City map.
- **`world_knowledge_manager_agent` Status:** Deleted. The agent was non-functional and overly complex. Reverting to manual WKG updates using the simpler `wkg_payload_generator_agent`.

# Agent Development Pipeline
- **PRIORITY:** `wkg_payload_generator_agent` needs to be tested at the next map transition.
- **Idea:** `maze_solver_agent` that uses a simple wall-following algorithm for complex mazes like this forest.

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
- **`wkg_payload_generator_agent`:** Untested. Must test at the next *new* map transition (VF Gate to Rte 2 was already known).
- **Level Cap Status:** SPARKY is at the cap (21). NIGHTSHADE is close (20). Avoid using them in battle unless necessary.