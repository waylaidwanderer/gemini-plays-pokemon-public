# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Rules
- **NPC Interaction Rule:** If an NPC with a trainer sprite only provides dialogue on the first interaction, assume they are a non-battler. Mark them and move on.
- **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps outside of battle.
- **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.
- **Move Categories:** In Gen 1, move categories are based on type (e.g., Flying-type moves like Gust are Physical).
- **Post-Battle Status Cure:** Non-volatile status conditions (e.g., Poison) are automatically cured after a trainer battle concludes.

### ROM Hack Discoveries
- **Sandshrew Typing:** Sandshrew is a GROUND type, not Normal. (Confirmed vs. Youngster on Route 25).

## 2. Battle Intel
### Gym Leaders
- **Pewter City Gym - Brock (DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Cerulean City Gym - Misty:** Psyduck (Lv 18), Goldeen (Lv 18), Starmie (Lv 21).
  - **Status:** Failed Attempt 1 (Blacked out).
  - **Intel:** Starmie (Water/Psychic) is fast and powerful, uses Bubblebeam & Confusion. A major threat.
  - **Strategy:** Requires a strong counter. SPARKY (Electric) is a good option but needs levels. Party composition needs re-evaluation.

### Rival BLAZe
- **@ Oak's Lab:** Eevee (Lv 5).
- **@ Route 22:** Pidgeotto (Lv 9), Rattata (Lv 8), Eevee (Lv 10).
- **@ Cerulean City (North):** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).

### Major Encounters
- **Team Rocket (Jessie & James) @ Mt. Moon:** Ekans (Lv 15), Meowth (Lv 16), Koffing (Lv 15).
- **Super Nerd @ Mt. Moon:** Grimer (Lv 12), Voltorb (Lv 12), Magnemite (Lv 12), Clefairy (Lv 12).

## 3. Navigation & Exploration
- **Route 4:** Confirmed one-way path EAST to Cerulean City.
- **Route 25:**
  - Northern maze area is inaccessible from the south. Likely a shortcut from Bill's area.
  - Item at (23, 3) is currently unreachable.
- **Cerulean City:** Sleeping Electrode at (29, 27) currently does nothing.

## 4. Defeated Trainers Log
- **Route 24:** Jr. Trainer @ (6, 21), Lass @ (11, 23), Youngster @ (12, 26), Youngster @ (12, 32), Rocket Grunt @ (12, 16).
- **Route 25:** Hiker @ (9, 5), Lass @ (19, 9), Hiker @ (24, 10), Youngster @ (33, 4), Lass @ (38, 5), Youngster @ (19, 6), Youngster @ (15,4).

## 5. Agent Development Log
- **`battle_navigator_agent`:** Updated to consolidate button presses.
- **`exp_tracker_agent`:** Created to monitor EXP/level cap.
- **`party_manager_agent`:** Created to suggest optimal party compositions.
- **`item_finder_agent`:** Updated to include searching for named NPCs.