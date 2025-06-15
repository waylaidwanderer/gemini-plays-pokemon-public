# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps. KITSUNE fainted from this! Must be more vigilant about checking party status after battles with poison-capable Pokémon.
*   **Agent Pathing:** Pathfinding agents need to target tiles *adjacent* to NPCs, not the NPCs themselves. Exploration agent paths can be flawed; if a path is invalid, the agent needs refinement.
*   **NPC Interaction:** Repeatedly talking to an NPC that gives the same dialogue line is pointless. It likely means they have already been defeated or served their purpose.
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. If a move's accuracy is low, switch to a more reliable one.
*   **WKG Management:** Execute all tool calls from an agent's multi-step plan sequentially.

## 2. Mt. Moon Exploration Strategy
*   **Objective:** Find the two fossils and the exit to Cerulean City.
*   **Method:** Systematically explore all floors of Mt. Moon, using my exploration and pathfinding agents to navigate efficiently. Defeat all trainers encountered to clear paths and gain EXP.
*   **Hypothesis (Failed):** The fossils are NOT located behind the Super Nerd at (25, 32) on Mt. Moon 1F. This area is a dead end. The fossils must be elsewhere.

## 3. Pokémon Battle Intel
*   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock.
*   **Geodude (Rock/Ground):** 4x weak to Grass/Water.
*   **Sandshrew (Ground):** Weak to Water, Grass, Ice. Immune to Poison status.
*   **Paras (Bug/Grass):** 4x weak to Fire/Flying.