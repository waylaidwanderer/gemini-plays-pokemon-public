## 1. Gameplay Insights & Lessons
- **Systematic Exploration is Key:** When a path is blocked or a menu option fails, I must test all other possibilities methodically before assuming a dead end or repeating the failed action. (Learned from Route 25 & PC menu loops).
- **NPC Interaction Rules:**
    - Non-battling trainers give dialogue once, then act as impassable walls. Mark and move on.
    - Defeated trainers are also impassable walls. Always plan routes *around* them. (Learned on Nugget Bridge).
    - Some NPCs blocking paths can be bypassed by walking around them. (Learned with Cool Trainer F on Route 25).
    - NPC roles vary; some are for trades or events, not just battles. (Learned from Cool Trainer F on Route 25).
- **Game Mechanics:**
    - **Poison Damage:** Poisoned Pokémon lose 1 HP every 4 steps outside battle.
    - **Level Cap EXP:** Pokémon at the level cap show an EXP gain message, but their actual EXP value does not increase (visual bug).
    - **Sandshrew Typing:** Confirmed as pure GROUND type.
    - **Post-Battle Status Cure:** Non-volatile status conditions are cured after trainer battles.
    - **PC System:** 'SOMEONE's PC' is for Pokémon Storage; 'Gem's PC' is for Item Storage.
    - **HM Usage (CUT):** Granted by the Cascade Badge. To use, stand in front of a cuttable tree and press 'A'. It is not used from a menu.
- **PIP (Pidgey) Evolution:** Pressing 'B' during evolution stops it. I need to be careful not to do this again.

## 2. Battle Intel
### Gym Leaders
- **Brock (Pewter City - DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Misty (Cerulean City - DEFEATED):** Psyduck (Lv 18), Goldeen (Lv 18), Starmie (Lv 21).
  - **Intel:** Starmie (Water/Psychic) is very fast. Paralysis was key to victory.

### Rival BLAZe
- **@ Oak's Lab:** Eevee (Lv 5).
- **@ Route 22:** Pidgeotto (Lv 9), Rattata (Lv 8), Eevee (Lv 10).
- **@ Cerulean City (North):** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).

### Wild Pokémon Intel
- **Route 24 Venonat (Lv 16):** Knows DISABLE, SUPERSONIC, TACKLE.

## 3. Key NPCs & Events
- **Bill & S.S. Ticket:** After fixing his teleporter experiment on Route 25, Bill gave me the S.S. Ticket. This is for the S.S. Anne in Vermilion City.
- **Cerulean City Team Rocket Plot:** A Rocket stole a TM for DIG from a Fishing Guru in the house at (28, 12). I defeated the Rocket and recovered TM28 (DIG).

## 4. Agent Development Log
- `battle_navigator_agent`: Updated for better consolidation & to fix switch confirmation logic.
- `exp_tracker_agent`: Created to monitor EXP/level cap.
- `party_manager_agent`: Created for party composition suggestions.
- `item_finder_agent`: Updated to find named NPCs.
- **NEW:** `wkg_updater_agent` created to automate WKG updates.

## 5. Untested Hypotheses & Plans
- **Agent Dev Note:** Deleting `exp_tracker_agent` to make space for a new `wkg_updater_agent` to streamline map data management.

- **NEW AGENT IDEA:** `progression_advisor_agent`. Input: badges, location. Output: Suggests the next logical major objective (e.g., next city/gym) to prevent getting fixated on incorrect paths.

- **Underground Path Item Hint:** A girl in the southern exit room mentioned that people often lose things in the tunnel. This could be a clue for a hidden item.

- **Poison Fainting:** A Sailor in Vermilion Pokecenter confirmed that a poisoned Pokémon can faint from taking damage while walking outside of battle.