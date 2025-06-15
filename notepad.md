# Mt. Moon Navigation Notes

## Layout & Obstacles
- **1F Layout:** The first floor is a large, looping area. The direct path south from the central corridors is blocked by impassable ledges (`elevated_ground`).
- **Dead Ends:** The ladder at (18, 12) on 1F leads to a small, isolated, dead-end platform on B1F.
- **Impassable Trainers:** All defeated trainers encountered so far act as solid walls and must be navigated around.

## Strategy & Hypotheses
- **Current Strategy:** Systematic exploration of all reachable unseen tiles. The path forward is likely through an unexplored area, not a forced exit.
- **Hypothesis (Active):** The main path forward is through the eastern corridors of 1F, likely leading to the ladder at (26, 16).

# Battle Learnings

- **Type Matchups:**
  - Electric is NOT very effective vs. Bug/Grass (Paras).
  - Electric is NOT very effective vs. Grass/Poison (Oddish, Bellsprout).
- **Risk Management:** Do not switch in low-level, non-resistant Pokémon to weaken wild encounters. It's too risky.

# Agent Reliability

- **`master_pathfinder_agent`:** This agent is **UNRELIABLE** in Mt. Moon. It has failed multiple times (5+) by routing through impassable walls, up ledges, and getting stuck in loops. **Do not use for navigation on this map.** Manual navigation is required.