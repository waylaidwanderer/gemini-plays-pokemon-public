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
*   **Trust Your Tools:** If an agent provides a path, follow it *exactly*. Do not deviate or attempt manual shortcuts. My manual navigation in complex areas has repeatedly failed.
*   **Systematic Exploration:** When exploring manually, adopt a methodical pattern (e.g., wall-following) to ensure complete coverage and avoid loops.
*   **Pre-Move Path Check:** Before moving, trace the next 5-10 steps on the map to ensure the path is clear and avoid walking into obvious obstacles.
*   **Verified Blockers:** The Rocket Grunt at Mt. Moon B2F (16, 23) is an impassable obstacle even after being defeated. Not all defeated trainers are blockers.
*   **Mobile NPCs:** For evasive NPCs, use `stun_npc` to freeze them before interaction.