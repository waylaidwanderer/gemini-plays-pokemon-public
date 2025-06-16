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

## 4. Cerulean Gym - Post-Mortem & New Strategy
*   **Failed Attempt 1:** Blacked out against Misty.
*   **Critical Mistake:** Sent SPROUT (Oddish, Grass/Poison) against Misty's Starmie (Water/Psychic). Starmie's Psychic moves are 4x super-effective against SPROUT. This was a fatal error.
*   **Key Intel:** Misty's ace is a Lv 21 Starmie (Water/Psychic). It is very fast and has powerful Psychic attacks (Confusion) and Water attacks (Bubblebeam).
*   **New Strategy:**
    1.  My current party is not strong enough or well-suited to defeat Starmie.
    2.  I need to find a better counter. The routes north of Cerulean City might have suitable Grass-type Pokémon that are not also Poison-type.
    3.  Alternatively, I need to grind levels for my existing team, especially SPARKY, to ensure he can out-speed and one-shot Starmie.
    4.  Do NOT re-challenge the gym until the team is properly prepared.

## 5. Agent Development Notes
*   **`party_health_assessor`:** The logic is flawed. It rated my party 'HEALTHY' when my key counter (SPARKY) was at 50% HP. The agent needs to be updated to weigh strategically important Pokémon more heavily.
*   **`targeted_pathfinder_agent` (DECOMMISSIONED):** This agent has failed repeatedly and is fundamentally broken. It cannot correctly identify impassable tiles or handle ledge mechanics. **DO NOT USE** until it is completely rewritten from scratch. (Failures: Turns 8533, 8534, 8536, 8565, 8570, 8572, 8574).
*   **`path_validator_agent`:** A reliable agent for checking if a manually plotted path is valid. Use this before committing to long, complex movements.

## 6. Non-Battling NPCs
*   Cerulean City Cool Trainer F at (30, 27)
*   Cerulean City Cool Trainer M at (32, 21)
*   Cerulean Mart Cool Trainer M at (4, 6) (gives advice)

## 7. Current Walkthrough Hint
*   The path north of Cerulean City is blocked by a police officer. To remove him, I must resolve the situation at the 'burgled house' in the northeast of the city.