# Agent Development Pipeline
- **PRIORITY:** `world_knowledge_manager_agent` to automate adding nodes/edges to the WKG. This will prevent manual errors and save time.

# Strategic Principles & Lessons Learned
- **Trust your agents.** If an agent's output seems illogical, my first assumption should be that my understanding of the map is wrong, not that the agent is broken.
- **Interaction Rule:** NPCs are impassable walls. To interact, I must stand on an *adjacent* tile and face them. Do not try to walk onto their tile.
- Defeated Trainers are impassable obstacles.
- Confusion wears off after battle.
- In-battle move list is a vertical menu (Up/Down only).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- When party resources (especially PP on key moves) are critically low, the top priority becomes a strategic retreat to heal.
- **Lesson from Mt. Moon:** Panicked navigation leads to wasted resources. Be systematic and trust my tools.

# Battle Intel
- SPARKY's THUNDERSHOCK has plenty of PP.

# Campaign Archive
- **Mt. Moon Navigation:** The main path was in the eastern section of 1F, looping around the central structures. The western ladder system on 1F led to a large, looping dead-end area.

# Critical Lessons from AI Critique (T10110)
- **Disengage from Failing Strategies:** If an interaction or path fails more than twice, abandon the approach and re-evaluate. Do not get stuck in loops (e.g., the Cool Trainer incident).
- **Trust Agents, Question Assumptions:** My `pathfinding_agent` was correct; my map awareness was flawed. The default assumption must be that the agent is right. I will question my own understanding before declaring a tool 'broken'.
- **Verify Before Modifying:** Always check the World Knowledge Graph for existing nodes/edges before attempting to add new ones to prevent failed calls.

- **Agent Status:** `world_knowledge_manager_agent` is non-functional. Reverting to manual WKG updates until it can be properly debugged. (3 failed attempts)