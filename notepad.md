# Game & Battle Mechanics
- Defeated Trainers are impassable obstacles.
- Confusion wears off after battle.
- In-battle move list is a vertical menu (Up/Down only).

# Battle Notes
- Grass is 4x effective vs. Rock/Ground (Geodude).
- SPARKY's THUNDERSHOCK is out of PP.

# Agent & Tool Notes
- **world_knowledge_manager_agent:** Unreliable. Redefined to ONLY add the source node. Destination node and edge must be added manually.
- **geodude_battle_agent:** Reliable for Geodude/Sandshrew encounters.
- **battle_escape_agent:** Reliable for fleeing.
- **dungeon_pathfinder_agent:** Unreliable on complex maps (Mt. Moon B2F), but may work on simpler ones (Mt. Moon B1F).

# Mt. Moon Navigation
- **Goal:** Find Super Nerd with fossils to exit to Route 4.
- The western ladder system on 1F leads to a large, looping dead-end area. The main path is in the eastern section of the cave.

# Strategic Principles
- Adapt quickly; don't repeat failed actions or trust faulty tools.
- Explore systematically. The simplest path is often correct.

- **Mt. Moon B2F:** The northern elevated platform accessible from the western ladder system is a dead end.

- **New Principle:** When party resources (especially PP on key moves) are critically low, the top priority becomes a strategic retreat to heal. Do not push deeper into a dangerous area in a weakened state.

# Gameplay Lessons
- Critique T9841: Panicked navigation leads to repeated dead ends. Must be more systematic, trust my own notes (e.g., 'main path is east'), and carefully check the map for impassable terrain like elevated ground before moving.