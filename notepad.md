# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time. Some key events are triggered by advancing through ALL of an NPC's dialogue.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Mobile NPCs:** For evasive NPCs, use `stun_npc` to freeze them before interaction.
*   **Defeated Trainers as Obstacles:** This is not a universal rule. The Rocket Grunt on Mt. Moon B2F at (16, 23) is a blocker, but others are not.
*   **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.

## 2. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types appear immune to poison status. Avoid low-accuracy moves.
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.

## 3. Agent Development & Known Issues
*   **npc_movement_predictor_agent:** Created to predict movement of mobile NPCs. Status: Untested.
*   **wkg_transition_recorder_agent:** Functional, but needs a WKG query to prevent adding duplicate edges. I should prioritize refining this.

## 4. Lessons from Critiques
*   **Abandon Failing Tools & Objectives:** If a tool (like an agent) or an objective proves unproductive after a few documented attempts, disengage immediately. Do not get stuck in a debugging or failure loop. Pivot to a manual backup plan or a different objective.
*   **Systematic Navigation:** When navigating complex dungeons, adopt a methodical exploration pattern (like wall-following) to prevent getting lost. Avoid forcing shortcuts.
*   **Map Awareness:** Before setting a navigation goal in a complex, multi-level area, carefully trace the path on the map to confirm it's a contiguous, reachable area. Do not make assumptions about connectivity between isolated sections.
*   **Commit to Exploration:** When arriving in a new, unexplored map area, explore it thoroughly before backtracking.