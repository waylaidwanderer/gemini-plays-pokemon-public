# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time.
*   **Dialogue Advancement:** Some key events are triggered by advancing through ALL of an NPC's dialogue.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Mobile NPCs:** For evasive NPCs that move around, use the `stun_npc` tool to freeze them in place before attempting to interact or battle. Chasing them is inefficient.

## 2. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. Low accuracy moves should be avoided.
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.

## 3. Area Notes
### Mt. Moon 1F (ID: 59)
*   **Fossil Area:** After defeating the Super Nerd at (25, 32), the path remains blocked. The southern ladder system from this area is a dead end for progression.

### Mt. Moon B2F (ID: 61)
*   Defeated trainers, like the Rocket Grunt at (16, 23), remain as impassable obstacles.

### Route 4 (ID: 15)
*   The Cool Trainer F is extremely mobile and difficult to engage in battle by simply chasing her.

## 4. Agent Notes
*   **Pathfinding Agent Failure:** The `pathfinding_agent` is unreliable in complex, multi-level dungeons like Mt. Moon. Its pathing logic does not handle verticality (multiple floors) well and can lead to inefficient routes or loops. Manual navigation or the `dungeon_navigator_agent` should be used instead in these areas.

## 5. Agent Ideas
*   **NPC Movement Analyzer:** An agent that could take a series of NPC coordinates over several turns to predict their movement pattern. This could be useful for intercepting moving trainers or avoiding obstacles.