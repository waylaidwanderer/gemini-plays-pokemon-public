# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time.
*   **Dialogue Advancement:** Some key events are triggered by advancing through ALL of an NPC's dialogue. Always press 'A' multiple times to ensure a conversation is truly over.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.

## 2. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. Low accuracy moves should be avoided.
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.

### Mt. Moon 1F (ID: 59)
*   **Fossil Area:** After defeating the Super Nerd at (25, 32), the path remains blocked. The southern ladder system from this area is a dead end for progression.

## 4. Area Notes
### Mt. Moon B2F (ID: 61)
*   Defeated trainers, like the Rocket Grunt at (16, 23), remain as impassable obstacles.

*   **Pathfinding Agent Failure:** The `pathfinding_agent` has repeatedly failed on Mt. Moon B2F, stating no path exists on `elevated_ground` even when a clear manual path is visible. It cannot be trusted for this map's layout. Manual navigation is required.