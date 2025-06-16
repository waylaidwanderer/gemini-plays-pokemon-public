# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Rules
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.

## 2. Battle Intel
*   **Rival BLAZe @ Cerulean City (North):** Challenged at (21, 7) after finding the burgled house.
*   **Team Rocket @ Mt. Moon B2F:** Jessie & James's Team: Ekans (Lv 15), Meowth (Lv 16), Koffing (Lv 15). Triggered at (4,5) when trying to reach the steps at (4,6).

### Verified Type Weaknesses
*   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock.
*   **Geodude (Rock/Ground):** 4x weak to Grass/Water. Immune to Electric.
*   **Sandshrew (Ground):** Weak to Water, Grass, Ice. Immune to Electric & Poison status.
*   **Paras (Bug/Grass):** 4x weak to Fire/Flying.

## 3. Gym Strategies
### Cerulean City Gym - Misty
*   **Status:** Failed Attempt 1 (Blacked out).
*   **Key Intel:** Misty's ace is a Lv 21 Starmie (Water/Psychic). It is very fast and has powerful Psychic attacks (Confusion) and Water attacks (Bubblebeam).
*   **Critical Mistake:** SPROUT (Oddish, Grass/Poison) is weak to Starmie's Psychic moves.
*   **New Strategy:** Do NOT re-challenge the gym until the team is properly prepared. The current party is not suited to defeat Starmie. Explore north of Cerulean City for a suitable counter (e.g., a non-Poison Grass-type or a strong Bug-type) or grind levels for SPARKY.

## 4. Navigation Log & Hypotheses
### Cerulean City Navigation
*   **Hypothesis 1:** Pathfind directly to the Rocket. **Result:** FAILED. Blocked by buildings and cuttable trees.
*   **Hypothesis 2:** Use the hidden passage behind the houses. **Result:** FAILED. It's a dead end and doesn't lead to the burgled house area.
*   **Hypothesis 3 (Stalled):** Interacting with the sleeping Electrode at (29, 27) is a story trigger. **Result:** FAILED (2 attempts). Electrode just snoozes. Might require an item/event.
*   **Hypothesis 4:** The path forward is to exit west to Route 4 and find a path that loops around to the northern routes (Route 24/25). **Result:** FAILED. Route 4 is a one-way path EAST to Cerulean City.
*   **Current Realization:** The northern bridge area seems to be a one-way trip down to the southern city area via ledges. It's impossible to walk back up directly.

## 5. Known NPCs & Objects
*   **Progression Blocker:** A Rocket is inside the burgled house at (31, 9) in Cerulean City. May need to be dealt with after the rival battle.
*   **Sleeping Electrode:** An object that looks like a Poké Ball at (29, 27) in Cerulean City is described as a sleeping Electrode. Interaction currently does nothing.
*   **Non-Battling NPCs:**
    *   Cerulean City Cool Trainer F at (30, 27)
    *   Cerulean City Cool Trainer M at (32, 21)
    *   Cerulean Mart Cool Trainer M at (4, 6) (gives advice)

## 6. Agent Development & Usage Notes
*   **`party_health_assessor` (Refined):** Logic updated to prioritize health of key strategic Pokémon.
*   **`pathfinder_agent`:** Reliable for checking path validity. Does not account for moving NPCs.
*   **`battle_action_advisor`:** Designed to give real-time advice during battles. Should be used more consistently.

## 7. Major Corrections & Lessons Learned
*   **WKG Tool Workflow:** To add a new connection, I must: 1. Check if nodes exist. 2. Create missing nodes and get their IDs. 3. Create the edge using the final IDs. Do not try to do it all at once with placeholders.

### Unique Battle Mechanics Observed
*   **Mankey @ Nugget Bridge:** A Lv 18 Mankey's Low Kick move caused my Pokémon to flinch, preventing my move. This happened twice in a row. This might be a property of the move, the Pokémon, or a specific trainer's Pokémon.
*   **Stun Spore Failure:** My SPROUT's Stun Spore failed against the same Mankey with the message "It didn't affect Enemy MANKEY!". This suggests a possible immunity to powder moves for either Mankey's species or Fighting-types in this ROM hack.

## 8. Pokémon-Specific Notes & Discoveries
*   **PARCH (Sandshrew):** Verified to be a NORMAL type in this ROM hack, not Ground. This completely changes its matchups and resistances.

*   **Jr. Trainer @ Route 24 (6, 21):** Battling his team, which includes a Lv 15 Diglett and a Lv 15 Psyduck.