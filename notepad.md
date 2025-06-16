# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Rules
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time. Interact from an adjacent tile, do not try to walk onto them.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.
*   **Move Categories:** In Gen 1, move categories are based on type. Flying-type moves like Gust are Physical, so their damage IS affected by moves like Growl.
*   **Battle Menu Input:** The game only registers one directional button press per turn in menus. Do not attempt to chain multiple inputs.

## 2. Battle Intel & Movesets
*   **Rival BLAZe @ Cerulean City (North):** Challenged at (21, 7) after finding the burgled house.
*   **Team Rocket @ Mt. Moon B2F:** Jessie & James's Team: Ekans (Lv 15), Meowth (Lv 16), Koffing (Lv 15). Triggered at (4,5) when trying to reach the steps at (4,6).
*   **Mankey @ Nugget Bridge:** A Lv 18 Mankey's Low Kick move can cause flinching. Its Stun Spore failed, suggesting a possible immunity to powder moves for Fighting-types.

### Verified Type Weaknesses
*   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock.
*   **Geodude (Rock/Ground):** 4x weak to Grass/Water. Immune to Electric.
*   **Sandshrew (Ground):** Weak to Water, Grass, Ice. Immune to Electric & Poison status.
*   **Paras (Bug/Grass):** 4x weak to Fire/Flying.

## 3. Gym Strategies
### Cerulean City Gym - Misty
*   **Status:** Failed Attempt 1 (Blacked out).
*   **Key Intel:** Misty's ace is a Lv 21 Starmie (Water/Psychic). It is very fast and has powerful Psychic attacks (Confusion) and Water attacks (Bubblebeam).
*   **New Strategy:** Explore north of Cerulean City for a suitable counter (e.g., a non-Poison Grass-type or a strong Bug-type) or grind levels for SPARKY.

## 4. Navigation Log & Hypotheses
*   **Route 4:** Confirmed one-way path EAST to Cerulean City.
*   **Sleeping Electrode @ Cerulean (29, 27):** Interaction currently does nothing. Might require an item/event.

## 5. Agent Development & Usage Notes
*   **`battle_navigator_agent`:** Must execute its plans one button press at a time. Was updated with correct 2x2 menu logic.
*   **`battle_action_advisor`:** Use in tandem with navigator for every battle action.
*   **`wkg_transition_recorder_agent`:** Could be improved to handle node checking/creation and edge creation in a single call.

## 6. Pokémon-Specific Notes & Discoveries
*   **PARCH (Sandshrew):** Verified to be a NORMAL type in this ROM hack, not Ground. This completely changes its matchups.

## 7. Defeated Trainers
*   **Jr. Trainer @ Route 24 (6, 21):** Team: Diglett (Lv 15), Psyduck (Lv 15).

## 8. Non-Battling NPCs
*   **Cerulean City Cool Trainer F @ (30, 27)**
*   **Cerulean City Cool Trainer M @ (32, 21)**
*   **Cerulean Mart Cool Trainer M @ (4, 6)** (gives advice)
*   **Route 24 Cool Trainer M @ (7, 6)** (taunts about Charmander)

*   **Route 25 Hiker @ (14, 8):** Non-battling. Only provides a tip about a shortcut to Cerulean City.

*   **Route 25 Cool Trainer F @ (19, 9):** Non-battling. Dialogue: 'Hi! My boyfriend is cool!'
*   **Trainer Interaction Rule:** If an NPC with a trainer sprite only provides dialogue on the first interaction, assume they are a non-battler and do not interact again.