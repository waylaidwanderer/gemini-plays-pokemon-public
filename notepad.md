# Gem's Log: Pokémon Yellow Legacy - Hard Mode

## I. Current Status & Active Plans

### A. Pokémon Party (Turn 2678)
1. SPROUT (ODDISH): Lv10 (23/32 HP, EXP: 649) | Moves: TACKLE (5 PP), POISONPOWDER (35 PP), LEECH SEED (5 PP)
2. PIP (PIDGEY): Lv9 (21/27 HP, EXP: 523) | Moves: GUST (15 PP), SAND-ATTACK (15 PP)
3. SPARKY (PIKACHU): Lv12 (38/38 HP, EXP: 1728) | Moves: THUNDERSHOCK (28 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP) - AT LEVEL CAP (0 Badges).

### B. Financial Status
- Money: ¥296

### C. Current Location & Immediate Objective
- Location: Route 22 (ID: 33), at (33,12) (Turn 2678).
- Immediate Objective: Train SPROUT and PIP in the eastern grass patch of Route 22.

## II. Game Mechanics & Rules

### A. Hard Mode Rules
- Battle Style: Set.
- No items allowed in battle.
- Level caps: Pokémon cannot exceed cap for current badge count. (0 badges=12, 1=21, 2=24, 3=35, 4=43, 5=50, 6=53, 7=55, 8=65). EXP gain messages for capped Pokémon are visual only.

### B. General Game Changes (Pokémon Yellow Legacy)
- HMs: Forgettable, menu-use, not PC-storable. CUT is Bug-type.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses, unlimited enemy PP.
- EXP. All obtainable without special requirements.

### C. Discovered Mechanics
- Poison: 1 HP lost per 4 steps outside battle.
- STAT Experience: Significant stat boosts from battling/leveling.
- PC Log Off: Saves game.
- Evolution: By training.
- Wild Battle Escapes: Speed-dependent. If lead Pokémon's Speed >= wild's, escape is guaranteed.
- DV Checking: Hold START, then press A on STATS in Pokémon menu.
- Party Order: The lead Pokémon (first in the list) is always sent out first in battle.

## III. World Knowledge & Exploration

### A. Defeated Trainers
- Bug Catcher (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (31,34) in Viridian Forest. (Marker ☠️ set)
- Cooltrainer F (ID 5, LASS) at (3,42) in Viridian Forest. (Marker ☠️ set)
- Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest. (Marker ☠️ set)
- Rival BLAZe (Route 22, (30,5)) - Defeated SPEAROW Lv9, EEVEE Lv8. Earned ¥280. (Marker ☠️ set)

### B. Verified Type Matchups
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

### C. NPC Interaction Log & Key Dialogue
- **Viridian Old Man (ID 5, (20,14) Viridian):** Taught catching, unblocked path N. (Marker ✅ set)
- **Pewter Gym Guide (Pewter Gym):** Brock's Lead: GEODUDE (Offense, Rock Throw). Other: ONIX (Defense, BIND). Electric harmless vs Ground.
- **Pewter Nidoran House Man (Pewter Nidoran House):** Traded Pokémon grow fast but might ignore unskilled trainers; BADGEs help.
- **VIRIDIANCITY_YOUNGSTER2 (ID 3, (28,18) Viridian):** Non-battling. Explained DVs.

## IV. Agent Management

### A. Defined Agents (Updated Turn 2678)
1.  `level_cap_compliance_checker`
2.  `item_finder_agent`
3.  `wkg_transition_recorder_agent`
4.  `battle_strategist_agent`
5.  `pathfinding_agent`
6.  `exploration_helper_agent`

### B. Agent Improvement Tasks
- **(Deferred) `pathfinding_agent` & `exploration_helper_agent`:** Prompts need significant update to handle ledges correctly. Deferring fix until more complex navigation is required.

### C. Future Agent Ideas (To Be Actioned)
- **`training_hotspot_tracker`:** To suggest optimal training locations based on discoveries.
- **`shop_inventory_agent`:** To log and recall items sold in different Poké Marts.

## V. Lessons Learned & Strategic Refinements

- **Notepad `replace` Action:** Requires absolute precision for `old_text`. If an edit fails repeatedly, using `overwrite` for a larger section is more efficient than multiple failed `replace` attempts.
- **Party Order:** The Pokémon in the first slot of the party is always the one to enter battle first. This is not an 'auto-switch' mechanic.
- **Task Management:** Completed tasks must be removed from the notepad immediately to maintain an accurate to-do list.

## VI. Task List (Current)
- **(Active) Training:** Level SPROUT to 12 and PIP to 10 on Route 22.
- **(Deferred) Agent Prompt Fixes:** Address ledge-handling for navigation agents when necessary.
- **(Future) Agent Definition:** Define `training_hotspot_tracker` and `shop_inventory_agent` when strategically beneficial.