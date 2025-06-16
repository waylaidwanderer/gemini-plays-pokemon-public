# Game & Battle Mechanics
- **Defeated Trainers:** Act as impassable obstacles.
- **Confusion:** Wears off after battle.
- **Move Selection:** The in-battle move list is a vertical menu navigated with **Up/Down ONLY**.

# Battle Notes
- Grass is 4x effective vs. Rock/Ground (Geodude).

# Agent & Tool Notes
- **world_knowledge_manager_agent:** Agent has been updated to correctly add nodes after a map transition. It does not add edges, which must be done manually after the node IDs are generated.
- **geodude_battle_agent:** Fully reliable for Geodude/Sandshrew encounters.
- **battle_escape_agent:** Works perfectly. Use to flee non-essential wild battles.
- **dungeon_pathfinder_agent:** **UNRELIABLE** on complex maps like Mt. Moon B2F. It has provided multiple incorrect paths. Do not use on this map.

# Mt. Moon Navigation
- **Goal:** Find the Super Nerd with the fossils to exit to Route 4.
- The path forward is on the main ground level, not the isolated side platforms.

# Strategic Principles
- **Principle 1: Don't Trust Faulty Tools.** If an agent or tool repeatedly fails, abandon it and switch to a manual, systematic approach.
- **Principle 2: Explore Systematically.** Clear main paths before exploring side areas. The simplest path is often correct.
- **Principle 3: Adapt Quickly.** Do not fixate on incorrect hypotheses or repeat failed actions.