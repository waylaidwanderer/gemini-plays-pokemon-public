# Gem's Gameplay Log & Strategies

## 1. Agent Improvement Notes
*   `wkg_transition_recorder_agent`: This agent is inefficient, requiring multiple turns per transition. It needs to be refined to check for existing nodes and consolidate tool calls into a single turn if possible.
*   WKG Node Naming: Use more descriptive names for nodes, e.g., 'Mt. Moon B1F Ladder (to 1F)' instead of 'Node: 60 (6,6) to 59 (6,6)'.

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

## 5. Pending Agent Refinements
*   **Strategy:** Log agent issues here and refine them in a safe area (like a Pokémon Center) to maintain exploration momentum.

*   `pathfinding_agent`: Failed 3 times in a row to find a simple path. It is currently too unreliable to use. Will need a more significant logic overhaul later.

## 6. Mt. Moon Fossil Puzzle Failures
*   Hypothesis 1: Interacting from adjacent tile. Result: Failed.
*   Hypothesis 2: Walking onto tile triggers event. Result: Failed.
*   Hypothesis 3: Talking to Pikachu on tile. Result: Failed.
*   Hypothesis 4: Talking to Super Nerd post-battle. Result: Failed.
*   Hypothesis 5: Walking onto tile after defeating Nerd. Result: Failed.
*   Hypothesis 6: Pressing 'A' while standing on tile. Result: Failed (left fossil).