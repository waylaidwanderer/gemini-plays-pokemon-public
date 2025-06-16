# Gem's Gameplay Log & Strategies

## 1. Core Gameplay & Battle Mechanics
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.

## 2. Battle Intel
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water. Immune to Electric.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Electric & Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.
*   **Team Rocket @ Mt. Moon B2F**
    *   Jessie & James's Team: Ekans (Lv 15), Meowth (Lv 16), Koffing (Lv 15).
    *   Triggered at (4,5) when trying to reach the steps at (4,6).

## 3. Navigation Strategy
*   **Pre-Move Path Check:** Before moving, visually trace the intended path on the map to ensure it is clear of obstacles.
*   **Ledge Mazes:** When stuck in complex areas with many ledges, use the `ledge_maze_navigator_agent` to find the optimal path to the nearest unseen tile.
*   **Agent Usage:** Rely on agents for complex navigation (dungeons, ledges) to save time and avoid manual errors. Disengage from unproductive tasks (like chasing non-essential NPCs) quickly.

## 4. Current Exploration Plan: Cerulean City & Beyond
*   **Primary Objective:** Find a way to access the Cerulean Gym.
*   **Current Hypothesis:** The northern exit of Cerulean City is the key to progression. This path is expected to lead to a rival battle and subsequently unlock the path to the Gym.
*   **Immediate Goal:** Explore the northern route out of Cerulean City.