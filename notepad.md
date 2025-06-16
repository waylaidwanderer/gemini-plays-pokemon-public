# Gem's Gameplay Log & Strategies

## 1. Core Gameplay & Battle Mechanics
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time. Some key events are triggered by advancing through ALL of an NPC's dialogue.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.

## 2. Battle Intel
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water. Immune to Electric.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Electric & Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.

## 3. Navigation & Exploration Strategy
*   **Agent Usage:** Agent outputs must be critically evaluated against the game state. If an agent proves unreliable, it must be refined or abandoned. Do not blindly trust a faulty tool.
*   **Systematic Exploration:** When exploring manually, adopt a methodical pattern (e.g., wall-following) to ensure complete coverage and avoid loops.
*   **Pre-Move Path Check:** Before moving, visually trace the intended path on the map to ensure it is clear of obstacles.
*   **Verified Blockers:** The Rocket Grunt at Mt. Moon B2F (16, 23) is an impassable obstacle even after being defeated. Not all defeated trainers are blockers.

## Mt. Moon B2F - Team Rocket Encounter
*   Jessie & James battle.
*   Jessie's Team: Ekans (Lv 15), Meowth (Lv 16).
*   James's Team: Unknown (likely Koffing).
*   Triggered at (4,5) when trying to reach the steps at (4,6).