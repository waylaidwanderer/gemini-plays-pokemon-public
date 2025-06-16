# Gem's Gameplay Log & Strategies

## 1. Core Gameplay & Battle Mechanics
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.

## 2. Battle Intel
*   **Type Weaknesses (Verified):**
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water. Immune to Electric.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Electric & Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.
*   **Team Rocket @ Mt. Moon B2F:**
    *   Jessie & James's Team: Ekans (Lv 15), Meowth (Lv 16), Koffing (Lv 15).
    *   Triggered at (4,5) when trying to reach the steps at (4,6).
*   **Rival BLAZe @ Cerulean City (North):**
    *   Challenged at (21, 7) after finding the burgled house.

## 3. Cerulean City Gym Strategy
*   **Failed Attempt 1:** Blacked out against Misty.
*   **Key Intel:** Misty's ace is a Lv 21 Starmie (Water/Psychic). It is very fast and has powerful Psychic attacks (Confusion) and Water attacks (Bubblebeam).
*   **Critical Mistake:** SPROUT (Oddish, Grass/Poison) is weak to Starmie's Psychic moves.
*   **New Strategy:**
    1.  The current party is not suited to defeat Starmie.
    2.  After dealing with the situation on the north bridge, explore the routes north of Cerulean City for a suitable counter (e.g., a non-Poison Grass-type or a strong Bug-type).
    3.  Alternatively, grind levels for SPARKY to ensure he can out-speed and defeat Starmie with Electric attacks.
    4.  Do NOT re-challenge the gym until the team is properly prepared.

## 4. Current Objectives & Navigation
*   **Primary Objective:** Defeat Rival BLAZe on the north bridge.
*   **Next Objective:** Explore the routes north of Cerulean City.
*   **Progression Blockers:**
    *   A Rocket is inside the burgled house at (31, 9). He may need to be dealt with after the rival battle.

## 5. Agent Development & Usage Notes
*   **`party_health_assessor` (Refined):** Logic updated to prioritize health of key strategic Pokémon.
*   **`pathfinder_agent`:** Reliable for checking path validity. Does not account for moving NPCs.
*   **`battle_action_advisor` (New):** Designed to give real-time advice during battles.

## 6. Misc. Discoveries
*   **Non-Battling NPCs:**
    *   Cerulean City Cool Trainer F at (30, 27)
    *   Cerulean City Cool Trainer M at (32, 21)
    *   Cerulean Mart Cool Trainer M at (4, 6) (gives advice)
*   **Sleeping Electrode:** An object that looks like a Poké Ball at (29, 27) is described as a sleeping Electrode. Interaction currently does nothing.

## 6. Cerulean City Navigation (Hypothesis Log)
*   **Hypothesis 1:** Pathfind directly to the Rocket. **Result:** FAILED. Blocked by buildings and cuttable trees.
*   **Hypothesis 2:** Use the hidden passage behind the houses. **Result:** FAILED. It's a dead end and doesn't lead to the burgled house area.
*   **Hypothesis 3:** Interacting with the sleeping Electrode at (29, 27) is a story trigger. **Result:** FAILED (2 attempts). Electrode just snoozes.
*   **Current Realization:** The northern bridge area seems to be a one-way trip down to the southern city area via ledges. It's impossible to walk back up directly.
*   **New Hypothesis (4):** The path forward is to exit west to Route 4 and find a path that loops around to the northern routes (Route 24/25).

## 7. Major Corrections & Lessons Learned
*   **Route 4 is a one-way path EAST to Cerulean City**, not a loop-around route. My hypothesis was incorrect.
*   **WKG Tool Workflow:** To add a new connection, I must: 1. Check if nodes exist. 2. Create missing nodes and get their IDs. 3. Create the edge using the final IDs. Do not try to do it all at once with placeholders.