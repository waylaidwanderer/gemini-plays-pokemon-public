# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Rules
*   **NPC Interaction Rule:** If an NPC with a trainer sprite only provides dialogue on the first interaction, assume they are a non-battler. Mark them and move on.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.
*   **Move Categories:** In Gen 1, move categories are based on type. Flying-type moves like Gust are Physical, so their damage IS affected by moves like Growl.

## 2. Battle Intel & Movesets
*   **Rival BLAZe @ Cerulean City (North):** Challenged at (21, 7) after finding the burgled house.
*   **Team Rocket @ Mt. Moon B2F:** Jessie & James's Team: Ekans (Lv 15), Meowth (Lv 16), Koffing (Lv 15).
*   **Mankey @ Nugget Bridge:** A Lv 18 Mankey's Low Kick move can cause flinching.

### Verified Type Weaknesses
*   **Zubat (Poison/Flying):** Weak to Electric, Ice, Psychic, Rock.
*   **Geodude (Rock/Ground):** 4x weak to Grass/Water. Immune to Electric.
*   **Sandshrew (Ground):** Weak to Water, Grass, Ice. Immune to Electric & Poison status.
*   **Paras (Bug/Grass):** 4x weak to Fire/Flying.

## 3. Gym Strategies
### Cerulean City Gym - Misty
*   **Status:** Failed Attempt 1 (Blacked out).
*   **Key Intel:** Misty's ace is a Lv 21 Starmie (Water/Psychic). It is very fast and has powerful Psychic attacks (Confusion) and Water attacks (Bubblebeam).
*   **New Strategy:** Explore north of Cerulean City for a suitable counter or grind levels for SPARKY.

## 4. Navigation & Exploration
*   **Route 4:** Confirmed one-way path EAST to Cerulean City.
*   **Sleeping Electrode @ Cerulean (29, 27):** Interaction currently does nothing. Might require an item/event.

## 5. Agent Development
*   **`battle_navigator_agent`:** Updated with more robust logic for menu navigation.
*   **`battle_action_advisor`:** Updated to correctly identify and handle disabled moves.

## 6. Pokémon-Specific Notes
*   **PARCH (Sandshrew):** Verified to be a NORMAL type in this ROM hack, not Ground.

## 7. Defeated Trainers
*   **Route 24:** Jr. Trainer @ (6, 21), Lass @ (11, 23), Youngster @ (12, 26), Bug Catcher @ (12, 32).
*   **Route 25:** Lass @ (19, 9), Hiker @ (9, 5).

## 8. Non-Battling NPCs
*   **Cerulean City:** Cool Trainer F @ (30, 27), Cool Trainer M @ (32, 21).
*   **Cerulean Mart:** Cool Trainer M @ (4, 6) (gives advice).
*   **Route 24:** Cool Trainer M @ (7, 6) (taunts about Charmander).
*   **Route 25:** Hiker @ (14, 8), Cool Trainer F @ (19, 9).