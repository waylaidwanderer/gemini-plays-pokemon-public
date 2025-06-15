# Gem's Gameplay Log & Strategies

## 1. Current Objectives
- **Primary:** Find the exit of Mt. Moon to reach Cerulean City and earn the Cascade Badge.
- **Secondary:** Fully explore Mt. Moon.
- **Tertiary:** Train my Pokémon towards the level cap of 21.

## 2. Agent Improvement Notes
*   `pathfinding_agent`: Was critically flawed and required multiple fixes. It seems to be working now, but needs to be monitored.

## 3. Game Mechanics & Lessons Learned
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Mandatory Puzzles:** Some environmental puzzles are not optional and must be solved to progress.

## 4. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. Low accuracy moves should be avoided.
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.

## 5. Mt. Moon Exploration Notes
*   **Main Objective:** Find the exit to Cerulean City.
*   **Fossil Puzzle (Stalled):** The path forward is past the Super Nerd, not through the fossils. Giving up on the puzzle for now.
*   **Confirmed Dead Ends:**
    *   Western corridor on Mt. Moon B1F at (14, 12).
    *   Entire eastern section of Mt. Moon B2F.
    *   Eastern corridor on Mt. Moon 1F (ladder at (38, 34) is a fake-out).