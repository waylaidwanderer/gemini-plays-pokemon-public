# Gem's Strategic Plan & Learnings

## Current Plan
1.  My party is in CRITICAL condition. My ONLY priority is to reach the Pewter City Pokémon Center to heal.
2.  I will use Repels to avoid wild encounters.
3.  I will use the `pathfinding_agent` to plot the most direct route to the forest exit and follow it precisely.
4.  The side-quest for the item at (13, 30) is ABANDONED as it is too risky.

## Lessons & Failed Hypotheses Log
*   **PoisonPowder vs. Metapod:** My assumption that Metapod is part Poison-type was incorrect. In Gen 1, it is a pure Bug-type. PoisonPowder's failure was due to its 75% accuracy, not type immunity. (Corrected after critique).
*   **Route 22 Training:** The main grassy area is inaccessible from the south/east. It requires jumping down ledges from an area blocked by the Pokémon League guard. (Failed >10 attempts to access). **Resolution: Abandoned. Training must be integrated with progression on the main path.**
*   **Manual Navigation in Viridian City:** Highly inefficient. Resulted in getting lost repeatedly. (Failed >15 attempts). **Resolution: Use `pathfinding_agent` for all city navigation.**
*   **Battle of Attrition (PIP vs. Pidgey):** Attempting to win with PIP despite multiple accuracy debuffs was a poor, high-risk choice that nearly resulted in a faint. (Failed >5 attack attempts). **Resolution: Switch to a reliable counter immediately when a fight goes south. Do not be stubborn.**
*   **Getting Stuck in Menus:** I have wasted significant time stuck in the nickname menu. This is an execution failure. **Resolution: Be more careful and deliberate with button inputs.**
*   **Viridian Forest Youngster (17, 44):** This NPC is non-hostile and blocks a dead-end path. I interacted with him 3 times with no battle initiated. The correct path is to the east and then north.

## Agent Usage Protocols
*   **`pathfinding_agent`:** Use PROACTIVELY for any non-trivial navigation.
*   **`battle_strategist_agent`:** Use PROACTIVELY at the start of any non-trivial battle.
*   **`pre_adventure_checker_agent`:** Use before leaving ANY town with a Pokémon Center to ensure party readiness. This is a critical step to avoid repeating the current low-health crisis.