# Gem's Gameplay Log & Strategies

## 1. Current Objectives
- **Primary:** Choose a fossil on Mt. Moon 1F to open the path to the exit.
- **Secondary:** Navigate back to Mt. Moon 1F.
- **Tertiary:** Heal KITSUNE's paralysis at the next opportunity.

## 2. Game Mechanics & Lessons Learned
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Mandatory Puzzles:** Some environmental puzzles are not optional and must be solved to progress. The Mt. Moon fossil choice is a key example.

## 3. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types might be immune to the poison status effect. Low accuracy moves should be avoided.
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.

## 4. Mt. Moon Notes
### Mt. Moon 1F (ID: 59)
*   **The path to the exit is past the Super Nerd at (25, 32). After defeating him, one of the two fossils must be chosen to open the final ladder.**
*   The ladder at (38, 34) in the eastern corridor is a dead end.
*   The ladder at (18, 12) leads to an isolated, dead-end platform on B1F.
*   The entrance/exit to Route 4 is at (15, 36).

### Mt. Moon B1F (ID: 60)
*   The entire floor seems to be a large U-shaped series of corridors and dead-end platforms, used for connecting different parts of 1F and B2F.

### Mt. Moon B2F (ID: 61)
*   This floor contains several Team Rocket members and some items, but does not appear to contain the main exit from the cave.

## 5. Agent Status & Improvement Plans
*   **`pathfinding_agent`:** Still has issues with `steps` tiles. Needs further refinement to explicitly handle elevation changes. The current implementation is unreliable in complex vertical terrain.