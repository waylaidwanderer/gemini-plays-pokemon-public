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

## 5. Mt. Moon Notes
### Mt. Moon 1F (ID: 59)
*   The main path to the exit is in the northwest corner, past the Super Nerd at (25, 32).
*   The ladder at (38, 34) in the eastern corridor is a dead end.
*   The ladder at (18, 12) leads to an isolated, dead-end platform on B1F.

### Mt. Moon B1F (ID: 60)
*   The western corridor accessed from the ladder at (14, 28) is a dead end.
*   The southern corridor accessed from the ladder at (6, 6) is a dead end.

### Mt. Moon B2F (ID: 61)
*   The entire eastern section of this floor is a dead end. The path forward is back up the ladder at (16, 28).

## 6. Agent Status
*   **`pathfinding_agent`:** Updated with improved logic for handling impassable targets and complex terrain. Monitoring for performance.