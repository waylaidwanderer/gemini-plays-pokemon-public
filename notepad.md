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

## 3. Battle Intel
### Gym Leaders
- **Brock (Pewter City - DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Misty (Cerulean City - DEFEATED):** Psyduck (Lv 18), Goldeen (Lv 18), Starmie (Lv 21).
  - **Intel:** Starmie (Water/Psychic) is very fast. Paralysis was key to victory.

- **CUT Unlocked:** After getting the Cascade Badge, I can now use the move CUT to chop down small bushes outside of battle.

### Rival BLAZe
- **@ Oak's Lab:** Eevee (Lv 5).
- **@ Route 22:** Pidgeotto (Lv 9), Rattata (Lv 8), Eevee (Lv 10).
- **@ Cerulean City (North):** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).

### Wild Pokémon Intel
- **Route 24 Venonat (Lv 16):** Knows DISABLE, SUPERSONIC, TACKLE.

## 4. Key NPCs & Events
- **Route 25 Trade:** Cool Trainer F at (38, 5) wants to trade a CLEFAIRY, but she can be bypassed by walking around her to the south.
S.S. Ticket Acquired: Bill gave me the S.S. Ticket for the S.S. Anne in Vermilion City. My hypothesis that this would move the officer blocking the path behind the burgled house was incorrect. The ticket's purpose is likely for an event within Vermilion City itself.

## 5. Agent Development Log
- `battle_navigator_agent`: Updated for better consolidation & to fix switch confirmation logic.
- `exp_tracker_agent`: Created to monitor EXP/level cap.
- `party_manager_agent`: Created for party composition suggestions.
- `item_finder_agent`: Updated to find named NPCs.

### Party & Training Notes
- **PIP (Pidgey):** Leveled to 19 and learned WING ATTACK. Its evolution was triggered, but I accidentally cancelled it. I need to remember that pressing 'B' during evolution stops it.

- **HM Usage (CUT):** The ability to use CUT is granted by the Cascade Badge. It is not used from a menu. To use it, stand in front of a cuttable tree and interact with it directly by pressing 'A'.

## 6. Untested Hypotheses