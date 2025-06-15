# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Agent Pathing:** Pathfinding agents need to target tiles *adjacent* to NPCs, not the NPCs themselves. Agents can have flawed logic and require refinement if their plans are invalid.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp. (Confirmed)
*   **NPC Interaction:** Repeatedly talking to an NPC that gives the same dialogue is pointless.
*   **Tool Usage:** Multiple tool calls from an agent's plan should be batched into a single turn for maximum efficiency.
*   **Strategic Correction:** Panicking leads to bad decisions. My initial attempt to escape Mt. Moon by backtracking to the entrance was incorrect. The true path forward is on 1F, past the Super Nerd.

## 2. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. If a move's accuracy is low, switch to a more reliable one.
*   **Type Weaknesses:**
    *   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock.
    *   **Geodude (Rock/Ground):** 4x weak to Grass/Water.
    *   **Sandshrew (Ground):** Weak to Water, Grass, Ice. Immune to Poison status.
    *   **Paras (Bug/Grass):** 4x weak to Fire/Flying.

## 3. Mt. Moon Exploration Notes
*   **Objective:** Find the two fossils and the exit to Cerulean City, which is past the Super Nerd on 1F.
*   **Confirmed Dead Ends:**
    *   The western corridor on Mt. Moon B1F at (14, 12).
    *   The entire eastern section of Mt. Moon B2F.
*   **Confirmed Fact:** The warp at (15, 36) is the ENTRANCE from Route 4, not the exit to Cerulean City.
*   **Main Path:** The main path forward is on the first floor, leading to the Super Nerd.