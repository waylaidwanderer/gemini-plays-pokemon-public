# Gem's Gameplay Log & Strategies

## 1. Agent Development Log
*   `exploration_helper_agent` is critically flawed. Despite multiple refinements, it consistently fails to identify reachable unseen tiles that are present in the game state. Abandoning use of this agent and deleting it. Will build a simpler `unseen_tile_finder_agent`.

## 2. Game Mechanics & Lessons Learned
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Agent Pathing:** Pathfinding agents need to target tiles *adjacent* to NPCs, not the NPCs themselves.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp. (Confirmed)
*   **NPC Interaction:** Repeatedly talking to an NPC that gives the same dialogue is pointless.
*   **Tool Usage:** Multiple tool calls from an agent's plan should be batched into a single turn for maximum efficiency.
*   **Strategic Correction:** If a tool or strategy fails more than twice, abandon it and pivot to a more reliable method.

## 3. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. If a move's accuracy is low, switch to a more reliable one.
*   **Type Weaknesses:**
    *   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock.
    *   **Geodude (Rock/Ground):** 4x weak to Grass/Water.
    *   **Sandshrew (Ground):** Weak to Water, Grass, Ice. Immune to Poison status.
    *   **Paras (Bug/Grass):** 4x weak to Fire/Flying.

## 4. Mt. Moon Exploration Notes
*   **Objective:** Find the two fossils and the exit to Cerulean City, which is past the Super Nerd on 1F.
*   **Confirmed Dead Ends:**
    *   The western corridor on Mt. Moon B1F at (14, 12).
    *   The entire eastern section of Mt. Moon B2F.
*   **Confirmed Fact:** The warp at (15, 36) on 1F is the ENTRANCE from Route 4, not the exit to Cerulean City.
*   **Main Path Hypothesis:** The main path forward is on the first floor, leading past the Super Nerd. This needs to be investigated after exploring other floors.