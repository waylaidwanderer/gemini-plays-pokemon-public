# Gem's Strategic Plan & Learnings

## Operational Rules (CRITICAL)
1.  **Crisis Protocol:** When the party is in a critical state (e.g., multiple Pokémon with low HP, no healing items), the Primary Goal of reaching a safe location (like a Pokémon Center) is ABSOLUTE. No deviations for training, item collection, or optional battles are permitted.
2.  **Risk Assessment:** Before deviating from a primary travel plan for an opportunistic goal (like training), I must use the `risk_assessor_agent` to get an objective analysis. High-risk actions are forbidden when the party is not fully prepared.

## Current Plan
1.  Flee the current battle with the Kakuna immediately.
2.  Navigate manually out of Viridian Forest to the exit at (2,1). The `pathfinding_agent` is unreliable here.
3.  Proceed directly to the Pewter City Pokémon Center to heal.

## Lessons & Failed Hypotheses Log
*   **Pathfinding Agent Failure (Viridian Forest):** The agent provided an invalid path from (17, 6) and (17, 8), suggesting movement through impassable trees. The agent's map data or logic is flawed for this area. **Resolution: The agent cannot be trusted for complex maze navigation. Manual navigation is required.** (Logged after 2 failed attempts).
*   **Strategic Discipline Failure:** I abandoned my critical primary goal (escape and heal) to pursue a low-value tertiary goal (training KITSUNE on a Kakuna) while my party was near-faint. This was an unacceptable risk. **Resolution: Adhere to Operational Rules.**
*   **PoisonPowder vs. Metapod:** My assumption that Metapod is part Poison-type was incorrect. In Gen 1, it is a pure Bug-type. PoisonPowder's failure was due to its 75% accuracy, not type immunity. (Corrected after critique).
*   **Route 22 Training:** The main grassy area is inaccessible from the south/east. It requires jumping down ledges from an area blocked by the Pokémon League guard. (Failed >10 attempts to access). **Resolution: Abandoned. Training must be integrated with progression on the main path.**

## Agent Usage Protocols
*   **`risk_assessor_agent`:** Use before undertaking any non-essential action when the party is not at 100% readiness.
*   **`pre_adventure_checker_agent`:** Use before leaving ANY town with a Pokémon Center to ensure party readiness. This is a critical step to avoid repeating the current low-health crisis.
*   **`battle_strategist_agent`:** Use PROACTIVELY at the start of any non-trivial battle.