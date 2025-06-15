# Mt. Moon Navigation Notes

## Strategy & Hypotheses
- **Current Strategy:** Systematic exploration of the western corridors of 1F. My previous attempts at random exploration and trying to force an exit have failed. The path forward is likely through an unexplored area.
- **Hypothesis (Active):** The main path forward is through the northwest section of the cave, likely leading to the ladder at (18, 12).
- **Hypothesis (Disproven):** The eastern corridors do not lead to the main exit; they are a dead end with items.

# Battle Learnings

- **Type Matchups:**
  - Electric is NOT very effective vs. Bug/Grass (Paras).
  - Electric is NOT very effective vs. Grass/Poison (Oddish, Bellsprout).
- **Risk Management:** Do not switch in low-level, non-resistant Pokémon to weaken wild encounters. It's too risky.

# Agent Reliability

- **`master_pathfinder_agent`:** This agent is **UNRELIABLE** in Mt. Moon. It has failed multiple times (5+) by routing through impassable walls and up ledges. **Do not use for long-distance navigation on this map.** Manual navigation is required.

# Dungeon Mechanics Update
- **Defeated Trainers:** Unlike on Route 3, the defeated Rocket Grunt on Mt. Moon B2F at (16, 23) was *not* an impassable obstacle. I was able to walk right through his tile. This is a critical difference for dungeon navigation!