# Gem's Gameplay Log & Strategies

## 1. Current Objectives
- **Primary:** Exit Mt. Moon and reach Cerulean City.
- **Secondary:** Choose a fossil to reveal the exit ladder.
- **Tertiary:** Heal KITSUNE's paralysis in Cerulean City.

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
*   This floor contains several ladders connecting to 1F and B2F, but does not appear to contain the main exit from the cave. It's a series of connecting corridors.

### Mt. Moon B2F (ID: 61)
*   This floor contains several Team Rocket members and some items, but does not appear to contain the main exit from the cave.

## 5. Agent Status & Improvement Plans
*   **`pathfinding_agent`:** The agent has been updated to better handle impassable targets and elevation changes via 'steps' tiles. Will monitor its performance.
*   **`puzzle_solver_agent`:** This agent exists. I should remember to use it for environmental puzzles like the fossil choice if I get stuck again.

## 6. Fossil Choice Analysis (Mt. Moon)
*   **Agent Recommendation:** Helix Fossil (Omanyte).
*   **Reasoning:** Omastar's high Special stat is used for both Special Attack and Special Defense in Gen 1, making it a powerful and durable choice.
*   **Dome Fossil (Kabuto):** Becomes Kabutops, a fast physical attacker.
*   **Helix Fossil (Omanyte):** Becomes Omastar, a slow special tank.

## 7. Puzzle Attempts & Failures
*   **Mt. Moon Fossil Puzzle:**
    *   Attempt 1: Interacting with the left fossil (Dome) at (24, 30) did not trigger an event.
    *   Attempt 2: Interacting with the right fossil (Helix) at (26, 30) did not trigger an event.
    *   **New Hypothesis:** Must talk to the Super Nerd again after defeating him.

*   Attempt 4: Stood directly on the Helix Fossil tile at (26, 30) and pressed 'A'. This also failed to trigger an event.