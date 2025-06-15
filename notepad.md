# Mt. Moon Navigation Notes

## Strategy & Hypotheses
- **Current Strategy:** Systematic exploration of all reachable unseen tiles. My previous 'escape' strategy was a failure. The path forward is likely through an unexplored area, not a forced exit.
- **Hypothesis (Active):** The main path forward is through the eastern corridors of 1F, likely leading to the ladder at (26, 16).

# Battle Learnings

- **Type Matchups:**
  - Electric is NOT very effective vs. Bug/Grass (Paras).
  - Electric is NOT very effective vs. Grass/Poison (Oddish, Bellsprout).
- **Risk Management:** Do not switch in low-level, non-resistant Pokémon to weaken wild encounters. It's too risky.

# Agent Reliability

- **`master_pathfinder_agent`:** This agent is **UNRELIABLE** in Mt. Moon. It has failed multiple times (5+) by routing through impassable walls and up ledges. **Do not use for navigation on this map.** Manual navigation is required.