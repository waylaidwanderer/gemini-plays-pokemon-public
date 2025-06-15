# Agent Improvement Plan
- **Core Priority:** Agent refinement is a top priority. I must immediately use `define_agent` to fix flaws, especially regarding navigation on maps with verticality (`elevated_ground`, `steps`).

# Battle Learnings
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras), or Grass/Poison (Oddish, Bellsprout).
- Defensive immunities aren't everything; type coverage of offensive moves is key.

# Gameplay Mechanics & Rules
- **Dialogue Advancement:** A single 'A' press advances to the next dialogue box. Repeatedly pressing 'A' on static text re-initiates the conversation.
- **Defeated Trainers:** Defeated trainers in Mt. Moon act as impassable obstacles.
- **Trap Ladder:** The ladder at (26, 16) on 1F is a one-way trap.

# Agent Performance History
- **`pathfinder_agent` failures:** Failed to generate path on B1F (T6640), failed to path around `elevated_ground` on B2F (T6680).
- **`dungeon_path_analyzer_agent` failure:** Failed to respect elevation on B2F (T6708).