# Strategic Principles & Lessons
- Defeated Trainers are impassable obstacles.
- Confusion wears off after battle.
- In-battle move list is a vertical menu (Up/Down only).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- When party resources (especially PP on key moves) are critically low, the top priority becomes a strategic retreat to heal.
- **Lesson from Mt. Moon:** Panicked navigation leads to repeated dead ends and wasted resources. Must be more systematic, trust my own notes and a reliable pathfinding agent, and carefully check the map for impassable terrain like elevated ground before moving.

# Battle Notes
- SPARKY's THUNDERSHOCK has plenty of PP. Incorrectly assuming it was out of PP was a major error.

# Agent & Tool Notes
- **`pathfinding_agent`:** Now reliable after multiple fixes. The key was explicitly telling it to treat 'elevated_ground' as impassable.
- **`geodude_battle_agent`:** Reliable for Geodude/Sandshrew encounters.
- **`battle_escape_agent`:** Reliable for fleeing.
- **PRIORITY TASK:** Create a `world_knowledge_manager_agent` to automate the process of adding nodes and edges to the World Knowledge Graph. This will prevent manual errors and save time.

# Past Campaigns
- **Mt. Moon Navigation:** The goal was to find a Super Nerd with fossils, but this was a flawed assumption. The main path was in the eastern section of 1F, looping around the central structures to exit. The western ladder system on 1F led to a large, looping dead-end area.