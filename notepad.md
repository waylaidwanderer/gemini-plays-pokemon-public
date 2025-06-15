# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps outside of battle.
*   **WKG Management:** Execute all tool calls from an agent's multi-step plan sequentially.
*   **NPC Sprites:** Defeated trainer sprites can sometimes temporarily block paths. Non-hostile trainers exist.
*   **Risk Management:** Avoid exploring deep into new, dangerous areas with an injured party. Prioritize healing.
*   **Item Interaction:** Items are map objects. Interact from an adjacent tile.
*   **Agent Pathing:** Trust agent-generated paths. If blocked, find a local detour to rejoin the path. Be precise with agent destination coordinates.
*   **Battle Tactics:** If a move's accuracy is severely lowered (e.g., by Sand-Attack), switch to a higher-accuracy move like Tackle instead of repeatedly trying a failing move.
*   **Battle Tactics:** Ground-types might be immune to the poison status effect.

## 2. Current Exploration Plan
*   **Objective:** Find the exit of Mt. Moon to reach Cerulean City.
*   **Path:** Explore the lower levels of Mt. Moon, defeat trainers, and find the correct ladder out.

## 3. Pokémon Battle Intel
*   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock.
*   **Geodude (Rock/Ground):** 4x weak to Grass/Water.
*   **Sandshrew (Ground):** Weak to Water, Grass, Ice. Immune to Poison status.
*   **Paras (Bug/Grass):** 4x weak to Fire/Flying.