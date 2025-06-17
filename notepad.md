# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Discoveries
- **NPC Interaction:** Non-battling trainers give dialogue once and then act as walls. Mark and move on.
- **Poison Damage:** Poisoned Pokémon lose 1 HP every 4 steps outside battle.
- **Level Cap EXP:** Pokémon at the level cap show an EXP gain message, but their actual EXP value does not increase (visual bug).
- **Sandshrew Typing:** Confirmed as pure GROUND type (vs. Youngster on Route 25).
- **Post-Battle Status Cure:** Non-volatile status conditions (e.g., Poison) are automatically cured after trainer battles.
- **PC System:** 'SOMEONE's PC' is for Pokémon Storage. 'Gem's PC' is for Item Storage.

## 2. Lessons Learned & Tactical Adjustments
- **Defeated Trainers are Impassable:** Always plan routes *around* them. (Learned on Nugget Bridge).
- **Systematic Exploration:** When a path is blocked or a menu option fails, test all other possibilities methodically before assuming a dead end or repeating the failed action. (Learned from Route 25 & PC menu loops).
- **NPC Roles:** Do not assume an NPC is a standard trainer. Some may be for trades or other events. (Learned from Cool Trainer F on Route 25).

## 3. Battle Intel
### Gym Leaders
- **Brock (Pewter City - DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Misty (Cerulean City):** Psyduck (Lv 18), Goldeen (Lv 18), Starmie (Lv 21).
  - **Intel:** Starmie (Water/Psychic) is fast and hits hard with Bubblebeam & Confusion. It's the primary threat.
  - **Strategy:** Lead with SPARKY (Pikachu) for a strong Electric advantage. SPROUT (Oddish) is a solid backup with Grass typing to resist Water moves. The level cap is 21.

### Rival BLAZe
- **@ Oak's Lab:** Eevee (Lv 5).
- **@ Route 22:** Pidgeotto (Lv 9), Rattata (Lv 8), Eevee (Lv 10).
- **@ Cerulean City (North):** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).

## 4. Key NPCs & Events
- **Route 25 Trade:** Cool Trainer F at (38, 5) wants to trade a CLEFAIRY. This is required to pass.
- **Cerulean City Blockage:** A police officer blocks the path to a 'burgled house'. Hypothesis: Helping Bill on Route 25 will resolve this.

## 5. Agent Development Log
- `battle_navigator_agent`: Updated for better consolidation.
- `exp_tracker_agent`: Created to monitor EXP/level cap.
- `party_manager_agent`: Created for party composition suggestions.
- `item_finder_agent`: Updated to find named NPCs.