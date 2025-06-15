# Strategic Lessons Learned
- **Soft-Locks Are Real:** Getting trapped in a one-way path without an Escape Rope is a soft-lock. The 'never stuck' rule doesn't apply to strategic errors. Accept the situation and reset.
- **Escape Ropes are MANDATORY:** Always carry at least one Escape Rope when entering a new dungeon, especially one with confirmed one-way paths.

# Agent Improvement Plan
- **Core Priority:** Agent refinement is a top priority. I must immediately use `define_agent` to fix flaws, especially regarding navigation on maps with verticality (`elevated_ground`, `steps`).

# Battle Notes
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras), or Grass/Poison (Oddish, Bellsprout).

# Dungeon Notes & Traps
- **Mt. Moon 1F:** The ladder at (26, 16) is a one-way trap leading to a different part of 1F.
- **Mt. Moon B1F:** The ladder at (18, 12) is a one-way trap from B2F. Entering it results in a soft-lock if you have no Escape Rope.

# Game Mechanics
- **Dialogue:** A single 'A' press advances to the next dialogue box. 'B' can dismiss dialogue.
- **Defeated Trainers:** Some defeated trainers act as impassable obstacles.

- **Elevation Rule:** Discovered that direct movement between adjacent 'ground' and 'elevated_ground' tiles is possible. This was the key to escaping the Mt. Moon B1F 'trap'.