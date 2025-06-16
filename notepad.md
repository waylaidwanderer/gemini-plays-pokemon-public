# Game Mechanics & Rules
- **Confusion:** Wears off after battle.
- **Defeated Trainers:** Act as impassable obstacles.

# Battle Mechanics
- **Move Selection:** The in-battle move list is a vertical menu navigated with **Up/Down ONLY**. Left/Right have no effect.

# Battle Notes
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras) or Grass/Poison (Oddish, Bellsprout).
- Flying is 4x effective vs. Bug/Grass (Paras).

# Team Strategy
- **SPIKE (Nidoran♂):** Evolve at Lv. 16 for an early power spike with Nidoking.

# Agent & Tool Notes
- **world_knowledge_manager_agent:** Agent is currently non-functional. **TOP PRIORITY:** Debug and fix this agent to ensure the World Knowledge Graph is kept up-to-date automatically.
- **geodude_battle_agent:** Automates battles with wild Geodude or Sandshrew. Switches to NIGHTSHADE and uses ABSORB. Logic is now fully corrected for active Pokémon and vertical move selection.
- **dungeon_pathfinder_agent:** This agent is reliable for single-map navigation and should be used to avoid manual navigation errors in complex areas.
- **Principle 4: Trust Your Markers.** Avoid re-interacting with NPCs or re-exploring areas already marked as complete or non-essential.

# Mt. Moon Navigation - CORRECTED
- **Goal:** Find the Super Nerd with the fossils to exit to Route 4.
- **Ladders Systems:** There are two distinct, unconnected ladder systems.
  - **Eastern System (Dead End):** 1F (18, 12) <-> B1F (26, 10) <-> B2F (26, 10). The ladder on B2F at (26, 10) is a **ONE-WAY trip UP**.
  - **Western System (Path to Fossils):** 1F (6, 6) <-> B1F (6, 6). This leads to the correct path forward.
- **Key NPCs & Obstacles:**
  - Super Nerd at (25, 32) on 1F is a non-battling NPC and a dead end.
  - Rocket at (30, 12) on B2F is not on the main progression path.

# Strategic Principles
- **Principle 1: Trust and Maintain Your Tools.** A `path_found: false` result likely means the World Knowledge Graph is incomplete or the path is truly blocked.
- **Principle 2: Explore Thoroughly.** Do not mark paths as dead ends until all connecting branches and warps are fully explored.
- **Principle 3: Adapt Quickly.** Do not fixate on incorrect hypotheses. The eastern part of B2F was a lesson in this.

- **B1F Western Platform:** This area is a winding maze of elevated platforms with numerous dead ends. Careful, systematic exploration is required.