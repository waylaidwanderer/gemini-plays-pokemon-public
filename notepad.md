# Gem's Gameplay Log & Strategies

## 1. Agent Improvement Notes
*   `pathfinding_agent`: Unreliable, needs a logic overhaul. It fails to find simple paths and must be refined before use.
*   `wkg_transition_recorder_agent`: Inefficient. Needs to be updated to check for existing nodes before adding new ones to prevent duplicates and streamline the process into a single turn.

## 2. Game Mechanics & Lessons Learned
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items. Visual patterns on the ground may be cosmetic.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time. Move away to break the loop.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.

## 3. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. Low accuracy moves should be avoided in favor of more reliable ones.
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.

## 4. Mt. Moon Exploration Notes
*   **Objective:** Find the exit to Cerulean City.
*   **Fossil Puzzle:** Abandoned. Numerous attempts to interact with the ground patterns failed. They are not items.
*   **Confirmed Dead Ends:**
    *   The western corridor on Mt. Moon B1F at (14, 12).
    *   The entire eastern section of Mt. Moon B2F.
    *   The eastern corridor on Mt. Moon 1F past the Super Nerd (ladder at (38, 34) is a fake-out).
*   **Main Path Hypothesis:** The exit is likely a ladder I have not yet found, possibly on a different floor or in a different section of 1F. The path past the Super Nerd was not the direct exit.