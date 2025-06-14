# Game Mechanics & Lessons

## Navigation
- **Misinterpretation of Obstacle (Mt. Moon B2F):** My repeated failures to pass the Rocket Grunt at (16, 23) led me to incorrectly conclude that defeated trainers are impassable. The critique suggests this is a hallucination. The blockage is likely an invisible wall on an *adjacent* tile, not the sprite itself. I must return to B2F after healing and systematically test all tiles around the grunt to find the correct path forward.

## Agent Development & Tactics
- **Pathfinder Agent Correction:** The update to the `master_pathfinder_agent` was based on the flawed assumption about defeated trainers. This change must be reverted. The agent should NOT treat defeated trainers as obstacles until this mechanic is proven with certainty.
- Battle tactics need to be more proactive. I will not wait until a Pokémon's HP is critical before using priority moves like Quick Attack.

## Battle Notes
- If running from a wild battle fails more than twice, it is more efficient to defeat the opponent (e.g., failed to run from Geodude 3 times in Mt. Moon).

## Battle Tactics & Analysis
- **Miscalculation vs. Paras (Mt. Moon B1F):** I underestimated the damage from a Lv. 11 Paras's Absorb. Switching in FURYFIST (Lv. 8) was too risky; it was brought to critical HP in a single turn. A bulkier Pokémon or a faster switch strategy is needed for weakening wild encounters.
- **Inefficient Menu Navigation:** My menuing to switch Pokémon against the Paras was clumsy and slow. I need to be more precise with my button presses (e.g., Down vs. Right) to avoid wasted turns.