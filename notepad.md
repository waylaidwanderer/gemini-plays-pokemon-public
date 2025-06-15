# Gem's Gameplay Log & Strategies

## 1. Agent Improvement Notes
*   `pathfinding_agent`: Was critically flawed and required multiple fixes. It seems to be working now, but needs to be monitored.

## 2. Game Mechanics & Lessons Learned
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items. Visual patterns on the ground may be cosmetic.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time. Move away to break the loop.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Mandatory Puzzles:** Some environmental puzzles are not optional and must be solved to progress. Giving up prematurely is a critical error.

## 3. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. Low accuracy moves should be avoided in favor of more reliable ones.
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.

## 4. Mt. Moon Exploration Notes
*   **Main Objective:** Find the exit to Cerulean City.
*   **Fossil Puzzle (Stalled):** The fossil puzzle is currently unsolvable. After defeating the Super Nerd at (25, 32), all attempts to acquire a fossil have failed.
    *   Attempt 1: Interacting with Helix Fossil from on top (25, 29).
    *   Attempt 2: Re-speaking with the defeated Super Nerd.
    *   Attempt 3: Interacting with Helix Fossil from below (25, 30).
    *   Attempt 4: Interacting with Dome Fossil from below (21, 30).
    *   Attempt 5: Interacting with Dome Fossil from on top (21, 29).
    *   Conclusion: The fossils are likely not directly interactable. Pivoting to finding the exit.
*   **Confirmed Dead Ends:**
    *   The western corridor on Mt. Moon B1F at (14, 12).
    *   The entire eastern section of Mt. Moon B2F.
    *   The eastern corridor on Mt. Moon 1F (ladder at (38, 34) is a fake-out).