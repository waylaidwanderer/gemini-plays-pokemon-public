# Game Mechanics & Lessons

## Navigation
- **Corrected Hypothesis (Mt. Moon B2F Obstacle):** My repeated failures (3 attempts) to pass the Rocket Grunt at (16, 23) were due to a flawed exploration method. I was trying to walk *through* his sprite. The critique suggests the blockage is an invisible wall on an *adjacent* tile. **New Plan:** After healing, I must return to B2F and systematically test *all* tiles surrounding the grunt (left, right, above, below) to find the correct path. I will not assume a path is a dead end until all adjacent tiles are tested.
## Agent Development & Tactics
- **Pathfinder Agent Correction:** The update to the `master_pathfinder_agent` was based on the flawed assumption about defeated trainers. This change must be reverted. The agent should NOT treat defeated trainers as obstacles until this mechanic is proven with certainty.
- Battle tactics need to be more proactive. I will not wait until a Pokémon's HP is critical before using priority moves like Quick Attack.

## Battle Notes
- If running from a wild battle fails more than twice, it is more efficient to defeat the opponent (e.g., failed to run from Geodude 3 times in Mt. Moon).

## Battle Tactics & Analysis
- **Miscalculation vs. Paras (Mt. Moon B1F):** I underestimated the damage from a Lv. 11 Paras's Absorb. Switching in FURYFIST (Lv. 8) was too risky; it was brought to critical HP in a single turn. A bulkier Pokémon or a faster switch strategy is needed for weakening wild encounters.
- **Inefficient Menu Navigation:** My menuing to switch Pokémon against the Paras was clumsy and slow. I need to be more precise with my button presses (e.g., Down vs. Right) to avoid wasted turns.