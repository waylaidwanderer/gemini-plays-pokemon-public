# Agent Improvement Plan
- **Core Priority:** Agent refinement is a top priority. I must immediately use `define_agent` to fix flaws, especially regarding navigation on maps with verticality (`elevated_ground`, `steps`).
- **`pathfinder_agent` Fix Details:** The system prompt needs a major overhaul. I will add explicit, pseudo-code-level instructions for its Python script: 
  1. When building the graph, iterate through every tile (u).
  2. For each neighbor (v) of tile (u), check for a valid connection.
  3. A connection is valid ONLY IF:
     - `u.type` is 'ground' and `v.type` is 'ground' OR 'steps'.
     - `u.type` is 'elevated_ground' and `v.type` is 'elevated_ground' OR 'steps'.
     - `u.type` is 'steps' and `v.type` is 'ground', 'elevated_ground', OR 'steps'.
  4. Any other combination (e.g., 'ground' to 'elevated_ground' directly) is an invalid path and no edge should be created.

# Battle Learnings
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras), or Grass/Poison (Oddish, Bellsprout).
- Defensive immunities aren't everything; type coverage of offensive moves is key.

# Gameplay Mechanics & Rules
- **Dialogue Advancement:** A single 'A' press advances to the next dialogue box. Repeatedly pressing 'A' on static text re-initiates the conversation. 'B' can sometimes dismiss dialogue without re-engaging.
- **Defeated Trainers:** Defeated trainers in Mt. Moon act as impassable obstacles.
- **Trap Ladder:** The ladder at (26, 16) on 1F is a one-way trap.

# Agent Performance History
- **`pathfinder_agent` failures:** Consistently fails to handle elevation changes on Mt. Moon B2F. It has been abandoned for this map until it is properly fixed.
- **`dungeon_path_analyzer_agent` failures:** Required multiple refinements to provide descriptive, useful output.