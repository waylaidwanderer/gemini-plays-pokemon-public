# Game Mechanics & Lessons

## Navigation
- **Defeated trainer sprites ARE impassable obstacles in this ROM hack.** This has been verified after being blocked by the Rocket Grunt in Mt. Moon B2F at (16, 23) from multiple angles. The previous assumption that they were passable was incorrect.

## Agent Development & Tactics
- The `master_pathfinder_agent` has been updated to treat defeated trainers as obstacles.
- Battle tactics need to be more proactive. I will not wait until a Pokémon's HP is critical before using priority moves like Quick Attack.

## Battle Notes
- If running from a wild battle fails more than twice, it is more efficient to defeat the opponent (e.g., failed to run from Geodude 3 times in Mt. Moon).

## Battle Tactics & Analysis
- **Miscalculation vs. Paras (Mt. Moon B1F):** I underestimated the damage from a Lv. 11 Paras's Absorb. Switching in FURYFIST (Lv. 8) was too risky; it was brought to critical HP in a single turn. A bulkier Pokémon or a faster switch strategy is needed for weakening wild encounters.
- **Inefficient Menu Navigation:** My menuing to switch Pokémon against the Paras was clumsy and slow. I need to be more precise with my button presses (e.g., Down vs. Right) to avoid wasted turns.