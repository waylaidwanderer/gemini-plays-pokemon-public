# Game Mechanics & Rules
- **Confusion:** Wears off after battle.
- **Defeated Trainers:** Act as impassable obstacles.

# Battle Notes
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras) or Grass/Poison (Oddish, Bellsprout).
- Flying is 4x effective vs. Bug/Grass (Paras).

# Team Strategy
- **SPIKE (Nidoran♂):** Evolve at Lv. 16 for an early power spike with Nidoking.

# Agent & Tool Notes
- `dungeon_navigator_agent`: Best for complex, multi-floor dungeons. Requires a complete World Knowledge Graph.
- `dungeon_pathfinder_agent`: Essential for safe, short-range paths within a single map.
- `battle_escape_agent`: Primary tool for running from non-essential wild battles.
- `geodude_battle_agent`: Automates switching to NIGHTSHADE and using ABSORB.

# Mt. Moon Navigation - CORRECTED
- **Goal:** Find the Super Nerd with the fossils to exit to Route 4.
- **Ladders Systems:** There are two distinct, unconnected ladder systems.
  - **Eastern System (Main Path to Dead End):**
    - 1F (18, 12) <-> B1F (26, 10). This ladder on B1F requires stepping on (18,11) and back to activate.
    - B1F (18, 12) <-> B2F (26, 10). **The ladder on B2F at (26, 10) is a ONE-WAY trip UP to B1F.** This area is a dead end.
  - **Western System (Path to Fossils):**
    - 1F (6, 6) <-> B1F (6, 6). Leads to the northwest section of B1F.
    - From B1F (NW section), another ladder leads to the western part of B2F, which is the correct path forward.
- **Key NPCs & Obstacles:**
  - Super Nerd at (25, 32) on 1F is a **non-battling NPC** and a dead end.
  - Rocket at (30, 12) on B2F blocks a side path in the eastern dead-end section. He is not on the main progression path.

# Strategic Principles
- **Principle 1: Trust and Maintain Your Tools.** A `path_found: false` result likely means the World Knowledge Graph is incomplete or the path is truly blocked.
- **Principle 2: Explore Thoroughly.** Do not mark paths as dead ends until all connecting branches and warps are fully explored.
- **Principle 3: Adapt Quickly.** Do not fixate on incorrect hypotheses. The eastern part of B2F was a lesson in this.