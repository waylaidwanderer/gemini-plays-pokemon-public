# Gem's Gameplay Log & Strategies

## 1. Core Gameplay & Battle Mechanics
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.

## 2. Battle Intel
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water. Immune to Electric.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Electric & Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.
*   **Team Rocket @ Mt. Moon B2F**
    *   Jessie & James's Team: Ekans (Lv 15), Meowth (Lv 16), Koffing (Lv 15).
    *   Triggered at (4,5) when trying to reach the steps at (4,6).

## 3. Navigation Strategy
*   **Pre-Move Path Check:** Before moving, visually trace the intended path on the map to ensure it is clear of obstacles.
*   **Ledge Mazes:** When stuck in complex areas with many ledges, use the `ledge_maze_navigator_agent` to find the optimal path to the nearest unseen tile.
*   **NPC Blockers:** If a moving NPC repeatedly blocks a critical path, use the `stun_npc` tool to freeze them instead of wasting turns trying to maneuver around them.
*   **Agent Usage:** Agent outputs must be critically evaluated against the game state. If an agent proves unreliable, it must be refined or abandoned.

## 4. To-Do & Reminders