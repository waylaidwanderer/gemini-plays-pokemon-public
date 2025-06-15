# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps outside of battle.
*   **Battle Tactics:** If a move repeatedly fails, switch to a guaranteed-hit move.
*   **WKG Management:** Execute all tool calls from an agent's multi-step plan sequentially.
*   **NPC Sprites:** Defeated trainer sprites can sometimes temporarily block paths.
*   **Risk Management:** Avoid exploring deep into new, dangerous areas with a significantly injured party. Prioritize healing.
*   **Item Interaction:** Items are objects on the map. I cannot walk on them. I must interact with them from an adjacent tile.
*   **Agent Pathing:** I must trust my `exploration_helper_agent`. When a path is blocked, I should find a local detour to rejoin the path, not discard the entire plan.

## 2. Current Exploration Plan
*   **Location:** Mt. Moon 1F
*   **Method:** Follow the agent-generated path. If blocked, find a local detour. The goal is to explore all unseen tiles, which will lead to items, trainers, and the exit.

## 3. Pokémon Battle Intel
*   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock. (SPARKY)
*   **Geodude (Rock/Ground):** 4x weak to Grass/Water. (SPROUT, THISTLE)
*   **Sandshrew (Ground):** Weak to Water, Grass, Ice. (SPROUT, THISTLE, PARCH)
*   **Paras (Bug/Grass):** 4x weak to Fire/Flying. (KITSUNE, PIP)

## Lessons from Mt. Moon
*   The 'Cool Trainer F' at (17, 24) is non-hostile.
*   A full retreat from a dungeon is a massive time loss.