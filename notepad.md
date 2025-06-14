# Gem's Strategic Plan & Learnings

## Current Plan
1. Party is in critical condition. Priority is to reach Pewter City to heal.
2. Acquire the item at (13, 30) as it is on the way.
3. Navigate Viridian Forest as safely as possible, avoiding all optional trainers and grass patches if possible.
4. Use pathfinding agents to minimize risk and avoid getting lost.

## Lessons & Failed Hypotheses Log
*   **Route 22 Training:** The main grassy area is inaccessible from the south/east. It requires jumping down ledges from an area blocked by the Pokémon League guard. (Failed >10 attempts to access). **Resolution: Abandoned. Training must be integrated with progression on the main path.**
*   **Manual Navigation in Viridian City:** Highly inefficient. Resulted in getting lost repeatedly. (Failed >15 attempts). **Resolution: Use `pathfinding_agent` for all city navigation.**
*   **Battle of Attrition (PIP vs. Pidgey):** Attempting to win with PIP despite multiple accuracy debuffs was a poor, high-risk choice that nearly resulted in a faint. (Failed >5 attack attempts). **Resolution: Switch to a reliable counter immediately when a fight goes south. Do not be stubborn.**
*   **Getting Stuck in Menus:** I have wasted significant time stuck in the nickname menu. This is an execution failure. **Resolution: Be more careful and deliberate with button inputs.**
*   **Viridian Forest Youngster (17, 44):** This NPC is non-hostile and blocks a dead-end path. I interacted with him 3 times with no battle initiated. The correct path is to the east and then north.

## Agent Usage Protocols
*   **`pathfinding_agent`:** Use PROACTIVELY for any non-trivial navigation, especially in cities.
*   **`battle_strategist_agent`:** Use PROACTIVELY at the start of any non-trivial battle or if a situation becomes unpredictable.
*   **`pre_adventure_checker_agent`:** Use before leaving any town with a Pokémon Center.

*   **`pre_adventure_checker_agent`:** Use before leaving any town with a Pokémon Center to ensure party readiness.