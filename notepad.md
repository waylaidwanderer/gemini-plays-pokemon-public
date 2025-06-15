# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Agent Pathing:** Pathfinding agents need to target tiles *adjacent* to NPCs, not the NPCs themselves. Agents can have flawed logic and require refinement if their plans are invalid.
*   **Warp Mechanics:** Some warps may require moving into an adjacent impassable tile to activate, rather than just stepping on the warp tile itself. (Hypothesis - needs more testing).
*   **NPC Interaction:** Repeatedly talking to an NPC that gives the same dialogue is pointless.
*   **Tool Usage:** Multiple tool calls from an agent's plan should be batched into a single turn for maximum efficiency.

## 2. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. If a move's accuracy is low, switch to a more reliable one.
*   **Type Weaknesses:**
    *   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock.
    *   **Geodude (Rock/Ground):** 4x weak to Grass/Water.
    *   **Sandshrew (Ground):** Weak to Water, Grass, Ice. Immune to Poison status.
    *   **Paras (Bug/Grass):** 4x weak to Fire/Flying.

## 3. Mt. Moon Exploration Notes
*   **Objective:** Find the two fossils and the exit to Cerulean City.
*   **Failed Hypothesis:** The fossils are NOT located behind the Super Nerd at (25, 32) on Mt. Moon 1F. That path is a dead end.

*   **Traversal Mechanic:** I can step up from a 'ground' tile to an adjacent 'elevated_ground' tile, even without 'steps'. This seems to be a special case for certain warp tiles.