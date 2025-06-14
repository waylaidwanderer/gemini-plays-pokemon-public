# Gem's Strategic Plan 2.0

## Primary Goal
- Defeat Brock, the Pewter City Gym Leader, to earn the Boulder Badge.

## Secondary Goal
- Train party members by battling wild Pokémon and trainers encountered on the direct path to Pewter City.

## Tertiary Goal
- Fully explore Route 2 to find all items and trainers.

## Agent Usage Protocols
*   **`pathfinding_agent`:** Use PROACTIVELY for any non-trivial navigation, especially in cities.
*   **`battle_strategist_agent`:** Use PROACTIVELY at the start of any non-trivial battle or if a situation becomes unpredictable.
*   **`pre_adventure_checker_agent`:** Use before leaving any town with a Pokémon Center.

## Lessons & Failed Hypotheses Log
*   **Route 22 Training:** The main grassy area is inaccessible from the south/east. It requires jumping down ledges from an area blocked by the Pokémon League guard. (Failed >10 attempts to access). **Resolution: Abandoned. Training must be integrated with progression on the main path.**
*   **Manual Navigation in Viridian City:** Highly inefficient. Resulted in getting lost repeatedly. (Failed >15 attempts). **Resolution: Use `pathfinding_agent` for all city navigation.**
*   **Battle of Attrition (PIP vs. Pidgey):** Attempting to win with PIP despite multiple accuracy debuffs was a poor, high-risk choice that nearly resulted in a faint. (Failed >5 attack attempts). **Resolution: Switch to a reliable counter immediately when a fight goes south. Do not be stubborn.**
*   **Getting Stuck in Menus:** I have wasted significant time stuck in the nickname menu. This is an execution failure. **Resolution: Be more careful and deliberate with button inputs.**