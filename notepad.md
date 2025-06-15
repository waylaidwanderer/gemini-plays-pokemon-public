# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps outside of battle.
*   **Battle Tactics:** If a move repeatedly fails, switch to a guaranteed-hit move.
*   **WKG Management:** Execute all tool calls from an agent's multi-step plan sequentially.
*   **NPC Sprites:** Defeated trainer sprites can sometimes temporarily block paths. Non-hostile trainers exist.
*   **Risk Management:** Avoid exploring deep into new, dangerous areas with an injured party. Prioritize healing.
*   **Item Interaction:** Items are map objects. Interact from an adjacent tile.
*   **Agent Pathing:** Trust agent-generated paths. If blocked, find a local detour to rejoin the path. Be precise with agent destination coordinates.

## 2. Current Exploration Plan
*   **Location:** Mt. Moon 1F
*   **Objective:** Follow the pathfinding agent's route to the item at (21, 34).
*   **Status:** Interrupted by a wild Sandshrew battle.

## 3. Pokémon Battle Intel
*   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock.
*   **Geodude (Rock/Ground):** 4x weak to Grass/Water.
*   **Sandshrew (Ground):** Weak to Water, Grass, Ice.
*   **Paras (Bug/Grass):** 4x weak to Fire/Flying.

## 4. Future Agent Ideas
*   **Pokédex Tracker Agent:** To suggest locations for catching new Pokémon based on the current Pokédex.